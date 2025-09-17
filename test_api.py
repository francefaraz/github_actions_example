#!/usr/bin/env python3
import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_api():
    print("Testing Flask API endpoints...\n")
    
    # Test 1: Home endpoint
    print("1. Testing GET / (Home endpoint):")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Health check
    print("2. Testing GET /health (Health check):")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 3: Get data
    print("3. Testing GET /api/data (Get sample data):")
    try:
        response = requests.get(f"{BASE_URL}/api/data")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 4: POST data - Success case
    print("4. Testing POST /api/data (Create new data):")
    try:
        data = {"name": "Test Item", "value": 150}
        response = requests.post(f"{BASE_URL}/api/data", json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 5: POST data - Another item
    print("5. Testing POST /api/data (Create another item):")
    try:
        data = {"name": "Another Item", "value": 250}
        response = requests.post(f"{BASE_URL}/api/data", json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 6: POST data - Empty data (should use defaults)
    print("6. Testing POST /api/data (Empty data - should use defaults):")
    try:
        data = {}
        response = requests.post(f"{BASE_URL}/api/data", json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 7: POST data - No data (should return error)
    print("7. Testing POST /api/data (No data - should return error):")
    try:
        response = requests.post(f"{BASE_URL}/api/data")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    print("API testing complete!")

if __name__ == "__main__":
    test_api()
