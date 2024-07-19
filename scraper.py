import requests, utils
from bs4 import BeautifulSoup as bs4


nono = ["Letter Boxed", "The Crossword", "Spelling Bee", "Digits | Beta", "Today’s Wordle Review", "Wordle", "Fox News @ Night - Friday, May 26", "Fox News Tonight - Friday, May 26", "Hannity - Friday, May 26", "The Ingraham Angle - Friday, May 26"]
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
   
def NYTScrape() -> list():
        res = requests.get("https://www.nytimes.com/").text
        soup = bs4(res, "html.parser")
        elements = soup.find_all(lambda tag: tag.has_attr('class') and 'css-xdandi' in tag['class'])
        articles = []
        for elem in elements:
            if elem.text in nono:
                pass
            else:
                articles.append(elem.text)
        return articles

def WSJScrape() -> list():
    res = requests.get("https://www.wsj.com/", headers=headers).text
    soup = bs4(res, "html.parser")
    elements = soup.find_all("span", class_=lambda x: x and "WSJTheme--headlineText--" in x)
    articles = []
    for elem in elements:
        articles.append(elem.text)
    return articles

def FoxScrape() -> list():
    res = requests.get("https://www.foxnews.com/", headers=headers).text
    soup = bs4(res, "html.parser")
    elements = soup.find_all("h3", class_="title")
    articles = []
    for elem in elements:
        e = elem.find_all("a")
        for i in e:
            if i.text not in nono:
                articles.append(i.text)
    return articles

def Scrape() -> list():
    articles = []
    articles.append(WSJScrape())
    articles.append(NYTScrape())
    articles.append(FoxScrape())
    print(len(utils.flatten_list(articles)))
    return utils.flatten_list(articles)

if __name__ == "__main__":
    print(Scrape()[3])