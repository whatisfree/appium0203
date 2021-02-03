from pageObject.page_cover import PageCover
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin


class ActionManager:
    def __init__(self,driver):
        self.pagecover = PageCover(driver)
        self.pageindex=PageIndex(driver)
        self.pagelogin = PageLogin(driver)