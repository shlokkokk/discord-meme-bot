# 🤖 AskMeBot — The Free AI Assistant for Discord

AskMeBot is a powerful, lightweight, *completely free* AI Discord bot built using:
- Slash Commands (`/ask`, `/image`, `/joke`, `/meme`, etc.)
- OpenRouter
- Meme API
- Conversation memory (remembers last 5 messages)
- AI Image Generation

Perfect for fun servers, study groups, coding servers, or general use.

---

## 🚀 Features
- **/ask** — Ask anything, get smart AI replies  
- **/image** — Generate AI images from prompts  
- **/joke** — Get a short funny AI-generated joke  
- **/fact** — Random interesting facts  
- **/write** — Generate paragraphs on any topic  
- **/meme** — Sends a random meme from Reddit  
- **Conversation Memory** — Bot remembers last 5 interactions  
- **Fast Slash Commands** — Modern and clean UX  
- 100% **FREE**

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/discord-AskMeBot.git
cd discord-AskMeBot
```

Install dependencies:

```bash
pip install discord requests
```

---

## 🔧 Setup

1. Go to **Discord Developer Portal**
2. Create New Application → Add Bot
3. Turn ON:
   - Public Bot
   - Message Content (optional)
4. Get your **Bot Token**
5. Make a free OpenRouter account → get your **API key**

Place them in your `bot.py`:

```python
OPENROUTER_KEY = "your_openrouter_key"
client.run("your_discord_bot_token")
```

---

## ▶️ Running the Bot

```bash
python bot.py
```

---

## 📘 Slash Commands

AskMeBot supports:

| Command | Description |
|---------|-------------|
| `/ask question:<text>` | Ask AI anything |
| `/image prompt:<text>` | Generate an AI image |
| `/joke` | AI joke |
| `/fact` | Random fact |
| `/write topic:<text>` | Write a paragraph |
| `/meme` | Random meme |
| `/help` | Show all commands |

---

## 📜 License
MIT License — feel free to use and modify.

