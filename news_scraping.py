import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from sentiment_analysis import test_model

def sentiment_analysis(inputHeadlines):
    newsArray = []
    for headline in inputHeadlines:
        print(headline)
        individualSentiment = test_model(headline)
        newsArray.append(individualSentiment)
    return newsArray

def sentiment_score(newsArray):
    total_sentiment = 0
    for headline in newsArray:
        if headline[1] == 'Positive':
            total_sentiment += headline[2]
        elif headline[1] == 'Negative':
            total_sentiment -= headline[2]
    print("TOTAL SENTIMENT: " + str(total_sentiment))

urls = ['https://www.theguardian.com/uk', 'https://www.bbc.co.uk/news']
number_of_articles = 10

for url in urls:
    print(url)

    if url == 'https://www.bbc.co.uk/news':
        list_titles = []
        headlineCount = 0
        response = requests.get('http://www.bbc.co.uk/news')
        doc = BeautifulSoup(response.text, 'html.parser')
        headlines = doc.find_all('h3')
        for headline in headlines:
            #First two articles are always the same for BBC
            if 1 < headlineCount < number_of_articles + 2:
                list_titles.append(headline.text)
            headlineCount+=1

        bbcArray = sentiment_analysis(list_titles)
        print (bbcArray)
        sentiment_score(bbcArray)





    elif url == 'https://www.theguardian.com/uk':
        upperframe = []

        try:
            # use the browser to get the url. This is suspicious command that might blow up.
            page = requests.get(url)
        except Exception as e:  # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()  # get the exception information
            print('ERROR FOR LINK:', url)  # print the link that cause the problem
            print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
        time.sleep(2)

        soupText = BeautifulSoup(page.text, 'html.parser')

        coverpage_news = soupText.find_all('h3', class_='fc-item__title')

        # Empty lists for content, links and titles
        news_contents = []
        list_links = []
        list_titles = []

        for n in np.arange(0, number_of_articles):
            # We need to ignore "live" pages since they are not articles
            if "live" in coverpage_news[n].find('a')['href']:
                continue

            # Getting the link of the article
            link = coverpage_news[n].find('a')['href']
            list_links.append(link)

            # Getting the title
            title = coverpage_news[n].find('a').get_text()
            list_titles.append(title)

        guardianArray = sentiment_analysis(list_titles)

with open('./data/08_news_data.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file, delimiter=',', quotechar='”', quoting=csv.QUOTE_MINIMAL)
        for i in range(number_of_articles):
            csv_write.writerow([guardianArray[i][0], guardianArray[i][1], guardianArray[i][2], bbcArray[i][0], bbcArray[i][1], bbcArray[i][2]])





