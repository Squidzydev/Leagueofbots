import discord
from discord.ext import commands
import asyncio
import requests
import os
from random import *

from bs4 import BeautifulSoup
from discord import Colour
import cassiopeia as cass
import datetime

all_champs_russia = {
    "атрокс": "aatrox",
    "экко": "ekko",
    "джинкс": "jinx",
    "фортуна": "miss-fortune",
    "шен": "shen",
    "варус": "varus",
    "ари": "ahri",
    "элиза": "elise",
    "калиста": "kalista",
    "мордекайзер": "mordekaiser",
    "шивана": "shyvana",
    "вейн": "vayne",
    "акали": "akali",
    "эвелин": "evelynn",
    "карма": "karma",
    "моргана": "morgana",
    "синджед": "singed",
    "вейгар": "veigar",
    "алистар": "alistar",
    "эзреаль": "ezreal",
    "картус": "karthus",
    "нами": "nami",
    "сион": "sion",
    "велкоз": "velkoz",
    "амуму": "amumu",
    "фиддлстикс": "fiddlesticks",
    "касадин": "kassadin",
    "насус": "nasus",
    "сивир": "sivir",
    "анивия": "anivia",
    "флора": "fiora",
    "катарина": "katarina",
    "наутилус": "nautilus",
    "скарнер": "skarner",
    "виктор": "viktor",
    "энни": "annie",
    "физз": "fizz",
    "кейл": "kayle",
    "нидалли": "nidalee",
    "сона": "sona",
    "владимир": "vladimir",
    "эш": "ashe",
    "галио": "galio",
    "кеннен": "kennen",
    "ноктюрн": "nocturne",
    "сорака": "soraka",
    "волибир": "volibear",
    "аурелион": "aurelion",
    "гангпланк": "gangplank",
    "казикс": "khazix",
    "нуну": "nunu",
    "свейн": "swain",
    "варвик": "warwick",
    "азир": "azir",
    "гарен": "garen",
    "киндред": "kindred",
    "олаф": "olaf",
    "синдра": "syndra",
    "вуконг": "wukong",
    "бард": "bard",
    "гнар": "gnar",
    "клед": "kled",
    "орианна": "orianna",
    "тамкенч": "tahm-kench",
    "зерат": "xerath",
    "блицкранк": "blitzcrank",
    "грагас": "gragas",
    "когмао": "kogmaw",
    "пантеон": "pantheon",
    "талия": "taliyah",
    "ксинжао": "xin-zhao",
    "брэнд": "brand",
    "бренд": "brand",
    "грейвз": "graves",
    "леблан": "leblanc",
    "поппи": "poppy",
    "талон": "talon",
    "ясуо": "yasuo",
    "браум": "braum",
    "гекарим": "hecarim",
    "лисин": "lee-sin",
    "лесин": "lee-sin",
    "квинн": "quinn",
    "тарик": "taric",
    "йорик": "yorick",
    "кайтлин": "caitlyn",
    "хеймердингер": "heimerdinger",
    "леона": "leona",
    "раммус": "rammus",
    "тимо": "teemo",
    "зак": "zac",
    "камила": "camille",
    "камилла": "camille",
    "иллаой": "illaoi",
    "лисандра": "lissandra",
    "раксай": "reksai",
    "треш": "thresh",
    "зед": "zed",
    "кассиопея": "cassiopeia",
    "ирелия": "irelia",
    "люциан": "lucian",
    "ренектон": "renekton",
    "тристана": "tristana",
    "зиггс": "ziggs",
    "чогат": "chogath",
    "иверн": "ivern",
    "лулу": "lulu",
    "ренгар": "rengar",
    "трандл": "trundle",
    "зилеан": "zilean",
    "корги": "corki",
    "жанна": "janna",
    "люкс": "lux",
    "ривен": "riven",
    "триндамир": "tryndamere",
    "зира": "zyra",
    "дариус": "darius",
    "джарван": "jarvan-iv",
    "мальфит": "malphite",
    "рамбл": "rumble",
    "твистедфейт": "twisted-fate",
    "диана": "diana",
    "джакс": "jax",
    "мальзахар": "malzahar",
    "райз": "ryze",
    "твич": "twitch",
    "мундо": "dr-mundo",
    "джейс": "jayce",
    "маокай": "maokai",
    "седжуани": "sejuani",
    "удир": "udyr",
    "дрейвен": "draven",
    "джин": "jhin",
    "мастерйи": "master-yi",
    "шако": "shaco",
    "ургот": "urgot",
    "афелий": "aphelios",
    "сенна": "senna",
    "пайк": "pyke",
    "сетт": "sett",
    "орн": "ornn",
    "кайн": "kayn",
    "каин": "kayn",
    "юми": "yuumi",
    "самира": "samira",
    "ёнэ": "yone",
}
Bot = commands.Bot(command_prefix='!')
all_runes_russia = {
    "Press the Attack": "Решительное наступление",
    "Lethal Tempo": "Смертельный темп",
    "Fleet Footwork": "Искусное лавирование",
    "Conqueror": "Завоеватель",
    "Electrocute": "Казнь электричеством",
    "Predator": "Хищник",
    "Dark Harvest": "Темная жатва",
    "Hail of Blades": "Град клинков",
    "Summon Aery": "Призыв Пушинки",
    "Arcane Comet": "Магическая комета",
    "Phase Rush": "Фазовый рывок",
    "Grasp of the Undying": "Хватка нежити",
    "Aftershock": "Дрожь земли",
    "Guardian": "Страж",
    "Glacial Augment": "Ледяной нарост",
    "Unsealed Spellbook": "Раскрытая книга заклинаний",
    "Prototype: Omnistone": "Прототип: Многогранник",
    "Overheal": "Сверхлечение",
    "Triumph": "Триумф",
    "Presence of Mind": "Присутствие духа",
    "Legend: Alacrity": "Легенда: Рвение",
    "Legend: Tenacity": "Легенда: Стойкость",
    "Legend: Bloodline": "Легенда: Родословная",
    "Coup de Grace": "Удар милосердия",
    "Cut Down": "Реванш",
    "Last Stand": "Последний рубеж",
    "Cheap Shot": "Грязный прием",
    "Taste of Blood": "Вкус крови",
    "Sudden Impact": "Внезапный удар",
    "Zombie Ward": "Тотем-зомби",
    "Ghost Poro": "Призрачный поро",
    "Eyeball Collection": "Коллекция глаз",
    "Ravenous Hunter": "Ненасытный охотник",
    "Ingenious Hunter": "Изобретательный охотник",
    "Relentless Hunter": "Беспощадный охотник",
    "Ultimate Hunter": "Абсолютный охотник",
    "Nullifying Orb": "Сфера уничтожения",
    "Manaflow Band": "Поток маны",
    "Nimbus Cloak": "Сияющий плащ",
    "Transcendence": "Превосходство",
    "Celerity": "Быстрота",
    "Absolute Focus": "Полная сосредоточенность",
    "Scorch": "Ожог",
    "Waterwalking": "Хождение по воде",
    "Gathering Storm": "Надвигающаяся буря",
    "Demolish": "Снос",
    "Font of Life": "Живой источник",
    "Shield Bash": "Удар щитом",
    "Conditioning": "Накопление",
    "Second Wind": "Второе дыхание",
    "Bone Plating": "Костяная пластина",
    "Overgrowth": "Разрастание",
    "Revitalize": "Оживление",
    "Unflinching": "Неустрашимость",
    "Hextech Flashtraption": "Хекстековый скачок",
    "Magical Footwear": "Магическая обувь",
    "Perfect Timing": "Самое время",
    "Future's Market": "Рынок будущего",
    "Minion Dematerializer": "Дезинтегратор миньонов",
    "Biscuit Delivery": "Доставка печенья",
    "Cosmic Insight": "Космическое знание",
    "Approach Velocity": "Скорость сближения",
    "Time Warp Tonic": "Тоник искривления времени",
}
Bot.remove_command('help')

@Bot.event
async def on_ready():
    activity = discord.Game(name='!help - помощь по боту')
    await Bot.change_presence(activity=activity)

@Bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args)


@Bot.command(aliases=['помощь'])
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Команды', description='!руны {чемпион} - руны на чемпиона(имя чемпиона писать слитно)\n'
                                                       '!аватар {пинг пользователя, без пинга покажется ваш аватар}\n'
                                                       '!summoner {ник призывателя} - ранк, уровень и мейн призывателя в ранкеде\n'
                                                       '!live {ник призывателя} - статистика матча\n'
                                                       '!changelog - изменения бота\n'
                                                       '!random {название канала} {кол-во участников}\n'
                                                       'https://goo.su/leaguebot - добавь бота к себе!', color=0xf5f5f5)

    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    message = await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await message.delete()


@Bot.command(aliases=['изменения'])
async def changelog(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Изменения бота',
                          description='**1.3**\n'
                                      '$!ранг -> !summoner(Команда изменена)'
                                      '**1.4**\n'
                                      '$Удалены команды **!bot, !top, !mid, !sup, !jungle** за ненадобностью'
                                      '**1.5**\n'
                                      '$Добавлена команда !random',
                          color=0xf5f5f5)

    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    message = await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await message.delete()


@Bot.command(aliases=['ава', 'аватар'])
async def ava(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user == None:

        ava = ctx.message.author.avatar_url
        t = 'Аватарка призывателя: ' + '**' + ctx.message.author.name + '**'
        em = discord.Embed(title=t, color=0xf5f5f5)
        em.set_image(url=ava)
        em.set_footer(text='LeagueOfBots',
                      icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
        await ctx.send(embed=em)
    else:
        ava = user.avatar_url
        t = 'Аватарка призывателя: ' + '**' + user.name + '**'
        em = discord.Embed(title=t, color=0xf5f5f5)
        em.set_image(url=ava)
        em.set_footer(text='LeagueOfBots',
                      icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
        await ctx.send(embed=em)


@Bot.command(aliases=['руны'])
async def runes(ctx, *, args):
    await ctx.message.delete()
    name_of_hero = ''
    for x in args:
        name_of_hero = args
    name = name_of_hero
    name_of_hero = all_champs_russia[name_of_hero.lower()]
    url = 'https://www.leaguespy.gg/league-of-legends/champion/' + name_of_hero + '/stats'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2',

    }
    print(url)
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'html.parser')

    rune1 = bs.find('div', attrs={'class': "rune-block__rune keystone rune-tt"})
    rune_sec = bs.find_all('div', attrs={'class': "rune-block__rune rune-tt"})
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
    title = 'Руны на чемпиона ' + name
    embed = discord.Embed(color=0xf5f5f5, title=title)
    embed.add_field(name='Главные руны', value=main_rune + '\n' + rune_sec1 + '\n' + rune_sec2 + '\n' + rune_sec3,
                    inline=True)
    embed.add_field(name='Добавочные руны', value=rune_sec4 + '\n' + rune_sec5, inline=True)
    embed.add_field(name='Адаптивные руны', value=rune_add1 + '\n' + rune_add2 + '\n' + rune_add3)
    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.name)
    url_a = f'https://www.mobafire.com/images/champion/square/' + name_of_hero + '.png'
    embed.set_thumbnail(url=url_a)
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'html.parser')
    text = bs.find('div', attrs={'class': 'skill-block__top'})
    text = text.find_all('li')
    poryadok = ''
    for x in text:
        poryadok = poryadok + x.find('span').text + '->'
    poryadok = poryadok[0: -2]
    embed.add_field(name='Подрядок умений', value=poryadok, inline=True)
    await ctx.send(embed=embed)


@Bot.command(aliases=['информация', 'саммонер', 'призыватель'])
async def summoner(ctx, name: str = None):
    await ctx.message.delete()
    key = os.environ.get('RIOT')
    cass.set_riot_api_key(key)
    lvl =''
    rank = 'Нет ранга'
    mainer = ''
    win1 = ''
    win2 = ''
    win3 = ''
    win4 = ''
    ch1 = ''
    ch2 = ''
    ch3 = ''
    ch4 = ''
    wins = ''
    if name == None:
        await ctx.send('Введите ник призывателя')
    else:
        summoner = cass.get_summoner(region='RU', name=name)
        lvl = str(summoner.level)
        try:
            rank = str(summoner.league_entries[0].tier) + ' ' + str(summoner.league_entries[0].division)
        except:
            pass
        mainer = str(summoner.champion_masteries[0].champion.name)
        for x in cass.get_match(summoner.match_history[0].id, region='RU').red_team.participants:
            if x.summoner.name == summoner.name:
                ch1 = '('+x.champion.name+')'
                if cass.get_match(summoner.match_history[0].id, region='RU').red_team.win == False:
                    win1 = ch1+"Поражение:red_circle:"
                else:
                    win1 = ch1+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[0].id, region='RU').blue_team.participants:
            if x.summoner.name == summoner.name:
                ch1 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[0].id, region='RU').blue_team.win == False:
                    win1 = ch1+"Поражение:red_circle:"
                else:
                    win1 = ch1+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[1].id, region='RU').red_team.participants:
            if x.summoner.name == summoner.name:
                ch2 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[1].id, region='RU').red_team.win == False:
                    win2 = ch2+"Поражение:red_circle:"
                else:
                    win2 = ch2+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[1].id, region='RU').blue_team.participants:
            if x.summoner.name == summoner.name:
                ch2 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[1].id, region='RU').blue_team.win == False:
                    win2 = ch2+"Поражение:red_circle:"
                else:
                    win2 = ch2+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[2].id, region='RU').red_team.participants:
            if x.summoner.name == summoner.name:
                ch3 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[2].id, region='RU').red_team.win == False:
                    win3 = ch3+"Поражение:red_circle:"
                else:
                    win3 = ch3+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[2].id, region='RU').blue_team.participants:
            if x.summoner.name == summoner.name:
                ch3 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[2].id, region='RU').blue_team.win == False:
                    win3 = ch3+"Поражение:red_circle:"
                else:
                    win3 = ch3+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[3].id, region='RU').red_team.participants:
            if x.summoner.name == summoner.name:
                ch4 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[3].id, region='RU').red_team.win == False:
                    win3 = ch4+"Поражение:red_circle:"
                else:
                    win3 = ch4+'Победа:green_circle:'
        for x in cass.get_match(summoner.match_history[3].id, region='RU').blue_team.participants:
            if x.summoner.name == summoner.name:
                ch4 = '(' + x.champion.name + ')'
                if cass.get_match(summoner.match_history[3].id, region='RU').blue_team.win == False:
                    win4 = ch4+"Поражение:red_circle:"
                else:
                    win4 = ch4+'Победа:green_circle:'
    wins = win1 +'\n'+win2+'\n'+win3+'\n'+win4
    t = 'Информация о призывателе: '+name
    embed = discord.Embed(title=t, color=0xf5f5f5)
    embed.add_field(name ='**Ранг:**',value=rank, inline=True)
    embed.add_field(name='**Лвл:**', value=lvl, inline=True)
    embed.add_field(name='**Мейн:**', value=mainer, inline=True)
    embed.add_field(name='**Последние игры:**', value=wins, inline=True)
    embed.set_thumbnail(url =summoner.profile_icon.url)
    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    await ctx.send(embed=embed)



@Bot.command()
async def mute(ctx,  channel: str = None):
    await ctx.message.delete()
    for a in ctx.message.author.roles:
        if "canmute" in a.name:
            if channel == None:
               pass
            else:
                ch = discord.utils.get(ctx.message.guild.voice_channels, name=channel)
                members_list = ch.members
                for x in members_list:
                    await x.edit(mute = True)


@Bot.command()
async def unmute(ctx,  channel: str = None):
    await ctx.message.delete()
    for a in ctx.message.author.roles:
        if "canmute" in a.name:
            if channel == None:
               pass
            else:
                ch = discord.utils.get(ctx.message.guild.voice_channels, name=channel)
                members_list = ch.members
                for x in members_list:
                    await x.edit(mute = False)



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

@Bot.command(aliases=['рандом','прятки','кто'])
@commands.has_permissions(administrator=True)
async def random(ctx, name_of_channel: str = None, count: int = 1, par: str = ''):
    await ctx.message.delete()
    members = []
    random_members = ''
    ch = discord.utils.get(ctx.message.guild.voice_channels, name=name_of_channel)
    members_list = ch.members
    if name_of_channel == None or count == None or count <1:
        emb = discord.Embed()
        emb.title = 'Что-то пошло не так...'
        emb.description = 'Проверьте введенные данные: ' \
                          '!рандом канал кол-во'
        emb.colour = 0xff1919
        message = await ctx.send(embed=emb)
        await asyncio.sleep(10)
        await message.delete()
    else:
        for x in range(count):
            member = choice(members_list)
            members.append(member.name)
            members = list(set(members))

        if par == '':
            for x in members:
                random_members += x + '\n'
        else:
            for x in members:
                random_members += x +' **'+par+'**' + '\n'
        emb = discord.Embed()
        emb.title = 'Случайно выбранные участники из канала '+name_of_channel
        emb.description = random_members
        emb.colour = 0xfcfafa
        emb.set_footer(text='LeagueOfBots',
                       icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')

        message = await ctx.send(embed=emb)
        await asyncio.sleep(10)
        await message.delete()
@Bot.command(aliases=['лайв', 'лаив'])
async def live(ctx, name: str = None):
    if name == None:
        await ctx.send('Введите никнейм призывателя')
        await ctx.message.delete()
    else:
        await ctx.message.delete()
        key = os.environ.get('RIOT')
        cass.set_riot_api_key(key)
        cass.set_default_region("RU")
        summoner = cass.get_summoner(name=name)
        match = cass.get_current_match(summoner)
        rt = summoner.current_match.red_team.participants
        rteam = ""
        bteam = ""

        masters = {
            '7': '<:Level_7:736291517676912660>',
            '6': '<:Level_6:736291517592764426>',
            '5': '<:Level_5:736291517416603658>',
            '4': '<:Level_4:736291517068738631>',
        }
        tiers = {
            'Iron': '<:Iron:736282364874850386>',
            'Bronze': '<:Bronze:736282364984164503>',
            'Silver': '<:Silver:736282365177102436>',
            'Gold': '<:Gold:736282364866723861>',
            'Platinum': '<:Platinum:736282365252337724>',
            'Diamond': '<:Diamond:736282364795420773>',
            'Master': '<:Master:736282365202006131>',
            'Grandmaster': '<:Grandmaster:736282364849684531>',
            'Challenger': '<:Challenger:736282365504127047>',

        }
        for x in rt:
            cm = ''
            tier = ''
            try:

                tier = str(x.summoner.league_entries[0].tier)
                tier = tiers[tier]
                cmm = cass.get_champion_mastery(x.summoner, x.champion, region='RU')
                cm = masters[str(cmm.level)]



            except:
                pass

            rteam = rteam + '\n' + '(' + str(
                x.summoner.level) + ')' + x.summoner.name + ' - ' + cm + x.champion.name + ' ' + tier

        bt = summoner.current_match.blue_team.participants
        for x in bt:
            cm = ''
            tier = ''
            try:
                tier = str(x.summoner.league_entries[0].tier)
                tier = tiers[tier]
                cmm = cass.get_champion_mastery(x.summoner, x.champion, region='RU')
                cm = masters[str(cmm.level)]
            except:
                pass
            bteam = bteam + '\n' + '(' + str(
                x.summoner.level) + ')' + x.summoner.name + ' - ' + cm + x.champion.name + ' ' + tier

        mode = match.map.name
        ava = summoner.profile_icon.url
        t = 'Лайв игра: ' + name
        em = discord.Embed(title=t, color=0xf5f5f5)
        em.add_field(name='Синяя команда:', value=bteam, inline=True)
        em.add_field(name='Красная команда:', value=rteam, inline=True)
        em.set_footer(text=str(mode), icon_url=ava)
        await ctx.send(embed=em)


key = os.environ.get('TOKEN')
Bot.run(key)
