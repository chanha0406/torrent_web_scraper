from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import ssl
from tenacity import retry, stop_after_attempt

class WebDelegate:
    def __init__(self, parser_engine=BeautifulSoup):
        #TO-DO: default parser engine은 BeautifulSoup. 필요시 추가.
        self.__parser_engine=parser_engine

    @retry(stop=stop_after_attempt(10))
    def get_web_data(self, addr):
        print(f"get web data {addr}")
        req = Request(addr, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req, timeout = 3, context=ssl.SSLContext()).read().decode('utf-8','replace')
        data = self.__parser_engine(html, "html.parser")
        return data

    @retry(stop=stop_after_attempt(10))
    def check_url_alive(self, addr):
        try:
            print(f"check {addr}")
            req = Request(addr, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req, timeout = 3, context=ssl.SSLContext())
            if html.status >= 300: # 3xx Redirection부터 에러 처리
                return False
            self.get_web_data(addr)
        except Exception as e:
            print("Exception access url : %s" % e)
            print("We can not scrap %s, something wrong.\n" % addr)
            return False

        return True
