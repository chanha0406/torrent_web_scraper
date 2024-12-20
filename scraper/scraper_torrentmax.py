from scraper.scraper import ScraperTemplate
import re


class ScraperTorrentmax(ScraperTemplate):
    def __init__(
        self, scraper_configuration_file, local_machine_status_file, local_machine_history_file
    ):
        site_name = "torrentmax"
        super().__init__(
            site_name,
            scraper_configuration_file,
            local_machine_status_file,
            local_machine_history_file,
        )

    def parse_page_data(self, url):
        bs_obj = self.web_delegate.get_web_data(url)
        # name_list = bs_obj.find('ul', attrs={'class' : 'list-body'}).find_all('a', href=re.compile(".*page.*"))
        _ = bs_obj.find("ul", attrs={"class": "list-body"})
        _list = _.find_all("div", attrs={"class": "wr-subject"})

        name_list = []
        for item in _list:
            a_tag = item.find("a", href=re.compile(".*page.*"))
            title = a_tag.get_text().strip()
            href = a_tag["href"]

            # name_list는 title과 href 리스트의 리스트로 구성
            name_list.append([title, href])

        return name_list

    def parse_magnet_from_page_url(self, url):
        bs_obj = self.web_delegate.get_web_data(url)
        magnet = None
        if not bs_obj == None:
            magnet_item = bs_obj.find("a", href=re.compile(".*magnet.*"))
            if not magnet_item == None:
                magnet = magnet_item.get("href")

        return magnet

    def parse_magnets_from_page_url(self, base_url, title):
        return []

    @staticmethod
    def get_board_id_num(url):
        """id num을 가져오는 방법은 사이트 별로 다르니 잘 기록해둘 것."""
        """ ex. https://torrentmax2.com/max/VARIETY/18966?page=1 """
        check_str = "com/max"
        tmp = url.rfind(check_str)

        if tmp < 0:  # 검색 못하면 포기
            return 0
        else:
            _ = url.split(check_str)[1]  # split 뒷 부분이 필요함
            split_list = re.split(r"\/|\?", _)
            for item in split_list:
                if item.isdigit():
                    return int(item)

        return 0
