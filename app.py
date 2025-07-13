from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime

app = Flask(__name__)

api_key = os.environ.get('GOOGLE_API_KEY', "AIzaSyBLlgvyKtYtnMKEFql4OgLV85iLkY5tweQ")

try:
    genai.configure(api_key=api_key)
    models = genai.list_models()
    print(f"Available models: {[model.name for model in models]}")
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        print("Using Gemini 2.0 Flash model")
    except:
        model = genai.GenerativeModel('gemini-pro')
        print("Using Gemini Pro model (fallback)")
    
    api_working = True
except Exception as e:
    print(f"API Key Error: {str(e)}")
    print("Please get a valid API key from: https://makersuite.google.com/app/apikey")
    api_working = False
    model = None

chat_history = []

@app.route('/')
def index():
    return render_template('index.html', history=chat_history)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({'reply': 'Please enter a message.'})
        
        if not api_working:
            return jsonify({'reply': 'API Key Error: Please set a valid Google Gemini API key. Get one from https://makersuite.google.com/app/apikey'})
        
        chat_history.append({
            'role': 'user',
            'text': user_message,
            'timestamp': datetime.now().strftime('%H:%M')
        })
        
        conversation = []
        for msg in chat_history[-10:]:
            if msg['role'] == 'user':
                conversation.append(f"User: {msg['text']}")
            else:
                conversation.append(f"Assistant: {msg['text']}")
        
        prompt = f"""You are a helpful AI assistant. Give direct, concise answers in 1-2 sentences maximum. Be friendly but brief.

Previous conversation:
{chr(10).join(conversation[:-1]) if len(conversation) > 1 else 'No previous conversation.'}

Current user message: {user_message}

Provide a brief, direct response:"""
        
        response = model.generate_content(prompt)
        bot_reply = response.text.strip()
        
        chat_history.append({
            'role': 'bot',
            'text': bot_reply,
            'timestamp': datetime.now().strftime('%H:%M')
        })
        
        return jsonify({'reply': bot_reply})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        error_msg = "Sorry, I encountered an error. Please check your API key and try again."
        if "API_KEY_INVALID" in str(e) or "API Key not found" in str(e):
            error_msg = "Invalid API Key: Please get a valid API key from https://makersuite.google.com/app/apikey"
        return jsonify({'reply': error_msg})

@app.route('/clear', methods=['POST'])
def clear_history():
    global chat_history
    chat_history = []
    return jsonify({'status': 'success'})

@app.route('/status')
def status():
    return jsonify({
        'api_working': api_working,
        'message': 'API is working correctly' if api_working else 'API key is invalid or missing'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
