import requests
from bs4 import BeautifulSoup
import time
import sys

def get_cards(url, timeToWait):
    addLinks = False
    print(timeToWait)
    pageNumber = 1
    cards = []
    nextFound = True
    while nextFound:
        print("Page Number: ", pageNumber)
        nextFound = False
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href is not None:
                if not nextFound and "&page=" + str(pageNumber+1) in href:
                    pageNumber += 1
                    url = 'https://scryfall.com' + href
                    nextFound = True
                if "https://scryfall" in href:
                    time.sleep(int(timeToWait))
                    newResponse = requests.get(href)
                    soup = BeautifulSoup(newResponse.text, 'html.parser')
                    og_title_tag = soup.find('meta', property='og:title')
                    og_title = og_title_tag['content'] if og_title_tag and 'content' in og_title_tag.attrs else None 
                    if '//' in og_title:
                        og_title = og_title.split("//")[0][:-1]
                    setTag = soup.find('meta', property='og:url')
                    og_set = setTag['content'] if setTag and 'content' in setTag.attrs else None
                    og_set = og_set.split("/")
                    print(og_title + " [" + og_set[4] + "] " + og_set[5])
                    cards.append(og_title + " [" + og_set[4] + "] " + og_set[5])
    return cards
if len(sys.argv) == 1:
    print("Please define search URL after py scryfallToTCGMassEntry.py")
    sys,exit(1)
elif len(sys.argv) == 2:
    url = sys.argv[1]
    timeToWait = 3
elif len(sys.argv) == 3:
    url = sys.argv[1]
    timeToWait = sys.argv[2]
all_cards = get_cards(url, timeToWait)
file_path = "output.txt"
with open(file_path, 'w') as file:
    for card in all_cards:
        file.write("1 " + card + "\n")
file.close()