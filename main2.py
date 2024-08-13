import os
import urllib.request
   # from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import tiktokvoice

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
    tiktokvoice.tts(text, voice, filename, play)
    return jsonify({"message": "TTS generated successfully", "filename": filename}), 200
@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({"message": "api ready"}), 200
if __name__ == "__main__":
    app.run(debug=True)
