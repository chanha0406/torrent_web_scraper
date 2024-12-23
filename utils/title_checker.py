from local_config.program_list import title_list

class Item:
    def __init__(self, dir_name, title, resolutions, releases):
        self.dir_name = dir_name
        self.title = title.strip().lower().split(" ")
        self.resolutions = resolutions
        self.releases = releases

    def __repr__(self):
        return f"{' '.join(self.title)} with {self.resolutions} from {self.releases} in {self.dir_name}"

class TitleChecker:
    def __init__(self):
        self.__list = []

        for info in title_list:
            dir_name, queries, resolutions, releases = info
            self.__list.append(Item(dir_name, dir_name, resolutions, releases))
            for title in queries:
                self.__list.append(Item(dir_name, title, resolutions, releases))

    def validate_board_title(self, board_title) -> Item | bool:
        "board_title string 값이 요청한 목록에 존재하는지 확인"
        board_title = board_title.lower()

        candidate = self.__validate_title(board_title)
        if not candidate:
            return False

        ret = self.__validate_resolution(board_title, candidate)
        if not ret:
            return False

        ret = self.__validate_release(board_title, candidate)
        if not ret:
            return False

        return candidate

    def __validate_title(self, board_title):
        "valid이면 valid한 대상의 item을 반환, 아니면 False를 반환"
        for iterator in self.__list:
            candidate_title_list = iterator.title
            matched = True
            for temp in candidate_title_list:
                temp = temp.lower()
                if not temp in board_title:
                    matched = False
                    break
            if matched:
                return iterator

        return False

    @staticmethod
    def __validate_resolution(board_title, candidate_item):
        """board_title에서 resolution을 검색해야 하므로, 해당하는
        item 정보(=class)가 필요함"""
        if candidate_item.resolutions[0] is None:
            return True

        for temp in candidate_item.resolutions:
            if temp in board_title:
                return True
        return False

    @staticmethod
    def __validate_release(board_title, candidate_item):
        """board_title에서 release을 검색해야 하므로, 해당하는
        item 정보(=class)가 필요함"""
        if candidate_item.releases[0] is None:
            return True

        for temp in candidate_item.releases:
            temp = temp.lower()
            if temp in board_title:
                return True
        return False
