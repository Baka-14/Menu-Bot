import os
import re
import hikari
import datetime

bot = hikari.GatewayBot('OTY2NTAzMDM1Mzk0MTk5NTgy.GcTrMF.f2tajLqbtZHU1-9pJSZINfHNNMB7zeXS24cpQk')
@bot.listen()
async def on_message(event: hikari.MessageCreateEvent) -> None:
    """Listen for messages being created."""
    if not event.is_human:
        # Do not respond to bots or webhooks!
        return

    HOUR = (datetime.now().hour)*100 + (datetime.now().minute)

    if event.content == "!food":
        if(HOUR < 2000 and HOUR > 2030):
            MEAL = "BREAKFAST"
        elif HOUR < 1230 and HOUR > 1200:
            MEAL = "LUNCH"
        elif HOUR < 1600 and HOUR > 1530:
            MEAL = "SNACKS"
        elif HOUR < 1900 and HOUR > 1830:
            MEAL = "DINNER"
        await event.message.respond(menu[ days[DAY] ][meals[MEAL]]+" @everyone")

    elif(event.content[0] == "!"):
        MEAL = (event.content)[1:].upper
        if(MEAL=="BREAKFAST" or MEAL=="LUNCH" or MEAL=="DINNER" or MEAL=="SNACKS"):
            await event.message.respond(menu[ days[DAY] ][meals[MEAL]]+" @everyone")
        else:
            await event.message.respond("Wrong command")
bot.run()
