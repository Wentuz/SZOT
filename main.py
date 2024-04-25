from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from responses import get_response_command
from discord import Intents, Client, Message, Interaction
from roll_dice import get_roll
from truth_or_dare import get_truth_or_dare
from art_prompts import get_art_prompt



load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = commands.Bot(command_prefix="!" ,intents=intents)


#====================================================================================
#==================================================================================== COMMANDS
#====================================================================================


@client.tree.command(name="r", description="rolls a dice")
async def dice(interaction: Interaction, num_dice: int, value_dice: int):
    response = get_roll(num_dice, value_dice)
    await interaction.response.send_message(response)

@client.tree.command(name="pings", description="shows your ping")
async def ping(interaction: Interaction):
    latency = round(client.latency*1000)
    await interaction.response.send_message(f"Pong!... {latency}ms!")

@client.tree.command(name="truth", description="or dare ?")
async def ping(interaction: Interaction):
    await interaction.response.send_message(get_truth_or_dare(0))

@client.tree.command(name="dare", description="or truth ?")
async def ping(interaction: Interaction):
    await interaction.response.send_message(get_truth_or_dare(1))

@client.tree.command(name="art_promtp", description="makes u autistic")
async def dice(interaction: Interaction, appearance: int, emotion: int, action: int):
    response = get_art_prompt(appearance, emotion, action)
    await interaction.response.send_message(response)

@client.tree.command(name="testing", description="used for tests by devs")
async def testComm(interaction: Interaction):
    response = "test woo hoo !"    
    await interaction.response.send_message(response)


#====================================================================================
#==================================================================================== TEST CASES
#====================================================================================







#====================================================================================
#==================================================================================== CHAT
#====================================================================================


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('How did we get here ?')
        return
        
    try: #Bot Commands
        #if client.user.mentioned_in(message):
        #    response: str = "Sup kitten ᓚᘏᗢ ?"
        if client.user.mentioned_in(message):
            response: str = get_response_command(user_message)
        
        await message.channel.send(response) 
    except Exception as e:
        print(e)


#====================================================================================
#==================================================================================== EVENT LISTENERS
#====================================================================================


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