import discord
import json
import random
import re
import asyncio

client = discord.Client()

# Weird python script to "re-role" people as a feudal hiarchy. 
# also writes a backup of all users

@client.event
async def on_ready():
    def get_name(name):
        sufix = ["port", "clare", "ley", "view", "folk", "sex", "karta", "grad", "hampton", "stead", "stedt", "stätt", "dorf", "wych", "wick", "wyke", "wich", "thorpe", "thorp", "ceter", "ham", "cester", "stadt", "caster", "by", "dale", "field", "ford", "town", "bury", "chester", "ton", "burgh", "burg", "ville"]
        temp = re.findall('[A-Z][^A-Z]*', name)
        if not temp:
            temp = [name]
        final = []
        for t in temp:
            for s in t.split():
                final.append(s)
        return f"{random.choice(final)}{random.choice(sufix)}"


    def get_color():
        return discord.Colour.from_rgb(random.randrange(0, 255),
                                        random.randrange(0, 255),
                                        random.randrange(0, 255))


    async def set_roles(member, role):
        try:
            print(f"Changing roles for {member.name}")
            roles = member.roles
            roles.remove(server.default_role)
            print(roles)
            await member.remove_roles(*roles)
            await member.add_roles(role)
        except:
            print(f"That hecker {member.name} broke while swapping roles")


    print('We have logged in as {0.user}'.format(client))
    print(client.guilds)
    server = client.guilds[0]
    users = {}
    scanies = []
    normies = []
    for m in server.members:
        roles = []
        if m.name in ["alizim110", "tayler1986", "Salt Mine", "Simplebird", "ChooseANameBetween2and32Chars", "MEE6", "PatchBot", "Stat Tracker"]:
            users[m.id] = m.roles
            continue
        is_sc = False
        for r in m.roles:
            if r.name in 'SCAN CLAN':
                is_sc = True
                scanies.append(m)
            roles.append(r.id)
        if not is_sc:
            normies.append(m)
        users[m.id] = m.roles

    country = get_name("alizim110")
    b_name = f"Baron of {country}"
    baron_role = await server.create_role(name=b_name,
        colour=get_color(),
        hoist=True,
        mentionable=True,
        reason="oWo It's the drift incident all over again!")
    # Get 2 barons
    for i in range(0,2):
        baron = scanies.pop(random.randrange(0, len(scanies)))
        baron_domain = get_name(baron.name)
        cap = get_name(baron.name)
        k_name = f"Knight of {baron_domain}"
        cat = await server.create_category(baron_domain)
        knight_role = await server.create_role(name=k_name,
            colour=get_color(),
            hoist=True,
            mentionable=True,
            reason="0wo It's the drift incident all over again!")
        barron_overwrites = {
            server.default_role: discord.PermissionOverwrite(send_messages=False),
            baron_role: discord.PermissionOverwrite(send_messages=True, send_tts_messages=True, manage_messages=True),
            knight_role: discord.PermissionOverwrite(send_messages=True)
        }
        await set_roles(baron, baron_role)
        await server.create_text_channel(cap, overwrites=barron_overwrites, category=cat)
        # Create baron area

        # Get 9 knights
        for j in range(0,9):
            knight = scanies.pop(random.randrange(0, len(scanies)))
            knight_domain = get_name(knight.name)
            p_name = f"Peasant of {knight_domain}"
            await set_roles(knight, knight_role)
            print(knight_domain)
            # Create peasant role
            peasant_role = await server.create_role(name=p_name,
                colour=get_color(),
                hoist=True,
                mentionable=True,
                reason="uWu It's the drift incident all over again!")
            knight_overwrites = {
                server.default_role: discord.PermissionOverwrite(send_messages=False),
                baron_role: discord.PermissionOverwrite(send_messages=True, send_tts_messages=True, manage_messages=True),
                knight_role: discord.PermissionOverwrite(send_messages=True, send_tts_messages=True, manage_messages=True),
                peasant_role: discord.PermissionOverwrite(send_messages=True)
            }
            await server.create_text_channel(knight_domain, overwrites=knight_overwrites, category=cat)
            # Get 6 peasants
            for k in range(0,3):
                peasant = normies.pop(random.randrange(0, len(normies)))
                await set_roles(peasant, peasant_role)


    with open('data.json', 'w') as outfile:
            json.dump(users, outfile)
    print(len(scanies))
    print(len(normies))
    print("Backup written. Done!")
    exit(0)




client.run('discord-token')
