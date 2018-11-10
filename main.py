import requests
from lxml import html
from urllib3.exceptions import NewConnectionError

import config
from dal.tinydb_accessor import TinyDBAccessor
from logger import logger
from page_parser.article_parser import ArticleParser


def main():
    logger.info('Starting up crawler...')
    try:
        session = requests.session()
        session.proxies = config.PROXIES

        html_element = html.document_fromstring(session.get(config.CRAWL_URL).content)
        article_container = html_element.cssselect("[class=col-sm-12]")
        for article in article_container:
            article = ArticleParser.parse_html_to_article(article)
            if article:
                TinyDBAccessor.insert_article(article.serialize())
    except NewConnectionError as e:
        logger.exception(f'Unable to connect to the website. (Error: {str(e)})')
    except Exception as e:
        logger.exception(f'Unable to run the code. (Error: {str(e)})')


if __name__ == '__main__':
    main()
