from crawler import Crawler
import json
from database import Database
from histogram import Histogram
import matplotlib.pyplot as plt
import sqlite3


def make_urls(filename, url):

    crawler = Crawler()
    soup_box = crawler.get_urls(url)
    crawler.get_links(soup_box)
    for url in crawler.internal_links:
        soup_box = Crawler.get_urls(url)
        crawler.get_links(soup_box)
    with open(filename, 'w') as new:
        json.dump(crawler.links, new, indent=4)



def load_urls(filename):
    with open(filename) as data_file:
        return json.load(data_file)


def complete_histogram(histogram, servers):
    for line in servers:
        histogram.add(line['server'])


def main():
    histogram = Histogram()
    db = Database('mydb-servers')
    cursor = db.cursor()
    sizes = []
    serverss = [('Apache',), ('nginx',), ('IIS',), ('lighttpd',), ('Other',)]
    for server in serverss:
        print(server)
        result = cursor.execute(
        """SELECT server FROM urls WHERE server = ?""", server)
        into_list = result.fetchall()
        sizes.append(into_list.count(server))
    colors = ['blues', 'green', 'yellow', 'orange']
    plt.pie(sizes, explode=None, serverss=serverss, colors=colors,
    autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.savefig("histogram.png")


if __name__ == '__main__':
    url = 'http://start.bg/'
    make_urls('all_urls.json', url)
    urls = load_urls('all_urls.json')
    Crawler.get_servers(urls, db)
    main()
