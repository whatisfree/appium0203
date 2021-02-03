import pytest

from base.baseDriver import BaseDriver
import time

@pytest.fixture(scope='function')
def getdriver():
    '''
    引入driver
    :return:
    '''
    driver = BaseDriver.start_driver(appPackage='com.douban.frodo',appActivity='activity.SplashActivity')
    yield driver
    time.sleep(5)
    driver.quit()
