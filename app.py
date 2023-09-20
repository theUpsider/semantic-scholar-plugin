from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS  # Import the CORS package
import requests
import os

app = Flask(__name__)
# allow cors for all domains on all routes
CORS(app, resources={r"/*": {"origins": "*"}})


# Serve .well-known/ai-plugin.json
@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def serve_manifest():
    return send_from_directory(os.path.join(app.root_path, "static"), "ai-plugin.json")


# /legal
@app.route("/legal", methods=["GET"])
def serve_legal():
    return send_from_directory(os.path.join(app.root_path, "static"), "legal.html")


# Serve openapi.yaml
@app.route("/openapi.yaml", methods=["GET"])
def serve_openapi():
    return send_from_directory(os.path.join(app.root_path, "static"), "openapi.yaml")


@app.route("/", methods=["GET"])
def serve_index():
    return jsonify({"message": "Welcome to the AI Plugin for Semantic Scholar!"})


# Search papers on Semantic Scholar
@app.route("/search_papers", methods=["GET"])
def search_papers():
    query = request.args.get("query")
    offset = request.args.get("offset", 0)
    limit = request.args.get("limit", 10)
    fields = "title,authors,abstract,influentialCitationCount,citationCount"

    response = requests.get(
        f"http://api.semanticscholar.org/graph/v1/paper/search?query={query}&offset={offset}&limit={limit}&fields={fields}"
    )
    if response.status_code != 200:
        return jsonify({"message": "Nothing found"}), 404
    return jsonify(response.json())


# Detail on paper on Semantic Scholar
@app.route("/paper_detail", methods=["GET"])
def paper_detail():
    paper_id = request.args.get("paper_id")
    fields = "title,authors,abstract,venue,year,influentialCitationCount,citationCount,references"

    response = requests.get(
        f"http://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields={fields}"
    )
    if response.status_code != 200:
        return jsonify({"message": "Paper not found"}), 404
    return jsonify(response.json())


if __name__ == "__main__":
    # serve on 0.0.0.0
    app.run(host="0.0.0.0", port=5000, debug=False)
