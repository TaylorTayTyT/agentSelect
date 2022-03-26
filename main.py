import discord
from replit import db
from keepAlive import keep_alive
import random 
import os

client = discord.Client()
db["teamwin"] = 0
db["teamloss"] = 0
db["welcome"] = 0
characters = ["astra", "breach", "brimstone", "chamber", "cypher", "jett", "kayo", "killjoy", "neon", "omen", "phoenix", "raze", "reyna", "sage", "skye", "sova", "viper", "yoru"]

#from geeksforgeeks website
def myAtoi(string):
    res = 0
  
    # Iterate through all characters of
    #  input string and update result
    for i in string:
        res = res * 10 + (int(i) - int('0'))
  
    return res

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("$hello"):
		await message.channel.send(message.author.name)

	#chooses an absolutely random variable
	elif message.content.startswith("$random"):
		chooseRandomly = random.randint(0, 17)
		if (chooseRandomly < 0) or (chooseRandomly >= 18):
			await message.channel.send("Taylor did something wrong")
			return
		await message.channel.send(characters[chooseRandomly])
		
		await send_photo(message, chooseRandomly)
		return

	elif (message.author.name == "MTN" or message.author.name == "taylornguyen") and (message.content.startswith("you're welcome") or message.content.startswith("youre welcome")) :
		f = open("ywcounter.txt", "r+")
		value = myAtoi(f.readline()) + 1
		f.seek(0)
		f.truncate(0)
		f.write(str(value))
		f.close()
		await message.channel.send("mtn has said youre welcome " + str(value) + " times")
	
async def send_photo(message, chooseRandomly):
	dir_name = "valorant agents/" + characters[chooseRandomly]
	list = os.listdir(dir_name) # dir is your directory path
	number_files = len(list)

	if number_files <= 0:
		await message.channel.send("someone hates " + characters[chooseRandomly] + " so there isn't a pic of them")
		return

	constraint = (random.randint(0, 100) % number_files) + 1
	pic_name = "valorant agents/" + characters[chooseRandomly] + "/" + str(constraint) + ".png"
	await message.channel.send(file=discord.File(pic_name))
	return

async def choose_character(file, message):
	file = open(file, "r")
	for line in file: 
		await message.channel.send(line) 

keep_alive()
client.run()
