# SET-UP
import random, math, hikari, lightbulb, os, dotenv, glob, openai
from dotenv import load_dotenv
load_dotenv()

my_token = os.getenv("TOKEN")
my_key = os.getenv("GPT2")

openai.api_key = my_key

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

# GENERATE RESPONSE FUNCTION FOR AI 
def generate_response(message):
    prompt = f"{message.content}\nAI Response:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.content}",
        max_tokens=100,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# INITIALIZING
bot = lightbulb.BotApp(
    token=my_token, 
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(1080686999482155058,1128372216774541414)
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

@bot.command
@lightbulb.option('question', 'what do you wanna ask',type=str)
@lightbulb.command('ai', 'pringle grows a brain')
@lightbulb.implements(lightbulb.SlashCommand)
async def ai(event):
    response = generate_response(question)
    await event.message.respond(response)


# RESPOND TO EMPTY PINGS TO PRINCE
prin_pin = ['why ping him when i exist', 'yes?', 'huh', 'yippie']
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping_pring(event):
    if not event.is_human:
        return
    if 409170244201086976 in event.message.user_mentions_ids:
        await event.message.respond(random.choice(prin_pin))

# RESPOND TO EMPTY PINGS TO ICA
ica_pin = ['who pinged my creator', 'i answer on behalf of them', 'i answer on behalf of her', 'you dare summon god?']
@bot.listen(hikari.GuildMessageCreateEvent)
async def ping_pring(event):
    if not event.is_human:
        return
    if 696386024233762825 in event.message.user_mentions_ids:
        await event.message.respond(random.choice(ica_pin))

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
    elif 'manta' in event.content:
        options = ["<:mantaray:1081096190558482496>", "<:stingray:1081094162780274758>", "did someone say manta"]
        await event.message.respond(random.choice(options))
    else:
        count = random.randint(0, 100)
        resp = ["rah", "h", "a", "yippie", "grr", ":3"]
        if count == 1 and event.channel_id != 1128778289083846657:
            await event.message.respond(random.choice(resp))

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
@lightbulb.command('ask-me', 'ask a yes/no question')
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
@lightbulb.implements(lightbulb.SlashCommand)
async def terminate(ctx: lightbulb.Context) -> None:
    await ctx.respond("I'm, eepy,,, <:passedout:1109295492132769842>")
    quit()

'''
#  JOIN VOICE CHANNEL
@bot.command
@lightbulb.command('join', 'Makes bot join a voice channel')
@lightbulb.implements(lightbulb.SlashCommand)
async def join(ctx):
    await bot.update_voice_state(pringles_prison, court)
    await ctx.respond("im in")
'''

# CUSTOM MEMBER GREETINGS
@bot.listen(hikari.GuildMessageCreateEvent)
async def greet(event):
    if not event.is_human:
        return
    if 'hi pri' in event.content or 'Hello Prin' in event.content or 'Hi pri' in event.content or 'hi crisp' in event.content:
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
        elif sender == 'grimm':
            await event.message.respond('hello grimm grimmace grimmerson')
        elif sender == 'prince':
            await event.message.respond('Oh, its you.')
        else:
            await event.message.respond('hi')
    else:
        return

# RECIEVE DMS TO BOT
@bot.listen(hikari.DMMessageCreateEvent)
async def recieve_text(event):
    if event.author_id in ids:
        num_index = ids.index(event.author_id)
        author = members[num_index]
        if author == 'ica' or author == "prince": 
            if "!cell" in event.content:
                reply = event.content.replace("!cell", '')
                await bot.rest.create_message(1080686999922540615, reply)
            elif "!jury" in event.content:
                reply = event.content.replace("!jury", '')
                await bot.rest.create_message(1145761294448869377, reply)
            elif "!gen" in event.content:
                reply = event.content.replace("!gen", '')
                await bot.rest.create_message(1128372218439671921, reply)
            elif "!bot" in event.content:
                reply = event.content.replace("!bot", '')
                await bot.rest.create_message(1130269996325552168, reply)
            elif "!grimm" in event.content:
                reply = event.content.replace("!grimm", '')
                await bot.rest.create_message(1128779968902615161, reply)
            elif "!zym" in event.content:
                reply = event.content.replace("!zym", '')
                await bot.rest.create_message(1128781770775613450, reply)
            elif "!garden" in event.content:
                reply = event.content.replace("!garden", '')
                await bot.rest.create_message(1128797349066588360, reply)
    else:
        return


# LAUNCH BOT OPERATIONS
bot.run(status=hikari.Status.IDLE,
        activity=hikari.Activity(
            name="your bs",
            type=hikari.ActivityType.LISTENING,
        )
    )
