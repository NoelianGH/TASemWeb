const fs = require('fs');
const path = require('path');

const ontologyPath = process.env.ONTOLOGY_PATH || './ontology/nusarasa_ontology.ttl';

// Get ontology info
exports.getOntologyInfo = async () => {
  try {
    const fullPath = path.join(__dirname, '../..', ontologyPath);
    const stats = fs.statSync(fullPath);
    
    return {
      name: 'Nusarasa Ontology',
      path: ontologyPath,
      size: stats.size,
      lastModified: stats.mtime,
      description: 'Ontology for Indonesian culinary semantic web'
    };
  } catch (error) {
    throw new Error(`Failed to read ontology: ${error.message}`);
  }
};

// Get all classes (placeholder - needs RDF parsing)
exports.getAllClasses = async () => {
  try {
    const fullPath = path.join(__dirname, '../..', ontologyPath);
    const content = fs.readFileSync(fullPath, 'utf-8');
    
    // Extract rdfs:Class definitions
    const classRegex = /rdf:type\s+rdfs:Class|rdfs:Class|owl:Class/g;
    const matches = content.match(classRegex) || [];
    
    return [
      {
        id: 'Food',
        label: 'Food',
        description: 'Food items'
      },
      {
        id: 'Recipe',
        label: 'Recipe',
        description: 'Culinary recipes'
      },
      {
        id: 'Ingredient',
        label: 'Ingredient',
        description: 'Food ingredients'
      },
      {
        id: 'Region',
        label: 'Region',
        description: 'Indonesian regions'
      }
    ];
  } catch (error) {
    throw new Error(`Failed to parse classes: ${error.message}`);
  }
};

// Get all properties (placeholder)
exports.getAllProperties = async () => {
  try {
    return [
      {
        id: 'hasIngredient',
        label: 'Has Ingredient',
        domain: 'Recipe',
        range: 'Ingredient'
      },
      {
        id: 'fromRegion',
        label: 'From Region',
        domain: 'Food',
        range: 'Region'
      },
      {
        id: 'hasFlavor',
        label: 'Has Flavor',
        domain: 'Food',
        range: 'String'
      },
      {
        id: 'preparationTime',
        label: 'Preparation Time',
        domain: 'Recipe',
        range: 'Integer'
      }
    ];
  } catch (error) {
    throw new Error(`Failed to parse properties: ${error.message}`);
  }
};

// Get class details
exports.getClassDetails = async (name) => {
  try {
    const classes = await exports.getAllClasses();
    const classDetail = classes.find(c => c.id.toLowerCase() === name.toLowerCase());
    
    if (!classDetail) {
      throw new Error(`Class ${name} not found`);
    }
    
    return classDetail;
  } catch (error) {
    throw new Error(`Failed to get class details: ${error.message}`);
  }
};

// Get property details
exports.getPropertyDetails = async (name) => {
  try {
    const properties = await exports.getAllProperties();
    const propDetail = properties.find(p => p.id.toLowerCase() === name.toLowerCase());
    
    if (!propDetail) {
      throw new Error(`Property ${name} not found`);
    }
    
    return propDetail;
  } catch (error) {
    throw new Error(`Failed to get property details: ${error.message}`);
  }
};
