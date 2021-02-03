from pageAction.actionManager import ActionManager


class Login(ActionManager):
    # 成功的登录业务作为其他业务的依赖
    def login_success(self):
        self.pagecover.click_password_login()
        self.pagelogin.input_username('15810263228')
        self.pagelogin.input_password('112233aa')
        # 点击登录按钮
        self.pagelogin.click_login_button()


    # 登录业务--主要测试登录的功能：参数化
    def login_business(self,username,password):
        self.pagecover.click_password_login()
        self.pagelogin.input_username(username)
        self.pagelogin.input_password(password)
        # 点击登录按钮
        self.pagelogin.click_login_button()

    # 断言 点击我的  判断昵称是否在页面源码里面
    def after_login_click_me(self):
        '''
        做断言
        :return:
        '''
        self.pageindex.click_mybutton()