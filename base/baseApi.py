'''
logger 正常描述 logger.info()
异常处理  logger.error()
'''
from tools.inihelper import IniHelper
from tools.logger import GetLogger
logger = GetLogger().get_logger()
class Base:
    def __init__(self, driver):
        # driver
        self.driver = driver
        self.source = IniHelper()

    def base_find_element(self,loc):
        '''
        loc = xpath=>//android.widget.TextView[@text='我的']
        字符串的类型
        :param loc:
        :return: 定位到的元素
        '''
        element=''
        ele_type = loc.split('=>')[0]
        value = loc.split('=>')[1]
        if ele_type == '' or value=="":
            logger.error('grammatical error,eg:"id=>name"')
            raise NameError('grammatical error,eg:"id=>name"')
        if ele_type == 'id':
            try:
                element = self.driver.find_element_by_id(value)
                logger.info('had find element{},by {} via value{}'.format(element.text,ele_type,value))
            except Exception as e:
                logger.error('定位方式有错误:%s' %e)
        elif ele_type == 'name':
            try:
                element = self.driver.find_element_by_name(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' %e)

        elif ele_type == 'link':
            try:
                element = self.driver.find_element_by_link_text(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' % e)
        elif ele_type == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' % e)

        elif ele_type == 'class':
            try:
                element = self.driver.find_element_by_class(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' % e)

        elif ele_type == 'p_link':
            try:
                element = self.driver.find_element_by_partial_link_text(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' % e)
        elif ele_type == 'android_uiautomator':
            try:
                element = self.driver.find_element_by_android_uiautomator(value)
                logger.info('had find element{},by {} via value{}'.format(element.text, ele_type, value))
            except Exception as e:
                logger.error('定位方式有错误:%s' % e)

        else:
            logger.error('NoSuchElementTypeException:%s' %ele_type)
            raise NameError('please enter correct type:id,name,class,link_text,android_uiautomator,xpath,p_link')

        return element

    def base_click(self,loc):
        '''
        点击
        :param loc:
        :return:
        '''
        el = self.base_find_element(loc)
        el.click()

    def base_input(self,loc,value):
        '''
        输入
        :param loc:
        :param value:
        :return:
        '''
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)


    @property
    def base_page_source(self):
        return self.driver.page_source()


if __name__ == '__main__':
    pass

