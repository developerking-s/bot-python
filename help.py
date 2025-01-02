import discord
from discord.ext import commands

# Crie o bot com um prefixo de comando
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando para enviar uma mensagem com Embed
@bot.command()
async def embed(ctx):
    # Criar o embed
    embed = discord.Embed(
        title="Título do Embed",
        description="Aqui está a descrição do embed",
        color=discord.Color.blue()  # Você pode mudar a cor
    )
    embed.set_author(name="Nome do Autor", icon_url="URL_DA_IMAGEM")
    embed.set_thumbnail(url="URL_DA_IMAGEM_THUMBNAIL")
    embed.add_field(name="Campo 1", value="Este é um campo de exemplo", inline=False)
    embed.add_field(name="Campo 2", value="Outro campo", inline=False)
    embed.set_footer(text="Rodapé do Embed")

    # Enviar o embed
    await ctx.send(embed=embed)

# Rodar o bot com o token
bot.run('SEU_TOKEN_AQUI')
      
