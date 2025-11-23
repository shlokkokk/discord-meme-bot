import discord
from discord import app_commands
import requests
from collections import deque   # for memory


OPENROUTER_KEY = "YOUR_OPENROUTER_KEY_HERE"
API_URL = "https://openrouter.ai/api/v1/chat/completions"


conversation_history = deque(maxlen=5)


def ask_ai(prompt):
    # Add user message to memory
    conversation_history.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    # Combine memory into messages list
    data = {
        "model": "qwen/qwen-2.5-7b-instruct",
        "messages": list(conversation_history)
    }

    res = requests.post(API_URL, json=data, headers=headers).json()

    try:
        reply = res["choices"][0]["message"]["content"]

        # Save bot reply to memory
        conversation_history.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("OpenRouter error:", res)
        return "AI is confused rn 😭"


def get_meme():
    try:
        response = requests.get("https://meme-api.com/gimme")
        return response.json().get("url", "Meme API error 😭")
    except:
        return "Meme API crashed 😭"


def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "luma-media/lumacream-xl",   # free model available on OpenRouter
        "prompt": prompt
    }

    res = requests.post("https://openrouter.ai/api/v1/images", json=data, headers=headers).json()

    try:
        return res["data"][0]["url"]
    except:
        print("Image Gen Error:", res)
        return "Couldn't generate the image 😭"


class AskMeBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")


client = AskMeBot()


@client.tree.command(name="help", description="Show all commands")
async def help_cmd(interaction: discord.Interaction):
    help_text = (
        "**🤖 AskMeBot — Your Discord AI Assistant**\n\n"
        "**Commands:**\n"
        "• `/ask question:<text>` — Ask the AI anything\n"
        "• `/image prompt:<text>` — Generate an AI image\n"
        "• `/joke` — Funny joke\n"
        "• `/fact` — Random cool fact\n"
        "• `/write topic:<text>` — Generate a paragraph\n"
        "• `/meme` — Sends a random meme\n"
        "• `/help` — Show this menu\n"
    )
    await interaction.response.send_message(help_text)


@client.tree.command(name="ask", description="Ask AskMeBot any question")
async def ask_cmd(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    reply = ask_ai(question)
    await interaction.followup.send(reply)


@client.tree.command(name="image", description="Generate an AI image")
async def image_cmd(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    img_url = generate_image(prompt)
    await interaction.followup.send(img_url)


@client.tree.command(name="joke", description="Get a funny AI joke")
async def joke_cmd(interaction: discord.Interaction):
    await interaction.response.defer()
    reply = ask_ai("Tell me a short funny joke.")
    await interaction.followup.send(reply)


@client.tree.command(name="fact", description="Get a random cool fact")
async def fact_cmd(interaction: discord.Interaction):
    await interaction.response.defer()
    reply = ask_ai("Give me a random cool fact.")
    await interaction.followup.send(reply)


@client.tree.command(name="write", description="Write a paragraph about any topic")
async def write_cmd(interaction: discord.Interaction, topic: str):
    await interaction.response.defer()
    reply = ask_ai(f"Write a paragraph about {topic}.")
    await interaction.followup.send(reply)


@client.tree.command(name="meme", description="Send a random meme")
async def meme_cmd(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(get_meme())


client.run("YOUR_DISCORD_BOT_TOKEN_HERE")   
