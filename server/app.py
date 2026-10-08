from flask import Flask, request, jsonify
from flask_cors import CORS

from dictionary_api import get_definitions
from language_detect import detect_language

app = Flask(__name__)
CORS(app)

@app.route("/search", methods=["POST"])
def search():

    data = request.get_json(silent=True)
    word = data.get("word") if isinstance(data, dict) else None

    if not isinstance(word, str) or not word.strip():
        return jsonify({"error": "No word provided"}), 400

    word = word.strip()
    language = detect_language(word)

    definitions = get_definitions(word)

    return jsonify({
        "detected_language": language,
        "definitions": definitions
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
