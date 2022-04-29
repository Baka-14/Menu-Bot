
import hikari
import pandas as pd
import lightbulb
import os
import datetime

#gets the current date and time and formats them into string
# time_hour=datetime.now()
# day=time_hour.strftime("%A")
# time=datetime.isoformat(time_hour)[11:19] 
now = datetime.now()
current_time = now.strftime("%H") 
#print("Current Time =", current_time)
Day=datetime.today().strftime('%A')

df=pd.read_excel('Menu.xlsx')
#print(df.head())
File = open('/Users/apple/Desktop/code/Baka Bot/bot/token','r')
T=File.readline()
#print (T)

baka=lightbulb.BotApp(
    token= T,
#token=Token,
#only for the menu server makes the bot faster 
default_enabled_guilds=(952510854899834930)
)

@baka.listen(hikari.GuildMessageCreateEvent)
#function header 
async def print_message(event):
    #function used to just print the message
    #  whatever typed on discord 

    print(event.content)

#event to tell me the bots running 
@baka.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Baka is alive , up and running")

@baka.command
@lightbulb.command('bakayaro','Konoyaro')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Konoyaro')

#making a subgroup of commands 
@baka.command
@lightbulb.command('akastuki','this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def itachi(ctx):
    pass #Pass implies the function does nothing 

#this is a sub command of the group command akastuki
@itachi.child
@lightbulb.command('itachi','do you know what mangekyo sharingan can do?')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sub_command(ctx):
    await ctx.respond('Amaterasu')

@baka.command
@lightbulb.option('num2','this is first number',type=int)
@lightbulb.option('num1','this is second number',type=int)
#taking in 2 numbers to add and the options must be above thelight bulb command 
#and underneath the baka.command 
@lightbulb.command('add','adds two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

#for pinging everyone so that they can get the notification'''
@baka.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if event.content.startswith("menu?"):
        await event.message.respond("https://cdn.discordapp.com/attachments/952512991717384303/968954395200987206/full_menu.png")
    
    time_hour=datetime.now()
    day=time_hour.strftime("%A")
    time=datetime.isoformat(time_hour)[11:19]
    
    while True:
      a=datetime.now()  
      actual_time=datetime.isoformat(a)[11:19]

      if actual_time==bk:
          

        
#time. sleep at that time => calculate how long it sleeps wakes up and 
#sends a message 
#iterate using iloc 
#taking in the menu every week 

    
baka.run() 
