#!/bin/bash

echo "Testing Flask API endpoints..."

echo -e "\n1. Testing GET / (Home endpoint):"
curl -X GET http://localhost:5000/

echo -e "\n\n2. Testing GET /health (Health check):"
curl -X GET http://localhost:5000/health

echo -e "\n\n3. Testing GET /api/data (Get sample data):"
curl -X GET http://localhost:5000/api/data

echo -e "\n\n4. Testing POST /api/data (Create new data):"
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item", "value": 150}'

echo -e "\n\n5. Testing POST /api/data (Create another item):"
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name": "Another Item", "value": 250}'

echo -e "\n\n6. Testing POST /api/data (Empty data - should use defaults):"
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{}'

echo -e "\n\n7. Testing POST /api/data (No data - should return error):"
curl -X POST http://localhost:5000/api/data

echo -e "\n\nAPI testing complete!"
