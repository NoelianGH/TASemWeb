const queryService = require('../services/queryService');
const nl2sparqlService = require('../services/nl2sparqlService');

// Execute SPARQL-like query
exports.executeSparqlQuery = async (req, res) => {
  try {
    const { query } = req.body;
    if (!query) {
      return res.status(400).json({ error: 'Query is required' });
    }
    const results = await queryService.executeSparqlQuery(query);
    res.json({ results });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Execute semantic search
exports.semanticSearch = async (req, res) => {
  try {
    const { keyword, ontologyClass } = req.body;
    if (!keyword) {
      return res.status(400).json({ error: 'Keyword is required' });
    }
    const results = await queryService.semanticSearch(keyword, ontologyClass);
    res.json({ results, count: results.length });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get related resources
exports.getRelatedResources = async (req, res) => {
  try {
    const { resource } = req.params;
    const related = await queryService.getRelatedResources(resource);
    res.json({ resource, related });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Translate NL to SPARQL and execute
exports.translateAndExecute = async (req, res) => {
  try {
    const { question } = req.body;
    if (!question) {
      return res.status(400).json({ error: 'Question is required' });
    }
    
    let sparql, explanation, formattedResults = [];
    let maxRetries = 3;
    let attempt = 0;
    let errorFeedback = null;
    let success = false;
    let lastError = null;
    
    while (attempt < maxRetries && !success) {
      try {
        const temperature = 0.1 + (attempt * 0.2); // Increase temp to 0.3 then 0.5
        const translationResult = await nl2sparqlService.translate(question, errorFeedback, temperature);
        sparql = translationResult.sparql;
        explanation = translationResult.explanation;
        
        // Execute generated SPARQL
        const rawResults = await queryService.executeSparqlQuery(sparql);
        
        if (rawResults && rawResults.length > 0) {
          const sparqlClient = require('../services/sparqlClient');
          formattedResults = rawResults.map(b => ({
            id: b.dish ? sparqlClient.localName(sparqlClient.val(b, 'dish')) : 'unknown',
            nama: sparqlClient.val(b, 'name') || sparqlClient.val(b, 'nama') || 'Tanpa Nama',
            deskripsi: sparqlClient.val(b, 'description') || sparqlClient.val(b, 'desc'),
            daerah: sparqlClient.val(b, 'region_name') || sparqlClient.val(b, 'regionName') || sparqlClient.val(b, 'region'),
            tingkat_kepedasan: sparqlClient.val(b, 'spice_level') || sparqlClient.val(b, 'spice'),
            kategori_diet: sparqlClient.val(b, 'diet_category') || sparqlClient.val(b, 'diet')
          }));
          success = true;
        } else {
          // No results found
          errorFeedback = "The previous SPARQL query executed successfully but returned 0 results. Please double check the prefixes and try a broader search, relax some strict filters, or ensure you are using LCASE(STR(?var)) inside CONTAINS().";
          attempt++;
        }
      } catch (err) {
        // Syntax error or other execution error
        errorFeedback = `The previous SPARQL query failed with error: ${err.message}. Please fix the syntax or logic.`;
        lastError = err;
        attempt++;
      }
    }
    
    // If all attempts failed, we return the last parsed data or an empty result set
    res.json({ 
      sparql: sparql || "Query failed to generate",
      explanation: explanation || (lastError ? `Error: ${lastError.message}` : "Tidak ditemukan kueri yang cocok."),
      results: formattedResults 
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
