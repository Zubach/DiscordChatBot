from asyncio.windows_events import NULL
import discord
import json
from discord.ext import commands
from discord.utils import get
from config import settings
from admin import Admin
from admin import AdminEncoder


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix = settings['prefix'])

admins_list = []

admins_list = json.load(open("admin_list.json"))

def admin_checker(name, level):

    for admin in admins_list:
        if admin["name"] == name and admin["level"]>=level:
            return True


@bot.command()
async def hello(ctx):
    author = ctx.message.author 

    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def makeadmin(ctx,name,admin_level):
    if admin_checker(ctx.message.author.mention,5):
        new_admin = Admin(name,int(admin_level))
        admins_list.append(new_admin)

        with open('admin_list.json', 'w') as jsonFile:
            json.dump(admins_list, jsonFile, cls=AdminEncoder)
            jsonFile.close()

        await ctx.send(f'Welcome to new chat admin {name}')
    else:
        await ctx.send('Fuck you leatherman')
@bot.command()
async def adminslist(ctx):
    str = ""
    for admin in admins_list:
        
        str = str + f'Name: {admin["name"]}, Level: {admin["level"]}' + '\n'

    await ctx.send("Admin List:\n" + str)

@bot.command()
async def mute(ctx,name):
    
    
    if admin_checker(ctx.message.author.mention,1):
        members = bot.get_all_members()
        role_ = NULL
        for role in ctx.guild.roles:
            if role.name == "магу писать":
                role_ = role
                break               
        for member in members:
        
            if( ("<@!" + str(member.id) + ">") == name):            
                await member.remove_roles(role_)
                break
        await ctx.send(f'{name} muted')
    else:
        await ctx.send('Fuck you leatherman')

@bot.command()
async def unmute(ctx,name):
    if admin_checker(ctx.message.author.mention,1):
        members = bot.get_all_members()
        role_ = NULL
        for role in ctx.guild.roles:
            if role.name == "магу писать":
                role_ = role
                break               
        for member in members:
       
            if( ("<@!" + str(member.id) + ">") == name):            
                await member.add_roles(role_)
                break    
        await ctx.send(f'{name} unmuted')
    else:
        await ctx.send('Fuck you leatherman')

@bot.command()
async def voice_mute(ctx,name):
    if admin_checker(ctx.message.author.mention,2):
        members = bot.get_all_members()
        role_ = NULL
        for role in ctx.guild.roles:
            if role.name == "✌Магу піздіть✌":
                role_ = role
                break               
        for member in members:
        
            if( ("<@!" + str(member.id) + ">") == name):            
                await member.remove_roles(role_)
                break
        await ctx.send(f'{name} muted') 
    else:
        await ctx.send('Fuck you leatherman')

@bot.command()
async def voice_unmute(ctx,name):
    if admin_checker(ctx.message.author.mention,2):
        members = bot.get_all_members()
        role_ = NULL
        for role in ctx.guild.roles:
            if role.name == "✌Магу піздіть✌":
                role_ = role
                break               
        for member in members:
       
            if( ("<@!" + str(member.id) + ">") == name):            
                await member.add_roles(role_)
                break    
        await ctx.send(f'{name} unmuted')
    else:
        await ctx.send('Fuck you leatherman')

bot.run(settings['token'])

