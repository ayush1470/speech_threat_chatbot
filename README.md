# Speech Threat Chatbot Model (Flask API for Speech-to-Threat Analysis)

This Flask-based API processes audio files, converts speech to text, and analyzes the text for potential threats using an AI-powered chatbot. The system assigns a threat score (1 to 5) and detects potentially dangerous messages.

## Features
- **Chatbot**: Generates responses to questions provided by user using Microsoft ChatGPT 3.5 LLM tool provided by aiXplain.
- **Speech-to-Text**: Converts audio files into text using AWS speech recognition tool provided by aiXplain.
- **Threat Analysis**: AI-powered chatbot assesses threat levels in transcribed text.
- **File Conversion**: Supports WAV, MP3, M4A, OGG formats and converts them to WAV/MP3.
- **CORS Enabled**: Allows frontend integration.
- **Secure Uploads**: Stores audio files temporarily in a safe location.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/speech_threat_chatbot.git
cd speech_threat_chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv 
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file or export the required environment variables:

```bash
export AIXPLAIN_API_KEY="your_aixplain_api_key"
export FFMPEG_PATH="/path/to/ffmpeg"  # If necessary
```

**Note**: The API requires an AIXPLAIN API Key to access speech recognition and chatbot services.

### 5. Run the Flask API
```bash
python app.py
```

## Usage
Once the server is running, you can send requests to analyze audio files or interact with the chatbot.

### 1. Analyze Audio for Threat Detection

#### Request (Using cURL)
```bash
curl -X POST http://localhost:5000/analyze-audio \
     -F "audio=@sample.wav"
```

#### Response Example
```json
{
    "transcribed_text": "This is a test message",
    "threat_score": 3,
    "is_threat": 0,
    "mp3_path": "processed/converted.mp3"
}
```
- **threat_score (1-5)**: Severity rating.
- **is_threat: 1** → Threat detected (Score 4-5).
- **is_threat: 0** → Normal message.

### 2. Chatbot Follow-Up

#### Request (Using cURL)
```bash
curl -X POST http://localhost:5000/chatbot \
     -H "Content-Type: application/json" \
     -d '{"text": "What should I do in case of a threat?"}'
```

#### Response Example
```json
{
    "response": "You should immediately contact emergency services."
}
```

## API Endpoints
| Method | Endpoint        | Description |
|--------|----------------|-------------|
| POST   | `/analyze-audio` | Processes audio, transcribes speech, and analyzes threat level. |
| POST   | `/chatbot`      | AI chatbot for follow-up questions. |

## Supported Audio Formats
- **Input**: WAV, MP3, M4A, OGG
- **Output**: Converted to WAV and MP3 for processing.

## Environment Variables
| Variable Name | Description |
|--------------|-------------|
| `AIXPLAIN_API_KEY` | API key for speech recognition and chatbot services. |
| `FFMPEG_PATH` | Path to FFmpeg (optional, for audio conversion). |

**Best Practice:** Store credentials in a `.env` file or system environment variables instead of hardcoding them.
