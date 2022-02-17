import discord
from replit import db
from keepAlive import keep_alive
import random 

client = discord.Client()
db.clear() 
characters = ["astra", "breach", "brimstone", "chamber", "cypher", "jett", "kayo", "killjoy", "neon", "omen", "phoenix", "raze", "reyna", "sage", "skye", "sova", "viper", "yoru"]



@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("$hello"):
			
		await choose_character("sova.txt", message)
	
	#clear all values
	elif message.content.startswith("$clear"): 
		await db.clear()

	#chooses an absolutely random variable
	elif message.content.startswith("$random"):
		chooseRandomly = random.randint(0, 17)
		if (chooseRandomly < 0) or (chooseRandomly >= 18):
			await message.channel.send("Taylor did something wrong")
			return;
		await message.channel.send(characters[chooseRandomly])
		
		await message.channel.send(file=discord.File("tay.png"))
		return; 
	
async def choose_character(file, message):
	file = open(file, "r")
	for line in file: 
		await message.channel.send(line) 

keep_alive()
client.run("OTQyOTQxMjcwMjExNDU3MDk1.Ygr0fQ.yKcf1tyw4gV8hm14JhKJnoJaPfY")