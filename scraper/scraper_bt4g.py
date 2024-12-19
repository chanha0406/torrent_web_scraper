from scraper.scraper import ScraperTemplate
import re
from urllib import parse


class ScraperBT4G(ScraperTemplate):
    def __init__(
        self, scraper_configuration_file, local_machine_status_file, local_machine_history_file
    ):
        site_name = "bt4g"
        super().__init__(
            site_name,
            scraper_configuration_file,
            local_machine_status_file,
            local_machine_history_file,
        )

    def parse_magnets_from_page_url(self, base_url, item):
        dir_name, queries, resolutions, releases = item
        magnet_list = []
        
        for title in queries:
            url = f"{base_url}/search?q={title}&page=rss&orderby=time"
            url = parse.urlparse(url)
            query = parse.parse_qs(url.query)
            result = parse.urlencode(query, doseq=True)
            url = url._replace(query=result)
            bs_obj = self.web_delegate.get_web_data(url.geturl())
            item_list = bs_obj.find_all("item")

            for rss_item in item_list:
                rss_item_title = rss_item.find("title").get_text()
                magnet_list.append((rss_item_title, re.search("<link/>(.*)<guid", str(rss_item))[1]))

        return magnet_list

    def parse_page_data(self, url):
        return

    def parse_magnet_from_page_url(self, url):
        return

    @staticmethod
    def get_board_id_num(url):
        return ""
