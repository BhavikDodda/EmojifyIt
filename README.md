# Features
- Automatically appends relevant emojis to the end of a sentence.
- Powered by the Groq API for intelligent emoji suggestions.
- Lightweight and easy to integrate into Python projects.
- Supports customization for different use cases (e.g., casual conversations, professional settings).

## Ongoing
- Automating responses based on your context/use case.

# Prerequisites
- Python
- AutoHotkey
- A Groq API key (https://console.groq.com/keys)

# Setup
1. Clone the repository
   ```cmd
     git clone https://github.com/BhavikDodda/EmojifyIt.git
     cd EmojiAppender
   ```
2. Install the required dependencies
   ```cmd
     pip install groq python-dotenv
   ```
3. Setup your Groq API key. Create a .env file in the root directory of the project and add your Groq API key to the .env file
   ```cmd
     GROQ_API_KEY=your_api_key_here
   ```
4. Install AutoHotkey if not already installed. Run the emojiadder.ahk script.

# Usage
- You can run the py script via CLI
  ```cmd
    python emoji_wrapper.py "[Provide a sentence]"
  ```
- The project integrates with AutoHotkey (AHK) to allow quick access via a hotkey. By default, pressing Numpad 4 opens a menu. Selecting "Emoji Appender" will utilize the Python script to append emojis to your text.

# Other methods
Have tried to integrate the AHK script with a Local LLM but the response time of that is greater than implementing with an API.