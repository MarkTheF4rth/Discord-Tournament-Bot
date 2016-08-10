import discord, asyncio, sys, os, shelve, time
from commands import Main
client = discord.Client()

LOOP = asyncio.get_event_loop()

@client.event
async def on_message(message):
    if message.content.lstrip().startswith(MAIN.config['command_char']): #removes leading spaces and checks that the message begins with the command character
        MAIN.message_parser(message)
    
@client.event
async def on_message_edit(old, message):
    if message.content.lstrip().startswith(MAIN.config['command_char']):
        MAIN.message_parser(message, True)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

async def main_loop(main):
    await asyncio.sleep(1)
    await client.send_message(main.config['message'].channel, 'I have restarted')
    while not client.is_closed:
        main.message_handler()
        for message in main.out_messages:
            await client.send_message(message[0], message[1])
            main.out_messages.pop(0)
        await asyncio.sleep(1)

MAIN = Main(shelve)
if __name__ == '__main__':
    if not os.path.isfile('token.txt'):
        print('There is no token file present, make sure your file is named "token.txt"')
        sys.exit()

    token = open('token.txt').readlines()[0].strip()

    LOOP.create_task(main_loop(MAIN))
    LOOP.run_until_complete(client.run(token))
    LOOP.run_until_complete(client.connect())
