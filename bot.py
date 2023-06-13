# SET-UP
import random, math, hikari, lightbulb, os, dotenv, glob
from dotenv import load_dotenv
load_dotenv()

my_token = os.getenv("TOKEN")
my_key = os.getenv("GPT")

# GENERAL SERVER INFO
pringles_prison = 1080686999922540615
court= 1080686999922540616
members = []
ids = []
with open('member-ids.txt','r') as textFile:
    file_content = textFile.readlines()
    for line in file_content:
        no_new_line = line.strip('\n')
        content = no_new_line.split(',')
        members.append(content[0])
        ids.append(int(content[1]))

# INITIALIZING
bot = lightbulb.BotApp(
    token=my_token, 
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(1080686999482155058),
    prefix="!"
)

# START-UP CONFIRMATION
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("BOT ONLINE")

# DISCONNECTION CONFIRMATION
@bot.listen(hikari.StoppedEvent)
async def bot_stopped(event):
    print("BOT OFFLINE")

# RESPOND TO EMPTY PINGS
ping_responses = ["<:huh:1109297758768214127>", "hihi :3", "tf do u want", "hello", "the better pringle is here", "wha", "augh", "hrnrgh"]
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping(event):
    if not event.is_human:
        return
    me = bot.get_me()
    if me.id in event.message.user_mentions_ids:
        await event.message.respond(random.choice(ping_responses))

# RESPOND TO EMPTY PINGS TO PRINCE
prin_pin = ['why ping him when i exist', 'yes?', 'huh', 'yippie']
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping_pring(event):
    if not event.is_human:
        return
    if 409170244201086976 in event.message.user_mentions_ids:
        await event.message.respond(random.choice(prin_pin))

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
    if not event.is_human:
        return
    if event.content in prompts:
        event_response = responses[prompts.index(event.content)]
        await event.message.respond(event_response)
    elif event.content == 'manta':
        options = ["<:mantaray:1081096190558482496>", "<:stingray:1081094162780274758>"]
        await event.message.respond(random.choice(options))
    else:
        return

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

# RESPOND TO YES/NO QUESTIONS
@bot.command
@lightbulb.option('question', 'what do you wanna ask',type=str)
@lightbulb.command('pringle', 'ask a yes/no question')
@lightbulb.implements(lightbulb.SlashCommand)
async def pringle(ctx):
    resp = ['ye', 'yes', 'no', 'naw', 'h', 'maybe', 'i can neither confirm nor deny', 'let me think,,,']
    await ctx.respond('> '+ ctx.options.question + '\n' + random.choice(resp))

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
@lightbulb.command("sleep", "knock him out")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def terminate(ctx: lightbulb.Context) -> None:
    await ctx.respond("I'm, eepy,,, <:passedout:1109295492132769842>")
    quit()

#  JOIN VOICE CHANNEL
@bot.command
@lightbulb.command('join', 'Makes bot join a voice channel')
@lightbulb.implements(lightbulb.SlashCommand)
async def join(ctx):
    await bot.update_voice_state(pringles_prison, court)
    await ctx.respond("im in")

# CUSTOM MEMBER GREETINGS
@bot.listen(hikari.GuildMessageCreateEvent)
async def greet(event):
    if not event.is_human:
        return
    if 'hi pri' in event.content:
        item_index = ids.index(event.author_id)
        sender = members[item_index]
        if sender == 'ica':
            await event.message.respond('ello loser /j')
        elif sender == 'manu':
            await event.message.respond('bonjour baguette')
        elif sender == 'reese':
            await event.message.respond('hihi rizz')
        elif sender == 'caf':
            await event.message.respond('Allo Cafcifer :3')
        elif sender == 'amber':
            await event.message.respond('hi ica')
        elif sender == 'aky':
            await event.message.respond('Hi Akyyyy :3')
        elif sender == 'prince':
            await event.message.respond('Oh, its you.')
        else:
            return
    else:
        return

# RECIEVE DMS TO BOT
@bot.listen(hikari.DMMessageCreateEvent)
async def recieve_text(event):
    if event.author_id in ids:
        num_index = ids.index(event.author_id)
        author = members[num_index]
        if not author == 'ica' or author == 'prince': 
            await bot.rest.create_message(1109594164938686634, author + ': ' + event.content)
            await bot.rest.create_message(1109604871885312020, author + ': ' + event.content)
        else:
            return
    else:
        return


# LAUNCH BOT OPERATIONS
bot.run()
