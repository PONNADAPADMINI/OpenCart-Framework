import configparser   #- These pulls the data from from config file at framework
import os

config_file_path=os.path.abspath(os.curdir)+r"\configurations\config.ini"
config=configparser.RawConfigParser()
config.read(config_file_path)

class readconfig:

    @staticmethod
    def getApplicationUrl():
        url=config.get('commonInfo','baseurl')
        return url

    @staticmethod
    def getEmail():
        email=config.get('commonInfo','email')
        return email

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password

