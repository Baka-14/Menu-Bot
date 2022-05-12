
# # import hikari
# import pandas as pd 
# import numpy as np
# from time import sleep 
# # import lightbulb
# import os
# import datetime 
# import openpyxl 
# # from apscheduler.schedulers.asyncio import AsyncIOScheduler
# # from apscheduler.triggers.cron import CronTrigger
# # from discord.ext import commands
# import discord

# df=pd.read_excel('/Users/apple/Desktop/Menu-Bot/bot/Menu.xlsx') 

# def processEXCEL(df):
#     df.drop(df.index[0], inplace = True)
#     days_index = []
#     cnt= 0
#     for i in df['Day']:
#         if(not pd.isnull(i)):
#             days_index.append(cnt)
#         cnt+=1
#     days_index.append(df.index[-1])

#     menu = {}
#     for day in range(len(days_index)-1):
#         roju = []
#         for meal in df.columns[1:]:
#             puta= []
#             for food in df[meal].iloc[days_index[day]:days_index[day+1]]:
#                 if(not pd.isnull(food)):
#                     puta.append(food)
#             roju.append(puta)
#         menu[day] = roju
#     return menu

# days={
#     "Monday": 0,
#     "Tuesday": 1,
#     "Wednesday": 2,
#     "Thursday": 3,
#     "Friday": 4,
#     "Saturday": 5,
#     "Sunday": 6,
# }
# meals={
#     "BREAKFAST": 0,
#     "LUNCH": 1,
#     "DINNER": 2,
#     "SNACKS": 3,
# }

# menu = processEXCEL(df)

# File = open('/Users/apple/Desktop/code/Baka Bot/bot/token','r')
# T=File.readline()


# baka=lightbulb.BotApp(
#     token= T,
# # only for the menu server makes the bot faster 
# default_enabled_guilds=(952510854899834930)
# )

# # @baka.listen(hikari.GuildMessageCreateEvent)
# # async def print_message(event):
# #        function used to just print the message
# #      whatever typed on discord 
# #     print(event.content)

# #event to tell me the bots running 
# @baka.listen(hikari.StartedEvent)
# async def bot_started(event):
#     print("Baka is alive , up and running")

# # @baka.command
# # @lightbulb.command('bakayaro','Konoyaro')
# # @lightbulb.implements(lightbulb.SlashCommand)
# # async def ping(ctx):
# #     await ctx.respond('Konoyaro')

# #for pinging everyone so that they can get the notification
# # @baka.listen()
# # async def ping(event: hikari.GuildMessageCreateEvent) -> None:
# #     if event.is_bot or not event.content:
# #         return

# #     if event.content.startswith("menu?"):
# #         await event.message.respond("https://cdn.discordapp.com/attachments/952512991717384303/968954395200987206/full_menu.png")



# # async def func():
# #     c = bot.get_channel(channel_id)
# #     await c.send("s!t")

# # @bot.event
# # async def on_ready():
# #     print("Ready")

# #     #initializing scheduler
# #     scheduler = AsyncIOScheduler()

# #     #sends "s!t" to the channel when time hits 10/20/30/40/50/60 seconds, like 12:04:20 PM
# #     scheduler.add_job(func, CronTrigger(second="0, 10, 20, 30, 40, 50")) 

# #     #starting the scheduler
# #     scheduler.start()

           
# DAY = datetime.datetime.today().strftime('%A')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# @bot.event
# async def on_ready():
#     while True:

#         sleep(1800)
#         HOUR = (datetime.datetime.now().hour)*100 + (datetime.datetime.now().minute)

#         if HOUR < 700 and HOUR > 630:
#             MEAL = "BREAKFAST"
#             print( menu[ days[DAY] ][meals[MEAL]]"@everyone" )
#         elif HOUR < 1230 and HOUR > 1200:
#             MEAL = "LUNCH"
#             print( menu[ days[DAY] ][meals[MEAL]] "@everyone")
    
#         elif HOUR < 1600 and HOUR > 1530:
#             MEAL = "SNACKS"
#             print( menu[ days[DAY] ][meals[MEAL]] "@everyone")
    
#         elif HOUR < 1900 and HOUR > 1830:
#             MEAL = "DINNER"
#             print({menu[ days[DAY] ]}{[meals[MEAL]]} "@everyone" ) 
    
    


# baka.run("T")