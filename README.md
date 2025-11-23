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

Clone the repository:

```bash
git clone https://github.com/yourusername/discord-AskMeBot.git
cd discord-AskMeBot
```

Install required packages:

```bash
pip install -r requirements.txt
```

---


## 🔧 Setup

### 1️⃣ Create a `.env` file  
In the project folder, create a file named **.env** and add:

```
OPENROUTER_KEY=your_openrouter_key
DISCORD_TOKEN=your_discord_bot_token
```

---

### 2️⃣ Configure Discord Bot
1. Open **Discord Developer Portal**  
2. Create New Application → Add Bot  
3. Enable:
   - **Public Bot**
   - **Message Content Intent** (optional but safe)  
4. Copy your **Bot Token**  

---

### 3️⃣ OpenRouter Setup
1. Go to **https://openrouter.ai/**
2. Create a free account  
3. Generate an API key  
4. Paste it into `.env`  

---

## ▶️ Running the Bot

### (Optional) Activate your virtual environment:
```bash
.\.venv\Scripts\activate
```

Start the bot:
```bash
python bot.py
```

If everything is correct, you’ll see:

```
Logged in as AskMeBot!
```

Slash commands will automatically appear in your Discord server.

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

