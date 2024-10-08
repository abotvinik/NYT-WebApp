from flask import Flask, jsonify, render_template
from flask_cors import CORS
import feedparser
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

RSS_URL = 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'

def translate_text(text):
    try:
        translation = translator.translate(text, dest='es').text
        return translation
    except Exception as e:
        print('Exception', e)
        return text

@app.route('/rss/en')
def fetch_rss(lang='en'):
    article_feed = feedparser.parse(RSS_URL)

    logo = article_feed.feed.image.url
    title = article_feed.feed.title
    link = article_feed.feed.link
    date = article_feed.feed.published

    if lang == 'es':
        title = translate_text(title)
        date = translate_text(date)

    articles = []
    for article in article_feed.entries:
        if 'media_content' in article:
            image_type = article.media_content[0]['medium']
            image_height = article.media_content[0]['height']
            image_width = article.media_content[0]['width']
            image = article.media_content[0]['url']

        if lang == 'es':
            title = translate_text(article.title)
            description = translate_text(article.description)
            author = article.author.replace(' and ', ' y ')
        else:
            title = article.title
            description = article.description
            author = article.author
        
        articles.append({
            'title': title,
            'link': article.link,
            'description': description,
            'date': article.get('published', ''),
            'author': author,
            'image' : {
                'height' : image_height,
                'width' : image_width,
                'type' : image_type,
                'url' : image
            }
        })

    return jsonify({'date': date, 'logo': logo, 'title': title, 'link': link, 'articles': articles})

@app.route('/rss/es')
def fetch_rss_es():
    return fetch_rss('es')

@app.route('/')
def index():
    return render_template('tester.html')

if __name__ == '__main__':
    app.run(debug=True)
