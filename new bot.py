import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("봇만드는중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
     if message.content.startswith("!인증"):
         author = message.guild.get_member(int(message.content[4:22]))
         role = discord.utils.get(message.guild.roles, name="User")
         await author .add_roles(role)
         await message.channel.send(f'{message.author.mention} 완료되었습니다')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
