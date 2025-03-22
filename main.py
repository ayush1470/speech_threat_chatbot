# from flask import Flask, request, jsonify
# from aixplain.factories import ModelFactory
# import re
# import os
#
# os.environ["AIXPLAIN_API_KEY"] = "1b77c0afde7a91f063092bdbad58a542970e5632d8d8ea18f10cbf977bae6920"
#
# app = Flask(__name__)
#
# # Load AI tools
# chatbot_tool = ModelFactory.get("646796796eb56367b25d0751")  # Chatbot (Azure GPT-3.5)
# speech_recognition_tool = ModelFactory.get("6610617ff1278441b6482530")  # Speech recognition (AWS)
#
#
# # API route to process an uploaded .wav file
# @app.route('/analyze-audio', methods=['POST'])
# def analyze_audio():
#     if 'audio' not in request.files:
#         return jsonify({"error": "No audio file provided"}), 400
#
#     audio_file = request.files['audio']
#     wav_path = os.path.join("/tmp", audio_file.filename)
#     audio_file.save(wav_path)
#
#     # Step 1: Convert Speech to Text
#     speech_result = speech_recognition_tool.run({"source_audio": wav_path})
#     transcribed_text = speech_result.data if speech_result and speech_result.data else ""
#
#     if not transcribed_text:
#         return jsonify({"error": "Speech recognition failed"}), 500
#
#     # Step 2: Chatbot Analyzes Threat Level
#     masked_text = transcribed_text.replace("serious consequences", "[redacted]")
#     chat_result = chatbot_tool.run({
#         "text": f"Analyze this message and provide a risk assessment rating from 1 (not concerning) to 5 (highly concerning). Only reply with the number. Message: '{masked_text}'"
#     })
#
#     if not chat_result or not chat_result.data:
#         return jsonify({"error": "Chatbot analysis failed"}), 500
#
#     response_text = chat_result.data.strip()
#     match = re.search(r'\b[1-5]\b', response_text)
#
#     if match:
#         score = int(match.group())
#         is_threat = 1 if score >= 4 else 0  # Consider 4+ as a threat
#     else:
#         is_threat = -1  # Fallback if parsing fails
#
#     return jsonify({"transcribed_text": transcribed_text, "threat_score": score, "is_threat": is_threat})
#
#
# # API route for chatbot follow-up questions
# @app.route('/chatbot', methods=['POST'])
# def chatbot_response():
#     data = request.json
#     user_query = data.get("text", "")
#
#     if not user_query:
#         return jsonify({"error": "No query provided"}), 400
#
#     chat_result = chatbot_tool.run({"text": user_query})
#     return jsonify({"response": chat_result.data if chat_result and chat_result.data else "No response"})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#



# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from aixplain.factories import ModelFactory
# import re
# import os
# from werkzeug.utils import secure_filename
# from pydub import AudioSegment
#
#
# os.environ["PATH"] += os.pathsep + r"C:\Program Files\ffmpeg-2025-03-20-git-76f09ab647-essentials_build\bin"
#
# # Set API Key for aiXplain tools
# os.environ["AIXPLAIN_API_KEY"] = "1b77c0afde7a91f063092bdbad58a542970e5632d8d8ea18f10cbf977bae6920"
#
# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend integration
#
# # Allowed audio formats
# ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a', 'ogg'}
#
# # Load AI tools
# chatbot_tool = ModelFactory.get("646796796eb56367b25d0751")  # Chatbot (Azure GPT-3.5)
# speech_recognition_tool = ModelFactory.get("6610617ff1278441b6482530")  # Speech recognition (AWS)
#
# # Function to check allowed file type
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# # Function to convert audio file to WAV format
# def convert_to_wav(audio_path, output_path):
#     audio = AudioSegment.from_file(audio_path)
#     audio.export(output_path, format="wav")
#
# # API route to process an uploaded audio file
# @app.route('/analyze-audio', methods=['POST'])
# def analyze_audio():
#     if 'audio' not in request.files:
#         return jsonify({"error": "No audio file provided"}), 400
#
#     audio_file = request.files['audio']
#
#     # Check for valid audio format
#     if not allowed_file(audio_file.filename):
#         return jsonify({"error": "Invalid file format. Only WAV, MP3, M4A, and OGG are allowed."}), 400
#
#     filename = secure_filename(audio_file.filename)
#     temp_path = os.path.join("/tmp", filename)
#     wav_path = os.path.join("/tmp", "converted.wav")  # Standard WAV file path
#
#     audio_file.save(temp_path)
#
#     # Convert to WAV if needed
#     if not filename.endswith(".wav"):
#         convert_to_wav(temp_path, wav_path)
#     else:
#         wav_path = temp_path  # No conversion needed if already WAV
#
#     # Step 1: Convert Speech to Text
#     speech_result = speech_recognition_tool.run({"source_audio": wav_path})
#     transcribed_text = speech_result.data if speech_result and speech_result.data else ""
#
#     if not transcribed_text:
#         return jsonify({"error": "Speech recognition failed"}), 500
#
#     # Step 2: Chatbot Analyzes Threat Level
#     masked_text = transcribed_text.replace("serious consequences", "[redacted]")
#     chat_result = chatbot_tool.run({
#         "text": f"Analyze this message and provide a risk assessment rating from 1 (not concerning) to 5 (highly concerning). Only reply with the number. Message: '{masked_text}'"
#     })
#
#     if not chat_result or not chat_result.data:
#         return jsonify({"error": "Chatbot analysis failed"}), 500
#
#     response_text = chat_result.data.strip()
#     match = re.search(r'\b[1-5]\b', response_text)
#
#     if match:
#         score = int(match.group())
#         is_threat = 1 if score >= 4 else 0  # Consider 4+ as a threat
#     else:
#         is_threat = -1  # Fallback if parsing fails
#
#     return jsonify({"transcribed_text": transcribed_text, "threat_score": score, "is_threat": is_threat})
#
#
# # API route for chatbot follow-up questions
# @app.route('/chatbot', methods=['POST'])
# def chatbot_response():
#     data = request.json
#     user_query = data.get("text", "")
#
#     if not user_query:
#         return jsonify({"error": "No query provided"}), 400
#
#     chat_result = chatbot_tool.run({"text": user_query})
#     return jsonify({"response": chat_result.data if chat_result and chat_result.data else "No response"})
#
# from pydub.utils import which
# print(which("ffmpeg"))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from aixplain.factories import ModelFactory
import re
import os
import subprocess
from werkzeug.utils import secure_filename
from pydub import AudioSegment

# Load environment variables
AIXPLAIN_API_KEY = os.getenv("AIXPLAIN_API_KEY")
FFMPEG_PATH = os.getenv("FFMPEG_PATH")

# Ensure API key is set
if not AIXPLAIN_API_KEY:
    raise ValueError("Missing AIXPLAIN_API_KEY environment variable!")

# Set FFmpeg Path if provided
if FFMPEG_PATH:
    os.environ["PATH"] += os.pathsep + FFMPEG_PATH

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Allowed audio formats
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a', 'ogg'}

# Create folders for audio storage
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load AI tools
chatbot_tool = ModelFactory.get("646796796eb56367b25d0751")  # Chatbot (Azure GPT-3.5)
speech_recognition_tool = ModelFactory.get("6610617ff1278441b6482530")  # Speech recognition (AWS)

# Function to check allowed file type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to convert audio file to WAV format
def convert_to_wav(audio_path, output_path):
    audio = AudioSegment.from_file(audio_path)
    audio.export(output_path, format="wav")

# Function to convert WAV to MP3 using FFmpeg
def convert_to_mp3(wav_path, mp3_path):
    ffmpeg_cmd = f'ffmpeg -i "{wav_path}" "{mp3_path}"'
    subprocess.run(ffmpeg_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# API route to process an uploaded audio file
@app.route('/analyze-audio', methods=['POST'])
def analyze_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']

    # Check for valid audio format
    if not allowed_file(audio_file.filename):
        return jsonify({"error": "Invalid file format. Only WAV, MP3, M4A, and OGG are allowed."}), 400

    filename = secure_filename(audio_file.filename)
    temp_path = os.path.join(UPLOAD_FOLDER, filename)
    wav_path = os.path.join(OUTPUT_FOLDER, "converted.wav")  # Standard WAV file path
    mp3_path = os.path.join(OUTPUT_FOLDER, "converted.mp3")  # MP3 output path

    audio_file.save(temp_path)

    # Convert to WAV if needed
    if not filename.endswith(".wav"):
        convert_to_wav(temp_path, wav_path)
    else:
        wav_path = temp_path  # No conversion needed if already WAV

    # Convert WAV to MP3
    convert_to_mp3(wav_path, mp3_path)

    # Step 1: Convert Speech to Text
    speech_result = speech_recognition_tool.run({"source_audio": wav_path})
    transcribed_text = speech_result.data if speech_result and speech_result.data else ""

    if not transcribed_text:
        return jsonify({"error": "Speech recognition failed"}), 500

    # Step 2: Chatbot Analyzes Threat Level
    masked_text = transcribed_text.replace("serious consequences", "[redacted]")
    chat_result = chatbot_tool.run({
        "text": f"Analyze this message and provide a risk assessment rating from 1 (not concerning) to 5 (highly concerning). Only reply with the number. Message: '{masked_text}'"
    })

    if not chat_result or not chat_result.data:
        return jsonify({"error": "Chatbot analysis failed"}), 500

    response_text = chat_result.data.strip()
    match = re.search(r'\b[1-5]\b', response_text)

    if match:
        score = int(match.group())
        is_threat = 1 if score >= 4 else 0  # Consider 4+ as a threat
    else:
        is_threat = -1  # Fallback if parsing fails

    return jsonify({
        "transcribed_text": transcribed_text,
        "threat_score": score,
        "is_threat": is_threat,
        "mp3_path": mp3_path  # Provide MP3 file path for reference
    })


# API route for chatbot follow-up questions
@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_query = data.get("text", "")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    chat_result = chatbot_tool.run({"text": user_query})
    return jsonify({"response": chat_result.data if chat_result and chat_result.data else "No response"})


if __name__ == '__main__':
    app.run(debug=True)