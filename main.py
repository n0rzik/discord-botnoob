#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
from discord.interactions import Interaction
import discord
from discord.ext import commands
from discord.ui import Button, View
@@ -32,5 +32,28 @@ async def on_member_join(member):
    emb = discord.Embed(title='Добро пожаловать в RedanTM', color=0x8b61cf).set_footer(text="RedanTM").add_field(name='Команды бота', value='Чтоб узнать все команды бота пропиши !help')
    await member.send(embed = emb)

'''
Create n0rzik
Удоления сообщений и команд
'''
@client.command(pass_context = True)
@commands.hat_permissions(administrator = True)

async def clear(ctx, amount = 1):
    await ctx.channel.purge ( limit = amount)

'''
Create n0rzik
Кик пользователя
'''
@client.command(pass_context = True)
@commands.hat_permissions(administrator = True)

async def kick ( ctx, member: discord.member, *, reason = None): # Кик участника в ДИСКОРД СЕРВЕРЕ где находиться бот и т.д
    await ctx.channel.purge ( limit = 1)

    await member.kick ( reason = reason)
    await ctx.send(f'Kick user {member.mention}')

#Токен бота
bot.run(config.bot_token)
