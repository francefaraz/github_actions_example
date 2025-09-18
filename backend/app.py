from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
app.config['PORT'] = int(os.environ.get('PORT', 5000))
app_datas={}
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Backend API BY Munexa Studio (MuneerFaraz)',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'backend'
    })

@app.route('/api/data')
def get_data():
    sample_data=[
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200},
        {'id': 3, 'name': 'Item 3', 'value': 300}
    ]
    sample_data.append(app_datas)
    return jsonify({
        'data': sample_data
    })
@app.route('/aboutme')
def about():
    return jsonify({
        'message': 'About page',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Simulate creating new data
    new_item = {
        'id': len(data.get('items', [])) + 1,
        'name': data.get('name', 'New Item'),
        'value': data.get('value', 0)
    }
    app_datas.update(new_item)
    return jsonify({
        'message': 'Data created successfully',
        'item': new_item
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])

# from flask import Flask, jsonify, request

# app=Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello, World!'})
# if __name__=='main':
#     app.run(host='0.0.0.0', port=5000, debug=True)