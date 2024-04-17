from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Interaction
import discord
from discord.ext import commands
from responses import get_response_command



load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = commands.Bot(command_prefix="!" ,intents=intents)


@client.tree.command(name="ping", description="shows your ping")
async def ping(interaction: Interaction):
    latency = round(client.latency*1000)
    await interaction.response.send_message(f"Pong!... {latency}ms")


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('How did we get here ?')
        return
        
    try: #Bot Commands
        if user_message[0] == '!':
            response: str = get_response_command(user_message)
        
        await message.channel.send(response) 
    except Exception as e:
        print(e)





@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running !')
    await client.change_presence(activity=discord.Game(name="with fate !"))
    await client.tree.sync()


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)



def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()