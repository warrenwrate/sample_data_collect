import csv
import psycopg2
from connections import Connections

class Load_Game(Connections):
    def __init__(self):
        super().__init__()
        self.game_details_list = []

    #do original idea of holdint the count 
    def get_game_data(self, filename):
        with open(filename, "r") as csvfile:
            datareader = csv.reader(csvfile)
            player1 = None
            player2 = None
            next(datareader)  # yield the header row
            for row in datareader:
                self.game_details_list.append( (row[0], row[1], int(row[2]), int(row[3]), row[4] ))
                if row[2] == '1':
                    player1 = row[1]
                if row[2] == '2':
                    player2 = row[1]
                if row[4] != '':
                    yield (row[0], row[1], int(row[2]), int(row[3]), row[4], player1, player2)
                #print(row)

    def save_game_data(self,game_data):
        sql = """INSERT INTO games(game_id, last_player_played,	last_move_number, last_col_number,result,player_1,player_2)
                VALUES(%s, %s, %s, %s, %s, %s, %s);"""
        try:
            self.cur.execute(sql, game_data)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error('game_id {} insert had an error:{}'.format(game_data[0], error))

    def save_gamedetails_data(self):
        sql = """INSERT INTO game_details(game_id, player_id, move_number, column_number,result)
                VALUES(%s, %s, %s, %s, %s);"""
        try:
            self.cur.executemany(sql,self.game_details_list)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error('insert many had an error:{}'.format( error))

    def run_game_upload(self):
        for game_data in self.get_game_data(self.csv_loc):
            self.save_game_data(game_data)
        self.save_gamedetails_data()
        self.conn.close()

    ##run_game_upload()
