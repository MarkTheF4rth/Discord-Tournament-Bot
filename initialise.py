import asyncio, discord, shelve

'''
Initialises the bot to be ready to be run by main script
Additionally can be used to reconfigure config file
'''

def main():
    config = shelve.open('Configs/config-MASTER')
    config.clear()
    while True:
        char = input('What character will you be using as a command character?: ')
        ans = input('Are you sure you want to use "'+char+'" as your command character? (yes/y)')
        if ans.lower() == 'yes' or ans.lower() == 'y':
            config['command_char'] = char
            print(config['command_char'])
            break

if __name__ == '__main__':
    main()
