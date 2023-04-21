import discord
from discord.ext import commands
from discord.ui import *
from discord.commands import Option
import json
from discord.ext.commands import has_permissions
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import asyncio
from discord import Color



intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

with open('config.json', 'r') as file:
    config = json.load(file)
    token = config['Misc']['Token']


teal= Color.teal()
blue= Color.blue()
red= Color.red()
green= Color.green()
darkblue= Color.dark_blue()

@bot.event
async def on_ready():
    print(f"{Fore.BLUE}Successfully booted {bot.user.name}{Style.RESET_ALL}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}[+] Made by Xilo#1612{Style.RESET_ALL}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}[+] Please join discord.gg/xilo for more information{Style.RESET_ALL}")
    

@bot.slash_command(description="Changes the bots status.")
async def change_status(ctx, status: Option(str, "What do you want the bots status to say?", required=True)):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status}"))
    await ctx.response.send_message("Sucessfully changed bots status!", ephemeral=True)

@bot.slash_command(description="Sends a verification panel.")
async def verify_setup(ctx, channel: discord.TextChannel, verify_role: discord.Role, description: Option(str, "What do you want the verify embed to say", required=True), image: Option(str, "Links only", required=False)):
    class Verify(discord.ui.View):
        @discord.ui.button(label="Verify!", style= discord.ButtonStyle.success)
        async def button_callback(self, button, interaction):
            user = interaction.user
            await user.add_roles(verify_role)
            await interaction.response.send_message("You have been successfully been verified!", ephemeral=True)

    embed = discord.Embed(
        description=f"{description}",
        color=darkblue
    )
    embed.set_author(name="Verification System", icon_url=f"{image}")
    embed.set_footer(text="Verification System ©")
    embed.set_image(url=f"{image}")
    await channel.send(embed=embed, view=Verify())
    await ctx.response.send_message("Sent verification panel!", ephemeral=True)

@bot.slash_command(description="Bans user(s) from discord server")
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(
        description=f"Successfully banned {user.mention}!",
        color=darkblue
    )
    await user.ban(reason=None)

@bot.slash_command(description="Kicks user(s) from server")
async def kick(ctx, user: discord.Member):
    await user.kick()

bot.run(token)