import requests
import player as p
from time import time
from datetime import datetime
import psycopg2
from connections import Connections
# import logging
# import configparser

class Load_Player(Connections):
    def __init__(self):
        super().__init__()
        # config = configparser.ConfigParser()
        # config.read('configdata.cfg')

        # #config variables
        # logger_file = config['logging']['log_file_name']
        # LOG_FORMAT = config['logging']['log_format']
        # host = config['connections']['host']
        # database = config['connections']['database']
        # user = config['connections']['user']
        # password = config['connections']['password']

        # logging.basicConfig(filename=logger_file, level= logging.INFO, format = LOG_FORMAT)
        # logger = logging.getLogger()

        # conn = psycopg2.connect(host=host,database=database, user=user, password=password)
        # cur = conn.cursor()

    def create_player(self, player, jdata):
        try:
            player.playerid = jdata['id']
            player.gender= jdata['data']['gender']
            player.email= jdata['data']['email']
            player.dob= datetime.strptime(jdata['data']['dob'], '%Y-%m-%d %H:%M:%S')
            player.registered= datetime.strptime(jdata['data']['registered'], '%Y-%m-%d %H:%M:%S')
            player.phone= jdata['data']['phone']
            player.cell= jdata['data']['cell']
            player.nat= jdata['data']['nat']
            #name
            player.title = jdata['data']['name']['title']
            player.first = jdata['data']['name']['first']
            player.last = jdata['data']['name']['last']
            #location
            player.street = jdata['data']['location']['street']
            player.city = jdata['data']['location']['city']
            player.state = jdata['data']['location']['state']
            player.postcode = jdata['data']['location']['postcode']
            #picture
            player.large = jdata['data']['picture']['large']
            player.medium = jdata['data']['picture']['medium']
            player.thumbnail = jdata['data']['picture']['thumbnail']
            #id
            player.id_name = jdata['data']['id']['name']
            player.id_value = jdata['data']['id']['value']

        except Exception as e:
            msg = 'Exception of {} for playerid:{}'.format(e,player.playerid)
            self.logger.error(msg)

        # for key, data in jdata['data'].items():
        #     if key == 'name':
        #         player.title = data['title']
        #         player.first = data['first']
        #         player.last = data['last']
        #     if key == 'location':
        #         player.street = data['street']
        #         player.city = data['city']
        #         player.state = data['state']
        #         player.postcode = data['postcode']
        #     if key == 'picture':
        #         player.large = data['large']
        #         player.medium = data['medium']
        #         player.thumbnail = data['thumbnail']
        #     if key == 'id':
        #         player.id_name = data['name']
        #         player.id_value = data['value']    
        #     if key == 'login':
        #         pass
        #         print('\tsaving to login table')

    def grab_data_rest(self):
        page = 0
        while True:
            r = requests.get('https://x37sv76kth.execute-api.us-west-1.amazonaws.com/prod/users?page={}'.format(page))
            jsondata = r.json()
            if len(jsondata) > 0:
                self.checkjson(jsondata)
                page += 1
            else:
                break

    def checkjson(self, jsondata):
        for jdata in jsondata:
            player = p.Player()
            self.create_player(player, jdata)
            #print("**running test on playerid {}**".format(player.playerid))
            msg = player.checkvalues()
            self.logger.warning(msg)
            self.add_to_db(player)
        #print(player.first, player.last, player.playerid, player.dob)

    def add_to_db(self, player):
        try:
            sql = '''
            insert into players 
            (playerid, firstname,	lastname,	title,	gender,	street,	city,	state,	postcode,	email,
            dob,	phone,	cell,	nat,	registered,	largeimage,	mediumimage,	thumbnail,	id_name,	id_value)

            values ( %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
            player_insert = (player.playerid,player.first,	player.last,	player.title,	player.gender,	player.street,	player.city,	
            player.state,	player.postcode,	player.email,	player.dob,	player.phone,	player.cell,	
            player.nat,	player.registered,	player.large,	player.medium,	player.thumbnail,	
            player.id_name,	player.id_value)

            #print(player_insert[0], player_insert[1], player_insert[3])
            self.cur.execute(sql, player_insert)
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error(error)
        
    def run(self):
        self.logger.info("Starting the process to load players")
        start = time()
        self.grab_data_rest()
        end = time()
        self.conn.close()
        self.logger.info("Finished the process in {} seconds".format(end - start))

