'''
pip install configparser
'''
import configparser

from item_path import DIR_NAME


class IniHelper(object):
    def __init__(self):
        '''
        具体的配置文件在哪一个文件夹里面
        '''
        self.source_folder = 'pageElement'

    def get_source_file(self,filename):
        '''
        获取ini文件的config配置信息
        :param filename: ini文件的名字
        :return:
        '''
        # 创建config这个类
        try:
            config=configparser.ConfigParser()
            file_path=DIR_NAME + '/'+self.source_folder +'/'+filename
            # 通过这个文件路径读取的内容就会保存到config中
            config.read(file_path, encoding='utf-8')
            return config
        except Exception as e:
            print('read config file error:'+str(e))


    def get_value(self,filename,section,key):
        '''
        获取key所对应的值，即定位方法和值
        :param filename:
        :param section:
        :param key:
        :return:
        '''
        try:
            config = self.get_source_file(filename)
            value = config.get(section, key)
            return value
        except Exception as e:
            print('get value fail:'+str(e))

if __name__ == '__main__':
    print(IniHelper().get_value('doubanLogin.ini', 'Button', '我的'))

