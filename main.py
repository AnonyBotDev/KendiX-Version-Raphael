import discord
from discord.ext import commands
import json
import pyfiglet
import os
import requests
import asyncio
from colorama import Fore

with open('./config.json') as f:
	prefix = json.load(f)


préfixes = prefix.get("prefixe")

bot = commands.Bot(command_prefix=préfixes, description="Le selfbot de l'AnonyBot!", self_bot=True)
bot.remove_command("help")
version = 0.2


@bot.event
async def on_ready():
	print(Fore.GREEN + "Lancement Du SelfBot...")
	await asyncio.sleep(2)
	print(Fore.GREEN + "Récupération du fichier Config.json...")
	await asyncio.sleep(2)
	print(Fore.GREEN + "Connexion a Discord")
	await asyncio.sleep(2)
	print(Fore.GREEN + "Changement du statut...")
	await asyncio.sleep(2)
	os.system("clear")
	await asyncio.sleep(3)
	text = pyfiglet.figlet_format(f"KendiX SelfBot \n\n\n\n\n")
	print(text)
	print(Fore.CYAN + "AVERTISSEMENT: Sachez que nous ne sommes pas responsables de vos actions, veuiller utiliser se selfbot avec modération.")
	print(Fore.WHITE + f"Connecté sur: {bot.user} \n Status chargé, selfbot prêt!")
	with open('./config.json') as f:
		stats = json.load(f)
		
	status = stats.get("status")
	await bot.change_presence(activity=discord.Game(name=status))
	
	
@bot.command()
async def ascii(ctx,*,args):
	await ctx.message.delete()
	texti = pyfiglet.figlet_format(args)
	await ctx.send(f"```{texti}```")
	
	
@bot.command()
async def hypesquad(ctx,house):
	await ctx.message.delete()
	request = requests.session()
	headers = {
			'Authorization': token,
			'Content-Type': 'application/json'
	}
	
	if house == "bravery":
		payload = {"house_id": "1"}
	elif house == "brilliance":
		payload = {"house_id": "2"}
	elif house == "balance":
		payload = {"house_id": "3"}
		
	try:
		request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers,json=payload)
		await ctx.send("J'ai changé ta hypesquad avec succès!")
	except:
		await ctx.send("Une erreur est survenue, merci de vérifier l'erreur dans ton terminal")
		print(Fore.RED + "[ERREUR] | Je n'ai pas pu changé ta hypesquad,cela arrive souvent quand tu es déjà dans cette maison de la hypesquad.")


@hypesquad.error
async def h_er(ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			await ctx.send("Tu n'as pas implenté le nom de la hypesquad !")
		

@bot.command()
async def customembed(ctx,title,*,description):
	await ctx.message.delete()
	embed = discord.Embed(title=title,description=description)
	await ctx.send(embed=embed)
	

@bot.command()
async def destroy(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Destruction du serveur....", delete_after=3)
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except:
                pass
        for user in list(ctx.guild.members):
            try:
               await user.ban()
            except:
                pass  
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass
        for _i in range(250):
            await ctx.guild.create_role(name=f"Raid by KendiX")
            await ctx.guild.create_text_channel(name="Raid By KendiX")
		
@bot.command()
async def spam(ctx, amount:int=None, *, message: str=None):

        await ctx.message.delete()

        for each in range (0, amount):

            await ctx.send(f"{message}")



with open('./config.json') as f:
	config = json.load(f)


token = config.get("token")
bot.run(token, bot=False)
