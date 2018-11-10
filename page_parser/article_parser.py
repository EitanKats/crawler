import arrow
from lxml.html import HtmlElement

import config
from logger import logger
from models.article import Article


class ArticleParser(object):
    @staticmethod
    def parse_html_to_article(cont: HtmlElement) -> Article:
        try:
            author = cont.cssselect("[class=col-sm-6]")[0].text_content().split('at')[0].split('by')[1].strip()

            title = cont.cssselect("[class='col-sm-5']")[0].text_content().strip()

            content = cont.cssselect("[class=text]")[0].text_content().strip()

            date = arrow.get(cont.cssselect("[class=col-sm-6]")[0].text_content().split('at')[1].strip(),
                             config.ARTICLE_DATE_FORMAT)

            return Article(author, title, content, date)
        except IndexError as e:
            logger.warning(f"Not an article (Error: {str(e)})")
        except Exception as e:
            logger.exception(f'Unknown parsing error occurred: {str(e)}')
