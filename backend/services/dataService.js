const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const dataPath = process.env.DATA_PATH || './data/dataset_kuliner_indonesia.csv';

let dataCache = null;

// Load CSV data
const loadData = async () => {
  if (dataCache) return dataCache;
  
  const fullPath = path.join(__dirname, '../..', dataPath);
  const data = [];
  
  return new Promise((resolve, reject) => {
    fs.createReadStream(fullPath)
      .pipe(csv())
      .on('data', (row) => {
        data.push({
          id: data.length + 1,
          ...row
        });
      })
      .on('end', () => {
        dataCache = data;
        resolve(data);
      })
      .on('error', (error) => {
        reject(error);
      });
  });
};

// Get all data with pagination
exports.getAllData = async (page = 1, limit = 20) => {
  try {
    const data = await loadData();
    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + limit;
    
    const items = data.slice(startIndex, endIndex);
    
    return {
      page: parseInt(page),
      limit: parseInt(limit),
      total: data.length,
      items
    };
  } catch (error) {
    throw new Error(`Failed to get data: ${error.message}`);
  }
};

// Get data by ID
exports.getDataById = async (id) => {
  try {
    const data = await loadData();
    return data.find(item => item.id === parseInt(id));
  } catch (error) {
    throw new Error(`Failed to get data by ID: ${error.message}`);
  }
};

// Search data
exports.searchData = async (query) => {
  try {
    const data = await loadData();
    const lowerQuery = query.toLowerCase();
    
    return data.filter(item => {
      return Object.values(item).some(value =>
        String(value).toLowerCase().includes(lowerQuery)
      );
    });
  } catch (error) {
    throw new Error(`Failed to search data: ${error.message}`);
  }
};

// Get data statistics
exports.getDataStats = async () => {
  try {
    const data = await loadData();
    
    return {
      totalRecords: data.length,
      lastUpdated: new Date().toISOString(),
      columns: data.length > 0 ? Object.keys(data[0]) : []
    };
  } catch (error) {
    throw new Error(`Failed to get data stats: ${error.message}`);
  }
};
