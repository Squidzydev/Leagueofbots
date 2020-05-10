import discord
from discord.ext import commands
import asyncio
import requests
import os
from bs4 import BeautifulSoup


all_champs_russia={
"атрокс":"aatrox",
"экко":"ekko",
"джинкс":"jinx",
"фортуна":"miss-fortune",
"шен":"shen",
"варус":"varus",
"ари":"ahri",
"элиза":"elise",
"калиста":"kalista",
"мордекайзер":"mordekaiser",
"шивана":"shyvana",
"вейн":"vayne",
"акали":"akali",
"эвелин":"evelynn",
"карма":"karma",
"моргана":"morgana",
"синджед":"singed",
"вейгар":"veigar",
"алистар":"alistar",
"эзреаль":"ezreal",
"картус":"karthus",
"нами":"nami",
"сион":"sion",
"велкоз":"velkoz",
"амуму":"amumu",
"фиддлстикс":"fiddlesticks",
"касадин":"kassadin",
"насус":"nasus",
"сивир":"sivir",
"анивия":"anivia",
"флора":"fiora",
"катарина":"katarina",
"наутилус":"nautilus",
"скарнер":"skarner",
"виктор":"viktor",
"энни":"annie",
"физз":"fizz",
"кейл":"kayle",
"нидалли":"nidalee",
"сона":"sona",
"владимир":"vladimir",
"эш":"ashe",
"галио":"galio",
"кеннен":"kennen",
"ноктюрн":"nocturne",
"сорака":"soraka",
"волибир":"volibear",
"аурелион":"aurelion",
"гангпланк":"gangplank",
"казикс":"khazix",
"нуну":"nunu",
"свейн":"swain",
"варвик":"warwick",
"азир":"azir",
"гарен":"garen",
"киндред":"kindred",
"олаф":"olaf",
"синдра":"syndra",
"вуконг":"wukong",
"бард":"bard",
"гнар":"gnar",
"клед":"kled",
"орианна":"orianna",
"тамкенч":"tahm-kench",
"зерат":"xerath",
"блицкранк":"blitzcrank",
"грагас":"gragas",
"когмао":"kogmaw",
"пантеон":"pantheon",
"талия":"taliyah",
"ксинжао":"xin-zhao",
"брэнд":"brand",
"бренд":"brand",
"грейвс":"graves",
"леблан":"leblanc",
"поппи":"poppy",
"талон":"talon",
"ясуо":"yasuo",
"браум":"braum",
"гекарим":"hecarim",
"лисин":"lee-sin",
"лесин":"lee-sin",
"квинн":"quinn",
"тарик":"taric",
"йорик":"yorick",
"кайтлин":"caitlyn",
"хеймердингер":"heimerdinger",
"леона":"leona",
"раммус":"rammus",
"тимо":"teemo",
"зак":"zac",
"камила":"camille",
"иллаой":"illaoi",
"лисандра":"lissandra",
"раксай":"reksai",
"треш":"thresh",
"зед":"zed",
"кассиопея":"cassiopeia",
"ирелия":"irelia",
"люциан":"lucian",
"ренектон":"renekton",
"тристана":"tristana",
"зиггс":"ziggs",
"чогат":"chogath",
"иверн":"ivern",
"лулу":"lulu",
"ренгар":"rengar",
"трандл":"trundle",
"зилеан":"zilean",
"корги":"corki",
"жанна":"janna",
"люкс":"lux",
"ривен":"riven",
"триндамир":"tryndamere",
"зира":"zyra",
"дариус":"darius",
"джарван":"jarvan-iv",
"мальфит":"malphite",
"рамбл":"rumble",
"твистедфейт":"twisted-fate",
"диана":"diana",
"джакс":"jax",
"мальзахар":"malzahar",
"райз":"ryze",
"твич":"twitch",
"мундо":"dr-mundo",
"джейс":"jayce",
"маокай":"maokai",
"седжуани":"sejuani",
"удир":"udyr",
"дрейвен":"draven",
"джин":"jhin",
"мастерйи":"master-yi",
"шако":"shaco",
"ургот":"urgot",
}
Bot = commands.Bot(command_prefix='!')
all_runes_russia ={
    "Press the Attack":"Решительное наступление",
    "Lethal Tempo":"Смертельный темп",
    "Fleet Footwork":"Искусное лавирование",
    "Conqueror":"Завоеватель",
    "Electrocute":"Казнь электричеством",
    "Predator":"Хищник",
    "Dark Harvest":"Темная жатва",
    "Hail of Blades":"Град клинков",
    "Summon Aery":"Призыв Пушинки",
    "Arcane Comet":"Магическая комета",
    "Phase Rush":"Фазовый рывок",
    "Grasp of the Undying":"Хватка нежити",
    "Aftershock":"Дрожь земли",
    "Guardian":"Страж",
    "Glacial Augment":"Ледяной нарост",
    "Unsealed Spellbook":"Раскрытая книга заклинаний",
    "Prototype: Omnistone":"Прототип: Многогранник",
    "Overheal":"Сверхлечение",
    "Triumph":"Триумф",
    "Presence of Mind":"Присутствие духа",
    "Legend: Alacrity":"Легенда: Рвение",
    "Legend: Tenacity":"Легенда: Стойкость",
    "Legend: Bloodline":"Легенда: Родословная",
    "Coup de Grace":"Удар милосердия",
    "Cut Down":"Реванш",
    "Last Stand":"Последний рубеж",
    "Cheap Shot":"Грязный прием",
    "Taste of Blood":"Вкус крови",
    "Sudden Impact":"Внезапный удар",
    "Zombie Ward":"Тотем-зомби",
    "Ghost Poro":"Призрачный поро",
    "Eyeball Collection":"Коллекция глаз",
    "Ravenous Hunter":"Ненасытный охотник",
    "Ingenious Hunter":"Изобретательный охотник",
    "Relentless Hunter":"Беспощадный охотник",
    "Ultimate Hunter":"Абсолютный охотник",
    "Nullifying Orb":"Сфера уничтожения",
    "Manaflow Band":"Поток маны",
    "Nimbus Cloak":"Сияющий плащ",
    "Transcendence":"Превосходство",
    "Celerity":"Быстрота",
    "Absolute Focus":"Полная сосредоточенность",
    "Scorch":"Ожог",
    "Waterwalking":"Хождение по воде",
    "Gathering Storm":"Надвигающаяся буря",
    "Demolish":"Снос",
    "Font of Life":"Живой источник",
    "Shield Bash":"Удар щитом",
    "Conditioning":"Накопление",
    "Second Wind":"Второе дыхание",
    "Bone Plating":"Костяная пластина",
    "Overgrowth":"Разрастание",
    "Revitalize":"Оживление",
    "Unflinching":"Неустрашимость",
    "Hextech Flashtraption":"Хекстековый скачок",
    "Magical Footwear":"Магическая обувь",
    "Perfect Timing":"Самое время",
    "Future's Market":"Рынок будущего",
    "Minion Dematerializer":"Дезинтегратор миньонов",
    "Biscuit Delivery":"Доставка печенья",
    "Cosmic Insight":"Космическое знание",
    "Approach Velocity":"Скорость сближения",
    "Time Warp Tonic":"Тоник искривления времени",
}
Bot.remove_command('help')
@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(705400966148784149)
    await channel.send(f'Привет, легенда {member.mention}, выбери роли(!бот, !топ, !лес, !мид, !саппорт)')
@Bot.event
async def on_ready():
    activity = discord.Game(name='!help - помощь по боту', )
    await Bot.change_presence(activity=activity)

@Bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *,args):

    await ctx.message.delete()
    await ctx.send(args)
@Bot.command(aliases=['помощь'])
@commands.has_permissions(administrator=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Команды', description='!(лайн) - выбрать роль в лиге\n'
                                                       '!руны {чемпион} - руны на чемпиона(имя чемпиона писать слитно)\n'
                                                       '!ранк {ник призывателя} - ранк и мейн призывателя в ранкеде', color=0xf5f5f5)
    embed.set_footer(text= 'LeagueOfBots', icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    message = await ctx.send(embed = embed)
    await asyncio.sleep(10)
    await message.delete()
@Bot.command()
async def runes(ctx, *, args):
    await ctx.message.delete()
    name_of_hero = ''
    for x in args:
      name_of_hero = args
    name = name_of_hero
    name_of_hero=all_champs_russia[name_of_hero.lower()]
    url = 'https://www.leaguespy.gg/league-of-legends/champion/' + name_of_hero+'/stats'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2',

    }
    print(url)
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'html.parser')

    rune1 = bs.find('div', attrs={'class':"rune-block__rune keystone rune-tt"})
    rune_sec = bs.find_all('div', attrs={'class':"rune-block__rune rune-tt"})
    rune_add = bs.find_all('div', attrs={'class': "rune-block__shard"})
    main_rune = all_runes_russia[rune1['name']]
    rune_sec1 = all_runes_russia[rune_sec[0]['name']]
    rune_sec2 = all_runes_russia[rune_sec[1]['name']]
    rune_sec3 = all_runes_russia[rune_sec[2]['name']]
    rune_sec4 = all_runes_russia[rune_sec[3]['name']]
    rune_sec5 = all_runes_russia[rune_sec[4]['name']]
    rune_add1 = rune_add[0]['title']
    rune_add2 = rune_add[1]['title']
    rune_add3 = rune_add[2]['title']
    title = 'Руны на чемпиона '+name
    disc = 'Главная руна: \n'+main_rune+'\n' + 'Добавочные руны: \n'+rune_sec1+'\n'+rune_sec2+'\n'+rune_sec3+'\n'+'Вторичные руны: \n'+rune_sec4+'\n'+rune_sec5+'\n'+'Адаптивные руны: \n'+rune_add1+'\n'+rune_add2+'\n'+rune_add3
    embed = discord.Embed(color=0xf5f5f5, title=title, description=disc)
    embed.set_footer(text='LeagueOfBots',icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    await ctx.send(embed = embed)








@Bot.command()
async def rank(ctx, *,args):
    name = ''
    await ctx.message.delete()
    for x in args:
        name = args+'+'
    name = name[0:-1]
    url = "https://www.leagueofgraphs.com/ru/summoner/ru/"+name+"#championsData-all-queues"
    print(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2',
        'championsData':'all-queues'
    }
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'html.parser')

    rank = bs.find('div', attrs={'class': 'leagueTier'})


    rank1 = rank.text
    data = {
        'championsData':'all-queues'
    }
    url = 'https://www.leagueofgraphs.com/ru/summoner/champions/ru/'+name+'#championsData-all-queues'
    print(url)
    r = requests.get(url,headers = header, data=data)
    bs = BeautifulSoup(r.text, 'html.parser')
    main = bs.find('span', attrs={'class':'name'})
    t = 'Инфо о игроке '+ name
    main = '```css\n'+'Мейн: '+main.text+'```'
    ranke = '```css'+rank1.replace(' ', '')+'```'
    embed = discord.Embed(title=t, description=ranke +''+main, color=0xf5f5f5)
    embed.set_footer(text='LeagueOfBots',icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    await ctx.send(embed=embed)
@Bot.command(aliases=['саппорт', 'сап', 'sup'])
async def support(ctx,):
    await ctx.message.delete()
    member = ctx.message.author
    if ctx.channel.name == "шестеренка":

        if "саппорт" in [y.name.lower() for y in member.roles]:

            role = discord.utils.get(ctx.guild.roles, name="Саппорт")
            await member.remove_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Саппорт")
            await member.add_roles(role)
@Bot.command(aliases=['топер', 'топ'])
async def top(ctx,):
    await ctx.message.delete()
    member = ctx.message.author
    if ctx.channel.name == "шестеренка":

        if "топ" in [y.name.lower() for y in member.roles]:

            role = discord.utils.get(ctx.guild.roles, name="Топ")
            await member.remove_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Топ")
            await member.add_roles(role)
@Bot.command(aliases=['ботер', 'бот'])
async def bot(ctx,):
    await ctx.message.delete()
    member = ctx.message.author
    if ctx.channel.name == "шестеренка":

        if "бот" in [y.name.lower() for y in member.roles]:

            role = discord.utils.get(ctx.guild.roles, name="Бот")
            await member.remove_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Бот")
            await member.add_roles(role)
@Bot.command(aliases=['мидер', 'мид'])
async def mid(ctx,):
    await ctx.message.delete()
    member = ctx.message.author
    if ctx.channel.name == "шестеренка":

        if "мид" in [y.name.lower() for y in member.roles]:

            role = discord.utils.get(ctx.guild.roles, name="Мид")
            await member.remove_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Мид")
            await member.add_roles(role)
@Bot.command(aliases=['лес', 'лесник'])
async def jungle(ctx,):
    await ctx.message.delete()
    member = ctx.message.author
    if ctx.channel.name == "шестеренка":

        if "лесник" in [y.name.lower() for y in member.roles]:

            role = discord.utils.get(ctx.guild.roles, name="Лесник")
            await member.remove_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Лесник")
            await member.add_roles(role)
@Bot.command(aliases=['удалить'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        await ctx.send('Укажите кол-во сообщений которые надо удалить', delete_after=10)
    else:
        await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title='Удаление сообщений',
                            description=f'Админ {ctx.author.mention} почистил чат.', color=0xf5f5f5)
        emb.set_footer(text='LeagueOfBots',
                         icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
        await ctx.send(embed=emb, delete_after=10)




key = os.environ.get('TOKEN')

Bot.run('NzA1MzcxMzYzMDI3ODQ1MTUw.XqquXA.0j776SXOG3FUfOj5rJHLGwJomyY')
