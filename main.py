import requests
from lxml import html

import config
from page_parser.article_parser import ArticleParser
from dal.tinydb_accessor import TinyDBAccessor


def main():
    session = requests.session()
    session.proxies = config.PROXIES

    html_element = html.document_fromstring(session.get(config.CRAWL_URL).content)
    article_container = html_element.cssselect("[class=col-sm-12]")
    for article in article_container:
        article = ArticleParser.parse_html_to_article(article)
        if article:
            TinyDBAccessor.insert_article(article.serialize())


if __name__ == '__main__':
    main()
