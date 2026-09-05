# Gemini Terminal Chat

A multi-turn Python CLI chat program powered by Google's `gemini-3.6-flash` model.

## Features
- Persistent context across chat turns using the Gemini Chat interface.
- Secure API key management via environment variables (`python-dotenv`).

## Setup
1. Clone this repository.
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
    python AI.py
    ```