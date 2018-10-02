from tokenconfig import TOKEN

def news_finder():
    sources = 'associated-press,reuters'
    pageSize = 10

    top_headlines = newsapi.get_top_headlines(sources=sources, language='en', pageSize=pageSize)
    return top_headlines

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key=TOKEN)