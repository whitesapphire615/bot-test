import discord
import os
import requests
from discord.ext import commands
from bot_logic import * 

with open("token.txt","r") as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    author_name = ctx.message.author.name
    await ctx.send(f'Hi{author_name}! I am a bot {bot.user}!')

@bot.command()
async def passwd(ctx):
    await ctx.send(gen_pass(6))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def math(ctx, a : int , b : int):
    result1 = a + b
    result2 = a - b
    result3 = a * b
    result4 = a / b
    await ctx.send(f'{a} + {b} = {result1}')
    await ctx.send(f'{a} - {b} = {result2}')
    await ctx.send(f'{a} * {b} = {result3}')
    await ctx.send(f'{a} / {b} = {result4}')

@bot.command()
async def mem(ctx):
    image_file = random.choice(os.listdir('images'))

    with open(f'images/{image_file}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_pokemon_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('pokemon')
async def pokemon(ctx):
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)


bot.run(token)


