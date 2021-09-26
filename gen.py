import requests, re

input_count = int(input("Genする数を入力してください>>>"))
input_count -= 1
 
def findUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
 
urls = []
head = {'gen': ''}



while not input_count < (sum([1 for _ in open('links.txt')])):
    with open("links.txt", "a") as file:
        file.write(findUrl(requests.post('https://masteralts.com/', data=head).content.decode())[8] + "\n")

