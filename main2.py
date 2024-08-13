from flask import Flask, request, jsonify
import tiktokvoice

app = Flask(__name__)

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