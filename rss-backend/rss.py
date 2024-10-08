from flask import Flask, jsonify, render_template
from flask_cors import CORS
import feedparser

app = Flask(__name__)
CORS(app)

RSS_URL = 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'

@app.route('/rss')
def fetch_rss():
    article_feed = feedparser.parse(RSS_URL)

    logo = article_feed.feed.image.url
    title = article_feed.feed.title
    link = article_feed.feed.link

    articles = []
    for article in article_feed.entries:
        if 'media_content' in article:
            image_type = article.media_content[0]['medium']
            image_height = article.media_content[0]['height']
            image_width = article.media_content[0]['width']
            image = article.media_content[0]['url']
        
        articles.append({
            'title': article.title,
            'link': article.link,
            'description': article.description,
            'date': article.get('published', ''),
            'author': article.get('author', ''),
            'image' : {
                'height' : image_height,
                'width' : image_width,
                'type' : image_type,
                'url' : image
            }
        })

    return jsonify({'logo': logo, 'title': title, 'link': link, 'articles': articles})

@app.route('/')
def index():
    return render_template('tester.html')

if __name__ == '__main__':
    app.run(debug=True)
