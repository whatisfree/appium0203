'''

多进程实现多任务
'''
import multiprocessing
import os
import subprocess

import pytest
def start_appium_server():
    os.system('appium')


def main():
    '''
    启动各种服务
    1.appium服务
    2.pytest运行脚本
    3.启动allure服务
    :return:
    '''
    # 用多进程启动appium服务，然后返回一个进程
    p=multiprocessing.Process(target=start_appium_server)
    p.start()
    pytest.main(['-sv','./case/test_douban.py','--alluredir=./reports/douban','--clean-alluredir'])
    # 启动allure服务
    subprocess.call('allure generate ./reports/douban -o ./reports/html/ --clean',shell=True)
    # 等待其他进程
    os.system('taskkill -F -PID node.exe')
    p.join()
    # 进程退出
    p.terminate()

if __name__ == '__main__':
    main()