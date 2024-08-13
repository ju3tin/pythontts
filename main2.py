import os
import urllib.request
   # from app import app
from flask import Flask, request, redirect, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import tiktokvoice

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)


@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text')
    voice = data.get('voice')
    filename = data.get('filename', 'output.mp3')
    play = data.get('play', False)

    if not text:
        return jsonify({"error": "Text input is required"}), 400
    if not voice:
        return jsonify({"error": "Voice selection is required"}), 400

    # Execute TTS
    output_file_path = os.path.join(output_dir, filename)
    tiktokvoice.tts(text, voice, output_file_path, play)
    return jsonify({"message": "TTS generated successfully", "filename": output_file_path}), 200
@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({"message": "api ready"}), 200
@app.route('/get-file/<filename>', methods=['GET'])
def get_file(filename):
    try:
        return send_from_directory(output_dir, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)
