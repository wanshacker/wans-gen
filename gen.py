import requests, re
from datetime import datetime


input_menu = int(input(f"Menu\n1:Minecraft\n2:Crunchyroll\n3:Hulu\n4:NordVPN\n5:IPVanish\n"))
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




    

