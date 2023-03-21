# SET-UP
import random, math, hikari, lightbulb, os, dotenv, glob, lavaplayer
from dotenv import load_dotenv

load_dotenv()
my_token = os.getenv("TOKEN")
tenor_API = os.getenv("TENOR")
lava_pass = os.getenv("LAVAPLAYER")

bot = lightbulb.BotApp(
    token=my_token, 
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(1080686999482155058),
    prefix="!"
)

lavalink = lavaplayer.LavalinkClient(
    host="localhost",  
    port=2333,  
    password=lava_pass
)

pringles_prison = 1080686999482155058
court= 1080686999922540616

# START-UP CONFIRMATION
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Alive and ready to commit crimes")

# RESPOND TO EMPTY PINGS
ping_responses = ["hihi :3", "tf do u want", "hello", "the better pringle is here", "wha", "augh", "hrnrgh"]
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping(event):
    if not event.is_human:
        return
    me = bot.get_me()
    if me.id in event.message.user_mentions_ids:
        await event.message.respond(random.choice(ping_responses))

# RESPOND TO EMPTY PINGS TO PRINCE
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping_pring(event):
    if not event.is_human:
        return
    pring_id = 409170244201086976
    if pring_id in event.message.user_mentions_ids:
        await event.message.respond('why ping him when i exist')

# RESPOND TO MISCELLANEOUS CHAT INPUT
prompts = []
responses = []
with open('messages.txt','r') as textFile:
    file_content = textFile.readlines()
    for line in file_content:
        no_new_line = line.strip('\n')
        content = no_new_line.split(',')
        prompts.append(content[0])
        responses.append(content[1])
@bot.listen(hikari.GuildMessageCreateEvent)
async def send_message(event):
    if event.content in prompts:
        event_response = responses[prompts.index(event.content)]
        await event.message.respond(event_response)
    elif event.content == 'manta':
        options = ["<:mantaray:1081096190558482496>", "<:stingray:1081094162780274758>"]
        await event.message.respond(random.choice(options))
    elif event.content == 'ket':
        ye = glob.glob('meme-pics/*.gif')
        f = hikari.File(ye[0])
        await event.message.respond(f)
    else:
        pass

# SEND A RANDOM LEROY ON COMMAND
many_leroy = glob.glob('leroy-pics/*.jpg')
@bot.command
@lightbulb.command('leroy', 'he approaches')
@lightbulb.implements(lightbulb.SlashCommand)
async def leroy(ctx):
    f = hikari.File(random.choice(many_leroy))
    await ctx.respond(f)

# SEND A RANDOM WILLOW ON COMMAND
many_willow = glob.glob('willow-pics/*.jpg')
@bot.command
@lightbulb.command('willow', 'she approaches')
@lightbulb.implements(lightbulb.SlashCommand)
async def willow(ctx):
    f = hikari.File(random.choice(many_willow))
    await ctx.respond(f)

# SEND A CREATURE FACT ON COMMAND
creature_facts = []
with open('creatures.txt','r') as textFile:
    file_content = textFile.readlines()
    for line in file_content:
        no_new_line = line.strip('\n')
        creature_facts.append(no_new_line)
@bot.command
@lightbulb.command('creature', 'the more you know')
@lightbulb.implements(lightbulb.SlashCommand)
async def creature(ctx):
    await ctx.respond(random.choice(creature_facts))

# TERMINATE BOT OPERATIONS
@bot.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("terminate", "disconnext pringle from the world")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def terminate(ctx: lightbulb.Context) -> None:
    await ctx.respond("```Command recieved. Disconnecting bot.```")
    quit()

#  JOIN VOICE CHANNEL
@bot.command
@lightbulb.command('join', 'Makes bot join a voice channel')
@lightbulb.implements(lightbulb.PrefixCommand)
async def join(ctx):
    await bot.update_voice_state(pringles_prison, court)
    await ctx.respond("im in")

# LAUNCH BOT OPERATIONS
bot.run()
