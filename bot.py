import matplotlib

import matplotlib.pyplot as plt

import numpy as np
import csv
from csv import reader

xaxis = np.array([0])
yaxis = np.array([0])
import csv
from matplotlib.pyplot import figure
import time
import datetime
from datetime import date
from random import seed
from random import random
import discord
from discord.ext import commands, tasks
import asyncio
from discord.ext import commands
from pathlib import Path
import requests
import json 

#made by Spaffel if you have any Problems contact me on Discord Spaffel#0581





#enter your information here
serverip = "play.spaffel.de"
port = "25565"
bottoken = "your-bot-token"



intents = discord.Intents.default()


client = discord.Client(intents=intents)



client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command("help")


uhrzeiten = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00" ]

figure(figsize=(8, 6), dpi=80)

Uhrzeit = "14"
Datum = "2021-10-10"




@tasks.loop(seconds=240.0)
async def collectdata():
    try:
        print('lol')
        today = date.today()
        timestamp = time.strftime('%H:%M')
    
        headers = {
        "ip": serverip,
        "port": port
            }

        url = 'http://api.spaffel.de:3667/getdata'
        
        s = requests.Session()
        s.headers.update({"ip" : serverip, "port": port })
        response = requests.post(url, headers = headers)

        response = json.loads(response.text)
        
        print(response)
        
        print("The server has {0} players and replied in {1} ms".format(response['players'], response['ping']))
        
        with open('data.csv', 'r', newline='') as file:
            writer = csv.writer(file)
            reader = csv.reader(file)
            print()
            lines= len(list(reader))
    

        fields = [today, timestamp, response['players'], response['ping'], serverip]
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    except Exception as e:
        print(e)
        pass

collectdata.start()





@client.command()
async def pcount(ctx):
    headers = {
    "ip": serverip,
    "port": port
        }

    url = 'http://cloud.spaffel.de:25578/getdata'
    
    s = requests.Session()
    s.headers.update({"ip" : serverip, "port": port })
    response = requests.post(url, headers = headers)

    response = json.loads(response.text)
    players =response['players']
    ping = response['ping']
    print('hhh')
    await ctx.channel.send(f'{players} Players are Online. Ping: {ping}')





def uhrzeitdurch(uhrzeit, Datum):
    with open("data.csv", "r") as csv_file:
        durchschnittmasse = 0
        durchschnittcount = 0
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            s = lines['Uhrzeit']
            s = s[:2]
            print(s)
            if s == uhrzeit:
                print('ich komme bis hier1')
                if str(lines['Datum']) == str(Datum):
                    print('ich komme bis hier2')
                    datumu = lines['Uhrzeit']
                    playercount = lines['playercount']
                    print(datumu)
                    
                    durchschnittcount = durchschnittcount +1
                    durchschnittmasse = durchschnittmasse + int(playercount)

                    print(playercount)
                    durchschnitt = durchschnittmasse//durchschnittcount
                    print(f'durchschnitt: {durchschnitt}')
                    return durchschnitt

def pingdurch(uhrzeit, Datum):
    with open("data.csv", "r") as csv_file:
        durchschnittmasse = 0
        durchschnittcount = 0
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            s = lines['Uhrzeit']
            s = s[:2]
            
            if s == uhrzeit:
               
                if str(lines['Datum']) == str(Datum):
                    
                    datumu = lines['Uhrzeit']
                    playercount = lines['latenz']
                    
                    
                    durchschnittcount = durchschnittcount +1
                    durchschnittmasse = durchschnittmasse + float(playercount)

                    
                    durchschnitt = durchschnittmasse//durchschnittcount
                    
                    return durchschnitt



@client.command()
async def serverstats(ctx):
    try:
        plt.clf()
        #ganzen tag berechnen: 
        xaxis = np.array([0])
        yaxis = np.array([0])
        timestamp = time.strftime('%H')
        today = date.today()
        print(timestamp)
        for uhrzeit in uhrzeiten:
            print(f'uhrzeit = {uhrzeit} datum = {today}')
            try:
                durch = uhrzeitdurch(uhrzeit, today)
                to_append = np.array([uhrzeit])
                xaxis = np.append(xaxis, to_append)
                to_append = np.array([durch])
                yaxis = np.append(yaxis, to_append)
                print(f'uhrzeit: {uhrzeit} durch {durch}')
            except Exception as e:
                print(e)
                pass
        namerandomnum = random()
        filename = f'{Datum} -{namerandomnum}.png'
        plt.plot(xaxis, yaxis)
        plt.savefig(filename)
        await ctx.channel.send('Player-Stats of Today::')
        await ctx.channel.send(file=discord.File(filename))
    except Exception as e:
        print(e)
        pass
    
    try:
        #ganzen tag berechnen: 
        plt.clf()
        timestamp = time.strftime('%H')
        today = date.today()
        print(timestamp)
        xxaxis = np.array([0])
        xyaxis = np.array([0])
        for uhrzeit in uhrzeiten:
            print(f'uhrzeit = {uhrzeit} datum = {today}')
            try:
                durch = pingdurch(uhrzeit, today)
                to_append = np.array([uhrzeit])
                xxaxis = np.append(xxaxis, to_append)
                to_append = np.array([durch])
                xyaxis = np.append(xyaxis, to_append)
                print(f'uhrzeit: {uhrzeit} durch {durch}')
            except Exception as e:
                print(e)
                pass
        namerandomnum = random()
        filename = f'{Datum} -{namerandomnum}.png'
        plt.plot(xxaxis, xyaxis)
        plt.savefig(filename)
        await ctx.channel.send('Ping-Stats of Today:')
        await ctx.channel.send(file=discord.File(filename))
    except Exception as e:
        print(e)
        pass







    


        



client.run(bottoken)


            




