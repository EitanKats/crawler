from arrow import Arrow

import config


class Article(object):
    def __init__(self, author: str, title: str, content: str, date: Arrow):
        self.author = author
        if author.lower() in config.FORBIDDEN_USERS:
            self.author = None
        self.title = title
        self.content = content
        self.date = date

    def __str__(self):
        return self.author

    def serialize(self) -> dict:
        return {
            'author': self.author,
            'date': self.date.isoformat(),
            'title': self.title,
            'content': self.content
        }
