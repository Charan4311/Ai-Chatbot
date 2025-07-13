# 🤖 Gemini AI Chatbot

A modern, responsive web-based chatbot powered by Google's Gemini AI. Built with Flask and featuring a beautiful, mobile-friendly interface.

## ✨ Features

- **AI-Powered Conversations**: Powered by Google's Gemini Pro model
- **Modern UI**: Beautiful, responsive design with message bubbles
- **Real-time Chat**: Instant responses with typing indicators
- **Chat History**: Maintains conversation context
- **Clear Chat**: One-click chat history clearing
- **Mobile Responsive**: Works perfectly on all devices
- **Keyboard Support**: Press Enter to send messages

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get a valid API key**:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated key

4. **Set up your API key** (choose one method):

   **Option A: Environment Variable (Recommended)**
   ```bash
   set GOOGLE_API_KEY=your-api-key-here
   ```

   **Option B: Direct in code**
   Replace the API key in `app.py` line 12:
   ```python
   api_key = os.environ.get('GOOGLE_API_KEY', "YOUR_API_KEY_HERE")
   ```

5. **Test your API key**:
   ```bash
   python test_api.py
   ```

6. **Run the application**:
   ```bash
   python app.py
   ```

7. **Open your browser** and go to `http://localhost:5000`

## 🎭 Demo Mode

If you don't have an API key yet, you can test the interface with the demo version:

```bash
python demo_app.py
```

This runs a demo version that shows the chat interface without requiring an API key.

## 📁 Project Structure

```
chatbot/
├── app.py              # Main Flask application with Gemini AI
├── demo_app.py         # Demo version (no API key required)
├── test_api.py         # API key testing utility
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── list.py            # Utility to list available models
├── static/
│   └── index.css      # Styles for the chat interface
└── templates/
    └── index.html     # HTML template for the chat interface
```

## 🔧 Configuration

### API Key Security

For production use, it's recommended to set your API key as an environment variable:

```python
import os
api_key = os.environ.get('GOOGLE_API_KEY')
```

Then set the environment variable:
```bash
set GOOGLE_API_KEY="your-api-key-here"
```

### Model Selection

The chatbot uses the `gemini-pro` model by default. You can change this in `app.py`:

```python
model = genai.GenerativeModel('gemini-pro')  # Change model here
```

## 🎨 Customization

### Styling

The chat interface can be customized by modifying `static/index.css`. The design uses:
- CSS Grid and Flexbox for layout
- CSS custom properties for easy theming
- Smooth animations and transitions
- Mobile-first responsive design

### Chat Behavior

Modify the prompt in `app.py` to change how the AI responds:

```python
prompt = f"""You are a helpful AI assistant. Please respond to the user's message in a conversational and helpful manner.

Previous conversation:
{chr(10).join(conversation[:-1]) if len(conversation) > 1 else 'No previous conversation.'}

Current user message: {user_message}

Please provide a helpful and relevant response:"""
```

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Consider rate limiting for production use
- Implement user authentication for multi-user scenarios

## 🐛 Troubleshooting

### Common Issues

1. **"API Key not found" error**: 
   - Get a valid API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Test it with: `python test_api.py`

2. **"Module not found" errors**: 
   - Make sure you've installed all dependencies with `pip install -r requirements.txt`

3. **CORS issues**: 
   - The app runs locally, so CORS shouldn't be an issue, but if you deploy it, you may need to configure CORS headers

4. **Model not responding**: 
   - Check your internet connection and API key validity

### Debug Mode

The app runs in debug mode by default. For production, set `debug=False` in `app.py`.

## 📱 Mobile Support

The chatbot is fully responsive and works great on mobile devices. The interface automatically adapts to different screen sizes.

## 🚀 Deployment

### Local Network Access

To make the chatbot accessible on your local network, the app is configured to run on `0.0.0.0:5000`.

### Production Deployment

For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up proper environment variables
- Implementing rate limiting
- Adding user authentication
- Using HTTPS

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Enjoy chatting with your AI assistant! 🤖✨** 