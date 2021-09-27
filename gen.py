import requests, re
from datetime import datetime
from random import randint
from bs4 import BeautifulSoup
import time
import string
import os
from pathlib import Path
import base64
from itertools import cycle
import random

input_menu = int(input(f"1:Minecraft\n2:Crunchyroll\n3:Hulu\n4:NordVPN\n5:IPVanish\n6:その他\n"))
if input_menu == 1:
    input_count = int(input("Genする数を入力してください>>>"))
    input_count -= 1
 
    def findUrl(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]

 
    urls = []
    head = {'gen': ''}

    while not input_count < (sum([1 for _ in open('output\links.txt')])):
        start_time = time.perf_counter()
        with open("output\links.txt", "a") as file:
            file.write(findUrl(requests.post('https://masteralts.com/', data=head).content.decode())[8] + "\n")
        print(findUrl(requests.post('https://masteralts.com/', data=head).content.decode())[8])
        

if input_menu == 2:
    crunchyroll_count = int(input("Genする数を入力してください>>>"))
    crunchyroll_count -= 1
    def findUrl(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]
 
 
    urls = []
    head = {'gen': ''}

    while not crunchyroll_count < (sum([1 for _ in open('output\crunchyroll.txt')])):
        with open("output\crunchyroll.txt", "a") as file:
            file.write(findUrl(requests.post('https://masteralts.com/crunchyroll/', data=head).content.decode())[8] + "\n")
        print(findUrl(requests.post('https://masteralts.com/crunchyroll/', data=head).content.decode())[8])

if input_menu == 3:
    Hulu_count = int(input("Genする数を入力してください>>>"))
    Hulu_count -= 1
    def findUrl(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]
 

    urls = []
    head = {'gen': ''}

    while not Hulu_count < (sum([1 for _ in open('output\hulu.txt')])):
        with open("output\hulu.txt", "a") as file:
            file.write(findUrl(requests.post('https://masteralts.com/hulu/', data=head).content.decode())[8] + "\n")
        print(findUrl(requests.post('https://masteralts.com/hulu/', data=head).content.decode())[8])

if input_menu == 4:
    nord_count = int(input("Genする数を入力してください>>>"))
    nord_count -= 1
    def findUrl(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]
 
    urls = []
    head = {'gen': ''}

    while not nord_count < (sum([1 for _ in open('output\linksnordvpn.txt')])):
        with open("output\linksnordvpn.txt", "a") as file:
            file.write(findUrl(requests.post('https://masteralts.com/nordvpn/', data=head).content.decode())[8] + "\n")
        print(findUrl(requests.post('https://masteralts.com/nordvpn/', data=head).content.decode())[8])

if input_menu == 5:
    vanish_count = int(input("Genする数を入力してください>>>"))
    vanish_count -= 1
    def findUrl(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)      
        return [x[0] for x in url]
 
 
    urls = []
    head = {'gen': ''}

    while not vanish_count < (sum([1 for _ in open('output\ipvanish.txt')])):
        with open("output\ipvanish.txt", "a") as file:
            file.write(findUrl(requests.post('https://masteralts.com/ipvanish/', data=head).content.decode())[8] + "\n")
        print(findUrl(requests.post('https://masteralts.com/ipvanish/', data=head).content.decode())[8])


if input_menu == 6:
    sonota = str(input("Nitro\nまだ未実装\n"))
    if sonota == "Nitro":
        nitro_num = int(input("いくつ生成しますか?>>>"))

with open("output/Nitro Codes.txt", "w", encoding='utf-8') as file:
    print(str(nitro_num) + "コードを記録しました。")

    for i in range(nitro_num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(str(nitro_num) + "コードのチェックを行います。")

with open("output/Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")













        




    

