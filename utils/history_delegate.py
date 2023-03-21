import csv
import os.path
import re

class HistoryDelegate:
    def __init__(self, historyFile):
        self.__csv_file = historyFile

        #if not os.path.isfile(self.__csv_file):
        if not self.__exist_history_file():
            try:
                open(self.__csv_file, 'x')
            except:
                print("HistoryDelegate: __init__ Exception!!")

    def __exist_history_file(self):
        if os.path.isfile(self.__csv_file):
            return True
        return False

    def check_magnet_history(self, magnet):
        if not self.__exist_history_file():
            return False

        with open(self.__csv_file, 'r', encoding="utf-8") as f:
            ff = csv.reader(f)
            for row in ff:
                if magnet == row[3]:
                    print("Fail to add magnet for [%s] which was already downloaded." % row[2])
                    return True
        return False

    def __check_data(self, title, data):
        if data is None:
            return False
        if data in title.lower():
            return True

        return False

    def __check_duplicate(self, season, ep, date, res, history_title):

        res = False

        if season:
            if self.__check_data(history_title, ep) and self.__check_data(history_title, season):
                res = True

            if self.__check_data(history_title, date):
                res = True
        else:
            if self.__check_data(history_title, ep):
                res = True

            if self.__check_data(history_title, date):
                res = True

        if res == "1080p" and re.search("720[pP]", history_title):
            res = False

        return res

    def check_title_history(self, title, matched_name):
        if not self.__exist_history_file():
            return False

        season = re.search("[sS][0-9]+", title)
        season = season.group().lower() if season else None

        ep = re.search("[eE][0-9]+", title)
        ep = ep.group().lower() if ep else None

        date = re.search("[0-9]{6}", title)
        date = date.group() if date else None

        res = re.search("[0-9]{3,4}[pP]", title)
        res = res.group().lower() if res else None

        with open(self.__csv_file, 'r', encoding="utf-8") as f:
            ff = csv.reader(f)
            for row in ff:
                if " ".join(matched_name.title) in row[2]:
                    if self.__check_duplicate(season, ep, date, res, row[2]):
                        print("Fail to add magnet for [%s] which was duplicated." % row[2])
                        return True
        return False

    def add_magnet_info_to_history(self, magnet_story):
        "magnet_story는 magnet 정보를 담은 list"
        with open(self.__csv_file, 'a', newline = '\n', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(magnet_story)
        f.close()
        return

