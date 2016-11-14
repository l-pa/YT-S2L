import urllib
import argparse
import time
from pathlib import Path
from urllib.request import urlopen
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", type=str, help="Source file TXT")
parser.add_argument("-o", "--output", action='store_true', help='Output file')
args = parser.parse_args()


lines = [line.rstrip('\n') for line in open(args.source)]

print(lines)
my_file = Path("YT_S2L.txt")
if my_file.is_file():
    f = open('YT_S2L.txt', 'a')
    f.write('\n'+ time.strftime("%c" + '\n'))
    f.write('\n')
    f.close()

if args.output:
    for text in lines:
        textToSearch = text
        query = urllib.parse.quote(textToSearch)

        url = "https://www.youtube.com/results?search_query=" + query
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        pls = (soup.find(attrs={'class': 'yt-uix-tile-link'}))
        with open('YT_S2L.txt', 'a') as out:
            out.write('https://www.youtube.com' + pls['href'] + '\n')
else:
    for text in lines:
        textToSearch = text
        query = urllib.parse.quote(textToSearch)

        url = "https://www.youtube.com/results?search_query=" + query
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        pls = (soup.find(attrs={'class': 'yt-uix-tile-link'}))
        print(text + ' ' + 'https://www.youtube.com' + pls['href'])
