import requests as req
from bs4 import BeautifulSoup as bs
import json

sources = req.get('https://news.google.com/rss/search?q=%7Bcoronavirus%7D&hl=en-NG&gl=NG&ceid=NG:en')
jsonFile = []
def extract():
    soup = bs(sources.text, features='lxml')
    items = soup.find_all('item')
    for item in items:
        article_title = item.title.string
        article_link = item.link.next_sibling
        publish_date = item.pubdate.string
        description = get_desc(item.description)
        source = item.source.next_sibling
        source_link = get_link(item)

        jsonFile.append({
            'article_title': article_title,
            'article_link' : article_link,
            'publish_date' : publish_date,
            'description' : description,
            'source' : source,
            'source_link' : source_link
        })
    with open('jsonFile.js', 'w') as outFile:
        json.dump(jsonFile, outFile)
    return jsonFile

def get_desc(item):
    soup = bs(item.string, features='lxml')
    description = soup.find('a')
    return description.string

def get_link(item):
    return (item.source.get('url'))



