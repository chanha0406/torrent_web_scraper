from datetime import datetime as dtime
from utils.title_checker import Item


class MagnetInfo:
    def __init__(self, title: str, magnet: str, matched_item: Item, site_name=None):
        self.create_time = dtime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.site_name = site_name
        self.title = title
        self.magnet = magnet
        self.matched_item = matched_item

    def __repr__(self):
        return f"{self.create_time}, {self.site_name}, {self.title}, {self.magnet}, {self.matched_item}"

    def get_list(self):
        return [
            self.create_time,
            self.site_name,
            self.title,
            self.magnet,
            self.matched_item,
        ]
