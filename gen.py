import requests, re
 
 
def findUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
 
urls = []
head = {'gen': ''}
 
while True:
    with open("links.txt", "a") as file:
        file.write(findUrl(requests.post('https://masteralts.com/', data=head).content.decode())[8] + "\n")
    
