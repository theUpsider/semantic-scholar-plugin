from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS  # Import the CORS package
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Serve .well-known/ai-plugin.json
@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_manifest():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ai-plugin.json')

# Serve openapi.yaml
@app.route('/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'openapi.yaml')

@app.route('/', methods=['GET'])
def serve_index():
    return jsonify({
        "message": "Welcome to the AI Plugin for Semantic Scholar!"
    })

# Search papers on Semantic Scholar
@app.route('/search_papers', methods=['GET'])
def search_papers():
    query = request.args.get('query')
    offset = request.args.get('offset', 10)
    limit = request.args.get('limit', 50)
    fields = "title,authors,abstract"
    
    response = requests.get(f"http://api.semanticscholar.org/graph/v1/paper/search?query={query}&offset={offset}&limit={limit}&fields={fields}")
    return jsonify(response.json())

if __name__ == '__main__':
    # serve on 0.0.0.0
    app.run(host='0.0.0.0', port=5337, debug=True)
