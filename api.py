import json
from urllib.parse import quote
from flask import Flask, request, abort
from flask_cors import CORS
from newspaper import Article

app = Flask(__name__)
cors = CORS(app)

# API /parse

@app.route('/parse', methods=['GET'])
def parse():
  doc = parse_article(request.args.get('url', ''))
  return json.dumps(doc)

# Content extraction using newspaper

def parse_article(url):
  print('fetch %s' % url)

  a = Article(url=url, keep_article_html=True)
  a.download()

  try:
    a.parse()
  except Exception:
    exc = traceback.format_exc()
    print ('Parse error: %s' % exc)

  # newspaper gives us some news stuff
  article_data = {
    "url": url,
    "title": a.title,
    "text": a.text
  }

  return article_data
