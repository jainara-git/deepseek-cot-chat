# Deepseek CoT Chat

A Streamlit-based chat application that uses Deepseek's Chain-of-Thought (CoT) model to provide detailed reasoning alongside responses.

## Features

- Interactive chat interface
- Real-time streaming responses
- Visible reasoning process with expandable sections
- Chat history persistence within session

## Live Demo

You can try the application directly at: [deepseek-cot-chat.streamlit.app](https://deepseek-cot-chat.streamlit.app)

The hosted version is free to use and doesn't require any API key or setup.

## Local Deployment

### Prerequisites

- Python 3.x
- Streamlit
- OpenAI Python package
- Openrouter API key (make a free account)

### Setup

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install streamlit openai
   ```
3. Create a `.streamlit/secrets.toml` file in your project directory
4. Add your Openrouter API key to the secrets file:
   ```toml
   DEEPSEEK_API_KEY = 'your-api-key'
   ```
   Replace `your-api-key` with your actual Openrouter API key

### Running the Application

Run the application using Streamlit:
```bash
streamlit run main.py
```

The application will open in your default web browser.

## Usage

1. Type your message in the chat input box
2. Press Enter or click the send button
3. Watch as the AI generates both its reasoning process (visible in the expandable 🧠 section) and final response
4. Continue the conversation as needed

## Note

This application requires a valid Openrouter API key for local deployment. If you don't want to set up your own instance or don't have an API key, you can use the hosted version at [deepseek-cot-chat.streamlit.app](https://deepseek-cot-chat.streamlit.app).
