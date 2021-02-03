from base.baseApi import Base
from tools.inihelper import IniHelper


class PageIndex(Base):
    # 点击账号密码登录

    def click_mybutton(self):
        self.base_click(self.source.get_value('doubanLogin.ini', 'Button', '我的'))