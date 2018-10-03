import logging
import configparser
import psycopg2

class Connections:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('configdata.cfg')

        #config variables
        try:
            self.logger_file = self.config['logging']['log_file_name']
            self.LOG_FORMAT = '%(levelname)s-%(filename)s: %(message)s - %(asctime)s'
            self.host = self.config['connections']['host']
            self.database = self.config['connections']['database']
            self.user = self.config['connections']['user']
            self.password = self.config['connections']['password']
            #csv location
            self.csv_loc = self.config['connections']['csv_loc']

            logging.basicConfig(filename= self.logger_file, level= logging.INFO, format = self.LOG_FORMAT)
            self.logger = logging.getLogger()

            self.conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="14Butters!")
            self.cur = self.conn.cursor()
        except Exception as error:
            print('error:',error)