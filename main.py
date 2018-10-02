from newsapi import NewsApiClient

from summarizer import text_summarizer
from tokenconfig import TOKEN

def news_finder():
    sources = 'associated-press,reuters'

    top_headlines = newsapi.get_top_headlines(sources=sources, language='en')
    top_headlines = top_headlines['articles']
    return top_headlines

def summarizer(url):
    total_articles = []

    articles = news_finder()
    for article in articles:
        source_name = article['source']['name']
        article_title = article['title']
        article_url = article['url']
        article_summary = text_summarizer(article_url)
        article_contents = "Title: {} \nURL: {} \nSummary: {} \n\n".format(article_title, article_url, article_summary)
        total_articles.append(article_contents)

    return total_articles

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key=TOKEN)

    print(summarizer())