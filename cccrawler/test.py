
#-*- coding: utf-8-*-

from  cccrawler import CCCrawler

if __name__ == '__main__':
    crawler = CCCrawler()

    crawler.save_html()

    crawler.extract_options()

