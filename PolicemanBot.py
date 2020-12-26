import discord
import random as r
intents = discord.Intents.default()
intents.members = True

rules = ["rule 0: no bad words here!", "rule 1: no stigmatization here!", "rule 2: no ad-hominem here!", 
		"rule 3: no insult here", "rule 4: all the previous rules are valid and subject to adjustements!"]

insults_words = ["fuck","dick","f***","d***","pussy","p****","I don't give a"]

bad_words = ["you dumb", "you mean", "you a stupid guy", "you are a stupid guy", "you stupid guy"]

encouragement_word = ["Don't worry and trust God","Everything will be allright just believe in Him", "Hang there", "you can do it, persevere!"]

sad_words = ["I'm so sad", "I'm sick", "It's too hard", "It's too difficult"]

Client = discord.Client()


@Client.event
async def on_ready():
	print("Policeman is ready")
	

@Client.event
async def on_message(message):
	if message.author == Client.user:
		return
	msg = message.content
		
	if any(element in msg for element in insults_words):
		await message.add_reaction("😡")
		await message.channel.send(rules[3] + "\nrules must be respected")
	if any(element in msg.lower() for element in bad_words):
		await message.channel.send(rules[0])
	if msg.startswith("list"):
		for user in Client.users:
			await message.channel.send(str(user.name))
	if msg.startswith("God is good"):
		await ctx.send("❤️")
	if msg.startswith("God is bad"):
		await ctx.send("We don't agree with you 😡")
	if any(element in msg.lower() for element in sad_words):
		await ctx.send(r.choice(encouragement_word))
	



Client.run("NzkxMzc5NzE1ODcxOTk3OTgz.X-OTyw.rrGehZ4okivUDWZxJj7B7pQMM7Q")