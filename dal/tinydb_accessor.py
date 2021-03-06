from tinydb import TinyDB, Query

import config
from logger import logger

db = TinyDB(config.DATABASE_PATH, default_table=config.TABLE_NAME)
article_record = Query()


class TinyDBAccessor(object):
    latest_insert = None

    @staticmethod
    def insert_article(serialized_article):

        # check whether it was already in the db or not
        try:
            if not db.contains(article_record.title == serialized_article.get('title')):
                db.insert(serialized_article)
        except Exception as e:
            logger.exception(f"Issues encountered while accessing the DataBase : (Error: {str(e)})")
