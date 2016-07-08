#!/home/mc/python3.5.1/bin/python3.5

import discord, asyncio
client = discord.Client()

@client.event
async def on_message(message):
    print('received message')
    print(type(message.server))
    if message.server.name == 'Test' and message.author.name != 'Tournament-Bot':
        print('sending message')
        await client.send_message(message.channel, 'I live!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run('MTg5NDgzNjU5NzkzOTI0MDk2.CmFpPA.wAM7k97fqlEI5kb0OPDwj4j8pOE')
client.connect()
