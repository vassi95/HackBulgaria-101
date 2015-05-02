import requests
from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt


class Histogram:

    def __init__(self):
        self.dict = {}

    def add(self, name):
        if name not in self.dict:
            self.dict[name] = 1
        else:
            self.dict[name] += 1

    def count(self, namee):
        if namee not in self.dict.keys():
            return None
        return self.dict[namee]

    def get_dict(self):
        return self.dict

    def make_histogram(self, name):
        with open(name, "r") as f:
            content = f.readlines()
            for line in content:
                if "nginx" in line:
                    self.add("nginx")
                if "Apache" in line:
                    self.add("Apache")
                if "IIS" in line:
                    self.add("IIS")
                if "lighttpd" in line:
                    self.add("lighttpd")
        keys = list(self.dict.keys())
        a = list(range(len(keys)))
        plt.bar(a, list(self.dict.values()), align = 'center')
        plt.xticks(a, keys)
        plt.title("All .bg servers")
        plt.savefig("histogram.png")


class Get_links:

    def __init__(self):
        pass

    def links(self):
        masiv = []
        strr = "link.php"
        url = "http://register.start.bg/"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        sites = soup.find_all('a')
        for href in sites:
            a = (href.get("href"))
            if strr in str(a):
                masiv.append(href.get("href"))
        """for i in masiv:
            print(i)"""
        return masiv

    def make_request(self, new_list):
        for i in new_list:
            try:
                r = requests.get("http://register.start.bg/" + i, timeout=3)
                print(r.headers['server'])
                self.to_file("servers.txt", r.headers['server'])
            except:
                print("Not valid url")

    def to_file(self, filename, names):
        with open(filename, "a+") as f:
            f.write(names + "\n")


a = Get_links()
h = Histogram()
h.add("Apache")
h.add("Apache")
h.add("nginx")
h.add("IIS")
h.add("nginx")
print(h.count("Apache") == 2)  # True
print(h.count("nginx") == 2)  # True
print(h.count("IIS") == 1)  # True
print(h.count("IBM Web Server") == None)  # True

if __name__ == '__main__':
    a.make_request(a.links())

    h.make_histogram("servers.txt")
