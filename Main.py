import discord
from discord.ext import commands
import asyncio
import requests
import os

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
async def on_member_join(member):
    channel = Bot.get_channel(705400966148784149)
    await channel.send(f'Привет, легенда {member.mention}, выбери роли(!бот, !топ, !лес, !мид, !саппорт)')


@Bot.event
async def on_ready():
    activity = discord.Game(name='!help - помощь по боту', )
    await Bot.change_presence(activity=activity)


@Bot.event
async def on_guild_join(guild):
    await guild.create_role(name="Бот", color=Colour.from_rgb(255, 255, 228))
    await guild.create_role(name="Топ", color=Colour.from_rgb(255, 255, 228))
    await guild.create_role(name="Мид", color=Colour.from_rgb(255, 255, 228))
    await guild.create_role(name="Саппорт", color=Colour.from_rgb(255, 255, 228))
    await guild.create_role(name="Лесник", color=Colour.from_rgb(255, 255, 228))


@Bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args)


@Bot.command(aliases=['помощь'])
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Команды', description='!(лайн) - выбрать роль в лиге\n'
                                                       '!руны {чемпион} - руны на чемпиона(имя чемпиона писать слитно)\n'
                                                       '!аватар {пинг пользователя, без пинга покажется ваш аватар}\n'
                                                       '!ранк {ник призывателя} - ранк и мейн призывателя в ранкеде\n'
                                                       '!live {ник призывателя} - статистика матча\n'
                                                       '!changelog - изменения бота\n'
                                                       'https://goo.su/leaguebot - добавь бота к себе!', color=0xf5f5f5)

    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    message = await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await message.delete()


@Bot.command(aliases=['изменения'])
async def changelog(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Изменения - 1.12',
                          description='$Добавлена команда: !live - помотреть матч призывателя \n$Теперь бота можно добавить к вам в дискорд канал - https://goo.su/leaguebot',
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


@Bot.command(aliases=['rang', 'ранк', 'ранг'])
async def rank(ctx, *, args):
    name = ''
    await ctx.message.delete()
    for x in args:
        name = args + '+'
    name = name[0:-1]
    url = "https://www.leagueofgraphs.com/ru/summoner/ru/" + name + "#championsData-all-queues"
    print(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2',
        'championsData': 'all-queues'
    }
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'html.parser')

    rank = bs.find('div', attrs={'class': 'leagueTier'})

    rank1 = rank.text
    data = {
        'championsData': 'all-queues'
    }
    url = 'https://www.leagueofgraphs.com/ru/summoner/champions/ru/' + name + '#championsData-all-queues'
    print(url)
    r = requests.get(url, headers=header, data=data)
    bs = BeautifulSoup(r.text, 'html.parser')
    main = bs.find('span', attrs={'class': 'name'})
    t = 'Инфо о игроке ' + name
    main = '```css\n' + 'Мейн: ' + main.text + '```'
    ranke = '```css' + rank1.replace(' ', '') + '```'
    embed = discord.Embed(title=t, description=ranke + '' + main, color=0xf5f5f5)
    embed.set_footer(text='LeagueOfBots',
                     icon_url='https://cdn.discordapp.com/attachments/500621541546000388/709146278050922596/1568968178125834341.jpg')
    await ctx.send(embed=embed)


@Bot.command(aliases=['саппорт', 'сап', 'sup'])
async def support(ctx, ):
    await ctx.message.delete()
    member = ctx.message.author

    if "саппорт" in [y.name.lower() for y in member.roles]:

        role = discord.utils.get(ctx.guild.roles, name="Саппорт")
        await member.remove_roles(role)
    else:
        role = discord.utils.get(ctx.guild.roles, name="Саппорт")
        await member.add_roles(role)


@Bot.command(aliases=['топер', 'топ'])
async def top(ctx, ):
    await ctx.message.delete()
    member = ctx.message.author

    if "топ" in [y.name.lower() for y in member.roles]:

        role = discord.utils.get(ctx.guild.roles, name="Топ")
        await member.remove_roles(role)
    else:
        role = discord.utils.get(ctx.guild.roles, name="Топ")
        await member.add_roles(role)


@Bot.command(aliases=['ботер', 'бот'])
async def bot(ctx, ):
    await ctx.message.delete()
    member = ctx.message.author

    if "бот" in [y.name.lower() for y in member.roles]:

        role = discord.utils.get(ctx.guild.roles, name="Бот")
        await member.remove_roles(role)
    else:
        role = discord.utils.get(ctx.guild.roles, name="Бот")
        await member.add_roles(role)


@Bot.command(aliases=['мидер', 'мид'])
async def mid(ctx, ):
    await ctx.message.delete()
    member = ctx.message.author

    if "мид" in [y.name.lower() for y in member.roles]:

        role = discord.utils.get(ctx.guild.roles, name="Мид")
        await member.remove_roles(role)
    else:
        role = discord.utils.get(ctx.guild.roles, name="Мид")
        await member.add_roles(role)


@Bot.command(aliases=['лес', 'лесник'])
async def jungle(ctx, ):
    await ctx.message.delete()
    member = ctx.message.author

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


@Bot.command(aliases=['лайв', 'лаив'])
async def live(ctx, name: str = None):
    if name == None:
        await ctx.send('Введите никнейм призывателя')
        await ctx.message.delete()
    else:
        await ctx.message.delete()
        mes = await ctx.send('Ожидание может занять до 1 минуты, т.к. сервера перегружены')
        await asyncio.sleep(4)
        await mes.delete()
        key = os.environ.get('RIOT')
        cass.set_riot_api_key(key)
        cass.set_default_region("RU")
        summoner = cass.get_summoner(name=name)
        match = cass.get_current_match(summoner)
        rt = summoner.current_match.red_team.participants
        rteam = ""
        bteam = ""
        tier = ''
        cm = ''

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
            try:

                tier = str(x.summoner.league_entries[0].tier)
                tier = tiers[tier]
                cmm = cass.get_champion_mastery(x.summoner, x.champion, region='RU')
                cm = masters[str(cmm.level)]



            except:
                pass
            if tier is not '':
                if cm is not '':
                    rteam = rteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' + cm+x.champion.name + ' ' + tier
                else:
                    rteam = rteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' + x.champion.name + ' ' + tier
            else:
                if cm is not '':
                    rteam = rteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' +cm+ x.champion.name
                else:
                    rteam = rteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' + x.champion.name

        bt = summoner.current_match.blue_team.participants
        cm = ''
        for x in bt:
            try:
                tier = str(x.summoner.league_entries[0].tier)
                tier = tiers[tier]
                cmm = cass.get_champion_mastery(x.summoner, x.champion, region='RU')
                cm = masters[str(cmm.level)]
            except:
                pass
            if tier is not '':
                if cm is not '':
                    bteam = bteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' +cm+ x.champion.name + ' ' + tier
                else:
                    bteam = bteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' + x.champion.name + ' ' + tier
            else:
                if cm is not '':
                    bteam = bteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' +cm+ x.champion.name
                else:
                    bteam = bteam + '\n' + '(' + str(
                        x.summoner.level) + ')' + x.summoner.name + ' - ' + x.champion.name

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
