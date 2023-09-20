from flask import Flask, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__)

# Serve ai-plugin.json
@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_manifest():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ai-plugin.json')

# Serve openapi.yaml
@app.route('/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'openapi.yaml')

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
    app.run(port=5337)
