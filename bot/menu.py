from http import client
import discord  
import pandas as pd 
import hikari
import datetime
import time
import asyncio

df=pd.read_excel('/Users/apple/Desktop/Menu-Bot/bot/new_menu.xlsx') 

def processEXCEL(df):
    df.drop(df.index[0], inplace = True)
    days_index = []
    cnt= 0
    for i in df['Day']:
        if(not pd.isnull(i)):
            days_index.append(cnt)
        cnt+=1
    days_index.append(df.index[-1])

    menu = {}
    for day in range(len(days_index)-1):
        roju = []
        for meal in df.columns[1:]:
            puta= []
            for food in df[meal].iloc[days_index[day]:days_index[day+1]]:
                if(not pd.isnull(food)):
                    puta.append(food)
            roju.append(puta)
        menu[day] = roju
    return menu

days={
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

meals={
    "BREAKFAST": 0,
    "LUNCH": 1,
    "DINNER": 2,
    "SNACKS": 3,
}

TOKEN = "LICK"
menu = processEXCEL(df) 
DAY = datetime.datetime.today().strftime('%A')
bot = hikari.GatewayBot(TOKEN)
channel_id = "ASS"

@bot.listen()
async def on_message(event: hikari.MessageCreateEvent) -> None:
    """Listen for messages being created."""
    if not event.is_human:
        # Do not respond to bots or webhooks!
        return

    HOUR = (datetime.now().hour)*100 + (datetime.now().minute)

    if event.content == "!food":
        MEAL = "BREAKFAST"
        if HOUR < 951 and HOUR > 1450:
            MEAL = "LUNCH"
        elif HOUR < 1451 and HOUR > 1805:
            MEAL = "SNACKS"
        elif HOUR < 1806 and HOUR > 2359:
            MEAL = "DINNER"
        answer = "```\n"
        for item in menu[ days[DAY] ][meals[MEAL]]:
            answer = answer +  item+ "\n"
        answer+= "```"
        await event.message.respond(answer+"<@everyone>")

    elif(event.content[0] == "!"):
        MEAL = (event.content)[1:].upper()
        if(MEAL=="BREAKFAST" or MEAL=="LUNCH" or MEAL=="DINNER" or MEAL=="SNACKS"):
            answer = ""
            for item in menu[ days[DAY] ][meals[MEAL]]:
                answer = answer +  item+ "\n"
            await event.message.respond(answer+"<@everyone>")
        else:
            await event.message.respond("Did you ping me?! I don't understand the command tho.")

def MakeString(lis):
    ans  = ""
    for i in lis:
        ans += i + "\n"
    return ans

async def scheduler():
    app = hikari.RESTApp()
    while True:
        
        HOUR = (datetime.datetime.now().hour)*100 + (datetime.datetime.now().minute)
        if HOUR < 700 and HOUR > 630:
        # if HOUR < 700 and HOUR > 100: for testing 
            MEAL = "BREAKFAST"
            async with app.acquire(TOKEN, hikari.TokenType.BOT) as client:
                await client.create_message(channel_id, f'** {MEAL} **\n```  {MakeString(menu[ days[DAY] ][meals[MEAL]])} \n```\n <@everyone>' )
            time.sleep(1800)
        elif HOUR < 1230 and HOUR > 1200:
        # elif HOUR < 1230 and HOUR > 100: for testing
            MEAL = "LUNCH"
            async with app.acquire(TOKEN, hikari.TokenType.BOT) as client:
                await client.create_message(channel_id, f'** {MEAL} **\n```  {MakeString(menu[ days[DAY] ][meals[MEAL]])} ```\n <@everyone>' )
            time.sleep(1800)
        elif HOUR < 1600 and HOUR > 1530:
        # elif HOUR < 1600 and HOUR > 1530:
            MEAL = "SNACKS"
            async with app.acquire(TOKEN, hikari.TokenType.BOT) as client:
                await client.create_message(channel_id, f'** {MEAL} **\n```  {MakeString(menu[ days[DAY] ][meals[MEAL]])} ```\n <@everyone>' )
            time.sleep(1800)

        elif HOUR < 1900 and HOUR > 1830:
            MEAL = "DINNER"
            async with app.acquire(TOKEN, hikari.TokenType.BOT) as client:
                await client.create_message(channel_id, f'** {MEAL} **\n```  {MakeString(menu[ days[DAY] ][meals[MEAL]])} ```\n <@everyone>' )
            time.sleep(1800)
asyncio.run(scheduler())
bot.run()
