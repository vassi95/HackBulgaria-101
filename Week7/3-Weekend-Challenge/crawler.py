import requests
from bs4 import BeautifulSoup
import json


class Crawler:

    def __init__(self):
        self.internal_links = []
        self.links = []
        self.start_page = "http://www.start.bg/"

    def get_urls(url):
        response = requests.get(url, timeout=1, allow_redirects=True)
        soup = BeautifulSoup(response.text)
        return soup

    def get_links(self, soup):
        links = set()
        internal_links = set()
        for link in soup.find_all('a'):
            link = str(link.get('href'))
            check = 'javascript' not in link and 'None' not in link and not link.startswith('#')
            if check==True:
                if 'start.bg' in link:
                    self.interal_links.append(link)
                elif 'link.php?' in link or link.startswith('/'):
                    self.links.append(self.start_page + link)
        self.links = list(set(self.links))
        self.internal_links = list(set(self.internal_links))
        return [self.links, self.internal_links]

    def get_servers(link):
        server = ""
        try:
            response = requests.head(link, timeout=1, allow_redirects=True)
            if "Server" in response.headers:
                server = response.headers["Server"]
        except:
            pass
        return server


    def save_in_file(file, data):
        with open(filename, 'w') as f:
            json.dump(data, f)

