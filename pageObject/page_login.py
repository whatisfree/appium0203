from base.baseApi import Base
from tools.inihelper import IniHelper


class PageLogin(Base):
    # 输入账号
    def input_username(self,username):
        self.base_input(self.source.get_value('doubanLogin.ini','TextInput','用户名'),username)
    # 输入密码
    def input_password(self,password):
        self.base_input(self.source.get_value('doubanLogin.ini','TextInput','密码'),password)
    # 点击登录
    def click_login_button(self):
        self.base_click(self.source.get_value('doubanLogin.ini','Button','登录按钮'))