import discord
from discord.ext import commands

# Crie o bot com um prefixo de comando
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando para mencionar o usuário
@bot.command()
async def mention(ctx):
    # Menciona o usuário que enviou o comando
    await ctx.send(f'Olá, {ctx.author.mention}! Como você está?')

# Rodar o bot com o token
bot.run('SEU_TOKEN_AQUI')
