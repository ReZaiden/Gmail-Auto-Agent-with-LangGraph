# 🤖 Gmail Auto Agent with LangGraph

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-1.0.4-brightgreen)
![Gradio](https://img.shields.io/badge/Gradio-6.0.2-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple)

An **AI-powered Gmail management agent** that automates email tasks using natural language commands.  
Powered by **LangGraph**, **LangChain**, **OpenAI**, and **Gradio** with a fully **modular multi-agent architecture**.

> ⚠️ **Note:** This project is built for development and testing.  
> For production, ensure secure API keys, OAuth credentials, HTTPS, and proper rate limiting.

## 🚀 Features

- 🧠 **LangGraph Agent System** with Gmail tool integration
- 📧 **Email Management** - Send, draft, search, read emails and threads
- 🔍 **Smart Search** - Natural language queries to find emails
- 💬 **Conversational Interface** - Chat-based email management via Gradio
- 🔧 **Gmail API Integration** - Full access to Gmail functionality
- 💾 **Memory Management** - Conversation state persistence across sessions
- 🛠️ **Tool Binding** - Automatic tool selection based on user intent
- 📚 **YAML-based Configuration** for agents and settings

## 🧠 Tech Stack

| Technology       | Version  | Description                        |
|------------------|----------|------------------------------------|
| **Python**       | 3.10+    | Core language                      |
| **LangGraph**    | 1.0.4    | Agent orchestration framework      |
| **LangChain**    | 1.1.0    | LLM framework and tools            |
| **OpenAI API**   | GPT-4o-mini | LLM for natural language understanding |
| **Gradio**       | 6.0.2    | Interactive chat UI framework      |
| **Gmail API**    | Latest   | Email service integration          |

## ⚙️ Prerequisites

Before running the project, ensure you have:

- 🐍 **Python 3.10+**
- 📦 **pip** or **uv** (recommended)
- 🌐 **Git**
- 🔑 **OpenAI API key**
- 📧 **Gmail API credentials** (OAuth 2.0)

## 🛠️ Installation

```bash
git clone https://github.com/ReZaiden/Gmail-Auto-Agent-with-LangGraph.git
cd Gmail-Auto-Agent-with-LangGraph
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or using **uv** (faster):

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

## 🗝️ Configuration

### 1. Create .env file

Rename `.env.sample` file to `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
```

### 2. Setup Gmail API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable **Gmail API**
4. Create **OAuth 2.0 credentials** (Desktop application)
5. Download the credentials and save as `config/credentials.json`
6. On first run, you'll be prompted to authorize the application
7. The authorization token will be saved to `config/token.json`

## ▶️ Run the Project

### Using Gradio UI:

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python app.py
```

The Gradio interface will launch and provide a URL (typically http://localhost:7860/)

## 📡 How It Works

1. **User provides instructions** → Describe what email task you need (e.g., "Find all emails from john@example.com")
2. **Gmail Agent analyzes** → The LangGraph agent processes your request and determines required tools
3. **Tools execution** → Agent automatically uses Gmail tools:
   - **GmailSendMessage** - Send emails
   - **GmailCreateDraft** - Create draft emails
   - **GmailSearch** - Search emails with queries
   - **GmailGetMessage** - Retrieve specific messages
   - **GmailGetThread** - Get email threads
4. **Response generation** → Agent provides natural language responses with results
5. **Memory persistence** → Conversation state is maintained across interactions

## 🧩 Project Structure

```plaintext
.
├── app.py                  # Gradio web interface (main entry point)
├── main.py                 # CLI entry point (placeholder for future use)
├── requirements.txt        # Python dependencies
├── .env.sample            # Environment variables template
├── .gitignore             # Git ignore rules
├── config/
│   ├── agents.yaml        # Agent configurations
│   ├── config.yaml        # Gmail settings
│   ├── credentials.json   # Gmail OAuth credentials (not tracked)
│   └── token.json         # Gmail OAuth token (not tracked)
├── graph/
│   ├── __init__.py
│   ├── setup.py           # LangGraph agent setup
│   └── state.py           # State schema definition
├── tools/
│   ├── __init__.py
│   └── gmail_tools.py     # Gmail API tool integration
├── utils/
│   ├── __init__.py
│   ├── config.py          # Configuration loader
│   └── logger.py          # Logging setup
└── tests/
    ├── gmail_tools_test.py
    ├── config_test.py
    └── graph_test.py
```

## 🤖 Agent Architecture

| Component          | Description                                    |
|--------------------|------------------------------------------------|
| **Gmail Agent**    | Main agent with tool binding and reasoning     |
| **Tool Node**      | Executes Gmail API tools                       |
| **Memory Saver**   | Persists conversation state                    |
| **State Graph**    | Manages agent workflow and transitions         |

### Agent Flow:

```
User Input → Gmail Agent → Tool Selection → Tool Execution → Response → User
                ↑                                                        ↓
                └────────────── Memory Persistence ─────────────────────┘
```

## 🔧 Available Gmail Tools

- **GmailSendMessage** - Send emails to recipients
- **GmailCreateDraft** - Create email drafts for later
- **GmailSearch** - Search emails with advanced queries
- **GmailGetMessage** - Retrieve specific email messages
- **GmailGetThread** - Get entire email threads/conversations

## 🔒 Security Notes

- Keep API keys inside `.env`
- Never commit `.env`, `credentials.json`, or `token.json` to version control
- OAuth tokens are stored locally in `config/token.json`
- Use environment variables for sensitive data
- Enable 2FA on your Google account
- Regularly review OAuth app permissions

## 💡 Example Use Cases

- "Search for all emails from my boss last week"
- "Send an email to john@example.com with subject 'Meeting Reminder'"
- "Create a draft reply to the latest email from customer support"
- "Show me all unread emails from today"
- "Get the email thread about the project proposal"

## 🧪 Testing

Run tests using pytest:

```bash
pytest tests/
```

> **Note:** Gmail tools tests require valid OAuth credentials and internet connectivity.

## 🛠️ Configuration Files

### agents.yaml
Defines the Gmail agent's behavior:
- Instructions for the agent
- Model selection (GPT-4o-mini)
- Tool capabilities

### config.yaml
Gmail API settings:
- Credentials file path
- Token file path

## 💡 Future Improvements

- [ ] Add email filtering and labeling automation
- [ ] Support for email attachments handling
- [ ] Scheduled email sending
- [ ] Email analytics and reporting
- [ ] Multi-account support
- [ ] Enhanced conversation memory with vector storage
- [ ] Support for other email providers (Outlook, etc.)
- [ ] Email templates and automation workflows

## 🐛 Troubleshooting

### "OPENAI_API_KEY not set" error
- Ensure `.env` file exists and contains valid API key
- Check that python-dotenv is loading the file correctly

### Gmail authentication issues
- Delete `config/token.json` and re-authenticate
- Verify `config/credentials.json` is valid
- Check Gmail API is enabled in Google Cloud Console

### Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Activate virtual environment before running

## 🧑‍💻 Author

**Developed by:** ReZaiden  
💼 **GitHub:** [@ReZaiden](https://github.com/ReZaiden)  
📧 **Contact:** rezaidensalmani@gmail.com

## 📄 License

This project is open source and available for educational and personal use.

---

⭐ **If you find this project helpful, please give it a star on GitHub!**