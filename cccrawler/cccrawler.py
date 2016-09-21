
#-*- coding: utf-8-*-
import configparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

class CCCrawler(object):
    def __init__(self):
        self.config = configparser.ConfigParser()        
        self.config.read('config.ini')
        self.url = self.config['DEFAULT']['URL']
        #print(self.url)

        self.page = urlopen(self.url).read()
        self.soup = BeautifulSoup(self.page, 'lxml')
        
    def save_html(self):
        f = open('temp.html', mode='w', encoding='utf-8')
        f.write(self.soup.prettify())
        f.close()

    def get_index(self, soup, name):
        index = 0
        for div in soup('div', {'class":"section',}):
            try:
                if div.h2.text == name:
                    return index
                else:
                    index += 1
            except:
                index += 1
        return 0

    def get_div(self, soup, name):
        for div in soup('div', {'class':'section',}):
            try:
                if div.h2.text == name:
                    return div
                else:
                    pass
            except:
                pass
        return None

    def extract_options(self):
        #index_des = self.get_index(self.soup, 'Description');
        #print(index_des)
        #index_opt = self.get_index(self.soup, 'Options')
        #print(index_opt)
        div_opt = self.get_div(self.soup, 'Options')
        #print(div_opt)

        for dt, dd in zip(div_opt.find_all('dt'), div_opt.find_all('dd')):
            if 'cvda' in dt.text:
                print(dt.text)
                for dt in dd.find_all('dt'):
                    print(dt.text)
            else:
                print(dt.text)
