#!/usr/env python3

import discord
import json
import random
import re
import asyncio

client = discord.Client()


# Removes the list of channels

@client.event
async def on_ready():

    server = client.guilds[0]
    delete_plz = ['Peasant of Gearhead99view', 'Peasant of Manateefield', 'Peasant of Veymaxwych', 'Peasant of Wisseauwyke', 'Peasant of Jazzview', 'Peasant of Ibrahimley', 'Peasant of onewhoistheonestedt', 'Peasant of Afolk', 'Peasant of Xxhampton', 'Peasant of Krysesdorf', 'Peasant of Xychronewick', 'Peasant of Pvtclare', 'Peasant of nalydhampton', 'Peasant of Timstätt', 'Peasant of Fe_manham', 'Peasant of mrcrazyscienceville', 'Peasant of Ginkesschester', 'Peasant of Rport']
    for r in server.roles:
        print(r.name)
        if r.name in delete_plz:
            print(f"delete {r.name}")
            await r.delete()



client.run('discord-token')
