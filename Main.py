import discord
from discord.ext import commands

import requests
import os
from bs4 import BeautifulSoup



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

@Bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *,args):

    await ctx.message.delete()
    await ctx.send(args)

@Bot.command()
async def runes(ctx, *, args):
    await ctx.message.delete()
    name_of_hero = ''
    for x in args:
        name_of_hero = args + '+'
    name_of_hero = name_of_hero[0:-1]
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
    title = 'Руны на чемпиона '+name_of_hero
    disc = 'Главная руна: \n'+main_rune+'\n' + 'Добавочные руны: \n'+rune_sec1+'\n'+rune_sec2+'\n'+rune_sec3+'\n'+'Вторичные руны: \n'+rune_sec4+'\n'+rune_sec5+'\n'+'Адаптивные руны: \n'+rune_add1+'\n'+rune_add2+'\n'+rune_add3
    embed = discord.Embed(color=0x00ff00, title=title, description=disc)
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
    embed = discord.Embed(title=t, description=ranke +''+main, color=0x00ff00)
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
                            description=f'Админ {ctx.author.mention} почистил чат.')
        await ctx.send(embed=emb, delete_after=10)




key = os.environ.get('TOKEN')

Bot.run(key)