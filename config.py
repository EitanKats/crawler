import os

PROXY_PORT = 9150

PROXIES = {'http': 'socks5h://localhost:{0}'.format(PROXY_PORT),
           'https': 'socks5h://localhost:{0}'.format(PROXY_PORT)}

DOCKER_HOST = os.getenv('DOCKER_HOST')
if DOCKER_HOST:
    PROXIES = {'http': 'socks5h://{0}:{1}'.format(DOCKER_HOST, PROXY_PORT),
               'https': 'socks5h://{0}:{1}'.format(DOCKER_HOST, PROXY_PORT)}

FORBIDDEN_USERS = ['anonymous', 'guest', 'unknown']

CRAWL_URL = 'http://nzxj65x32vh2fkhk.onion/all'

ARTICLE_DATE_FORMAT = 'DD MMM YYYY, HH:mm:ss'

DATABASE_PATH = 'data/articles.json'

TABLE_NAME = 'articles'
