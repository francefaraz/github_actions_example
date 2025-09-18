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

@app.route('/aboutllm')
def aboutllm():
    return (
        """
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Sample Info Page</title>
            <style>
              body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 40px; background:#0f172a; color:#e2e8f0; }
              .card { max-width: 720px; margin: 0 auto; background: #111827; border: 1px solid #1f2937; border-radius: 14px; padding: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.35); }
              h1 { margin: 0 0 8px; font-size: 32px; color:#a78bfa; }
              h2 { margin: 8px 0 16px; color:#34d399; font-weight: 600; }
              p { line-height: 1.6; color:#cbd5e1; }
              .badge { display:inline-block; padding:6px 10px; border-radius:999px; background:#0ea5e9; color:#0b1020; font-weight:700; margin-top:12px; }
              .glow { text-shadow: 0 0 8px rgba(167,139,250,0.65); }
            </style>
          </head>
          <body>
            <div class="card">
              <h1 class="glow">✨ Hello there!</h1>
              <h2>Random placeholder content below</h2>
              <p>
                This is a simple sample page rendered by Flask. No special keywords here,
                just clean vibes and a touch of neon.
              </p>
              <ul>
                <li>Penguins propose with pebbles.</li>
                <li>Honey never spoils.</li>
                <li>The Eiffel Tower can be 15 cm taller in summer.</li>
              </ul>
              <p>Need JSON instead? Try the <code>/api/data</code> endpoint.</p>
              <span class="badge">Munexa Studio • MuneerFaraz</span>
            </div>
          </body>
        </html>
        """
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])

# from flask import Flask, jsonify, request

# app=Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello, World!'})
# if __name__=='main':
#     app.run(host='0.0.0.0', port=5000, debug=True)