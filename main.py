from newsapi import NewsApiClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from summarizer import text_summarizer
from tokenconfig import TOKEN

def news_finder():
    sources = 'associated-press,reuters'

    top_headlines = newsapi.get_top_headlines(sources=sources, language='en')
    top_headlines = top_headlines['articles']
    return top_headlines

def summarizer():
    total_articles = []

    articles = news_finder()
    for article in articles:
        source_name = article['source']['name']
        article_title = article['title']
        article_url = article['url']
        article_summary = text_summarizer(article_url)
        article_contents = "Title: {} \nURL: {} \nSummary: {}".format(article_title, article_url, article_summary)
        total_articles.append(article_contents)

    return total_articles

def send_email(email_body):
    # The contents of email to be sent
    fromaddr = 'scriptingfortech@gmail.com'
    toaddr = 'yonghao.choo@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['X-Priority'] = '3'
    msg['Subject'] = 'Daily Top News Headlines'
    body = '\n\n'.join(str(x) for x in email_body)
    msg.attach(MIMEText(body, 'plain'))

    # Setting up gmail to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'scripting1234**')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def main():
    email_body = summarizer()
    send_email(email_body)

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key='ed148100f1aa4950a86b05a0699004d0')

    main()