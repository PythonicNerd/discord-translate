import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from googletrans import Translator
import random


client = Bot(description="Translates stuff badly", command_prefix="!")

def translate_s(sentence):
    t = Translator()

    languages  = ['japanese','afrikaans','arabic','chinese','irish','french','italian','zulu','swahili','turkish','korean','french','icelandic','hindi','greek','german','dutch','czech','russian','hawaiian','polish','thai','spanish','yiddish']


    text = sentence
    copy = t.translate(text, dest='english')


    for i in range(30):
        try:
            print(str(i) + ')')
            copy = t.translate(copy.text, dest=random.choice(languages))
            print(copy.text)
            print('Language: ' + str(copy.src))
            print('In english: ' + t.translate(copy.text, dest='english').text)
            print('\n')
            print('---------------------------------------------------------------')

        except:
            pass



    return t.translate(copy.text, dest='en').text


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')


@client.command()
async def translate(sentence):
    print("SENTENCE TO TRANSLATE: " + str(sentence))
    await client.say("Translating your sentence! This will take around 15 to 45 seconds.")
    translated = translate_s(sentence)
    await client.say("Your sentence is: " + str(translated))



#testing-token: MzY0MjMwNDk0MDYzNDI3NTg3.DO4xCg.zuNF6qx1UTbyXN455obiFnitKEI
#real-token: MzgwNDUxNjc5NzIxNjE5NDYw.DO4ywA.vlj6dd0iceRF3gTWZ5kuZ9Cr8SQ

client.run('MzgwNDUxNjc5NzIxNjE5NDYw.DO4ywA.vlj6dd0iceRF3gTWZ5kuZ9Cr8SQ')
