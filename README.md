# Gemini Interactive Chat (Streamlit)

A real-time, multi-turn AI chat application built with Streamlit and powered by Google's `gemini-3.6-flash` model using token-by-token streaming.

## Features

* Multi-turn conversational memory powered by Google GenAI.
* Real-time response streaming for near-zero perceived latency.
* Clean web UI built with Streamlit chat components.
* Environment-based API key handling for secure configuration.

## Setup
1. Clone this repository:
    ```bash
   git clone [https://github.com/Vasanth-Nataraj/gemini-terminal-chat.git](https://github.com/Vasanth-Nataraj/gemini-terminal-chat.git)
   cd gemini-terminal-chat
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv my_env
   my_env\Scripts\activate
    ```
3. Install dependancies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in the root directory:
    ```bash
    GEMINI_API_KEY=your_actual_key_here
    ```
5. Run the application:
    ```bash
    streamlit run AI.py
    ```