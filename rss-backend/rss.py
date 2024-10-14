# Backend for RSS Feed Reader
# Handles RSS Feed Fetching, Translation, and Caching

from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from flask_caching import Cache
import feedparser
from googletrans import Translator
import json
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(
        app,
        resources={r"/*": {"origins": ["http://localhost:3000", "https://nyt-webapp-d825b46890e5.herokuapp.com"]}}
    )

translator = Translator()

cache = Cache(app, config={
        'CACHE_TYPE': 'simple',
        'CACHE_DEFAULT_TIMEOUT': 900
    })

load_dotenv()

# CONFIG_FILE = './config.json'

# def get_config():
#     with open(CONFIG_FILE) as f:
#         return json.load(f)

# config = get_config()
    

from datetime import datetime

# Parse date to format YYYY-MM-DD
def reformat_date(date_string):
    parsed_date = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')
    formatted_date = parsed_date.strftime('%Y-%m-%d')
    return formatted_date

# Translate text to a given language
def translate_text(text, language='es'):
    try:
        translation = translator.translate(text, dest=language).text
        return translation
    except Exception as e:
        print('Exception', e)
        return text

# English RSS feed and RSS processing
@app.route('/rss/en')
@cache.cached(timeout=900)
@cross_origin()
def fetch_rss(lang='en'):
    article_feed = feedparser.parse(os.environ['RSS_URL'])

    # Extract feed metadata
    logo = article_feed.feed.get('image', {}).get('url', 'No logo available')
    title = article_feed.feed.get('title', 'No title available')
    link = article_feed.feed.get('link', '#')
    date = article_feed.feed.get('published', '')

    if lang == 'es':
        title = translate_text(title)
        date = translate_text(date)

    articles = []
    for article in article_feed.entries:
        try:
            # Extract Image and Image metadata
            if 'media_content' in article:
                image_type = article.media_content[0]['medium']
                image_height = article.media_content[0]['height']
                image_width = article.media_content[0]['width']
                image = article.media_content[0]['url']

            # Extract Translated Article Data if necessary
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
                'date': reformat_date(article.get('published', '')),
                'author': author,
                'image' : {
                    'height' : image_height,
                    'width' : image_width,
                    'type' : image_type,
                    'url' : image
                }
            })
        
        except Exception as e:
            print('Error Processing Article: ', e, ' Skipping...')
            continue

    return jsonify({'date': date, 'logo': logo, 'title': title, 'link': link, 'articles': articles})

# Spanish RSS feed
@app.route('/rss/es')
@cache.cached(timeout=900)
@cross_origin()
def fetch_rss_es():
    return fetch_rss('es')

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
