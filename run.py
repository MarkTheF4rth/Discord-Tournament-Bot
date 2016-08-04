#!/home/mc/python3.5.1/bin/python3.5

import discord, asyncio, sys, os, shelve, time
client = discord.Client()

LOOP = asyncio.get_event_loop()

class Main:
    def __init__(self):
        self.config = shelve.open('Configs/config-MASTER')
        self.in_messages = []
        self.out_messages = []
   
    def message_handler(self):
        print('message handler is running')
        for message in self.in_messages:
            print('Processed message: ', message.content)

@client.event
async def on_message(message):
    print('Incoming message: ', message.content)
    if message.content.lstrip().startswith(MAIN.config['command_char']): #removes leading spaces and checks that the message begins with the command character
        MAIN.in_messages.append(message)
    
@client.event
async def on_message_edit(old, message):
    if message.content.lstrip().startswith(MAIN.config['command_char']):
        MAIN.in_messages.append(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

async def main_loop(main):
    print('loop running')
    while not client.is_closed:
        await asyncio.sleep(1)
        main.message_handler()

MAIN = Main()
if __name__ == '__main__':
    print('hello')
    if not os.path.isfile('token.txt'):
        print('There is no token file present, make sure your file is named "token.txt"')
        sys.exit()

    token = open('token.txt').readlines()[0].strip()

    LOOP.create_task(main_loop(MAIN))
    LOOP.run_until_complete(client.run(token))
    LOOP.run_until_complete(client.connect())
