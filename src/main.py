import discord
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands
from json import loads
from json import load

f = open('env.json')
envs = load(f)
f.close()
TOKEN = envs['TOKEN']

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.command(
    name="store",
    description="Scans the entire server and stores everything in it."
)
async def store(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!", ephemeral=True)

@client.event
async def on_ready():
    await client.wait_until_ready()
    await tree.sync()
    print("Ready!")

client.run(TOKEN)
