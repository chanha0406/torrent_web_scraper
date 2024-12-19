from datetime import datetime as dtime
from utils.title_checker import Item

class MagnetInfo():
    def __init__(self, title: str, magnet: str, matched_item: Item,  sitename=None):
        self.create_time = dtime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sitename = sitename
        self.title = title
        self.magnet = magnet
        self.matched_item = matched_item

    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.create_time, self.sitename,
                self.title, self.magnet, self.matched_item)

    def get_list(self):
        return [self.create_time, self.sitename, self.title, self.magnet, self.matched_item]
