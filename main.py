import ArticleGen, HeadlineGen, scraper, time, AIFilter
from datetime import date


def main():
    headlines = scraper.Scrape()
    newsheadlines = [] 
    print(headlines[190])
    for i in range(10):
        newsheadlines.append(HeadlineGen.GenHeadlines(headlines[190]))
    articles = []
    for headline in newsheadlines:
        try:
            article = ArticleGen.GenArticle(headline, date.today())
            articles.append(article)
        except:
            articles.append("Carter: ")
    n = 0
    for a, h in zip(articles, newsheadlines):
        print(h, a)
        if AIFilter.Filter(a, h):
            n += 1
        print(AIFilter.Filter(a, h))
    print(n/10) 

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("-----TIME-----")
    print(end_time - start_time)