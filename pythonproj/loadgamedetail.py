import csv
import psycopg2
from connections import Connections

class Load_Game_Detail(Connections):
    def __init__(self):
        super().__init__()

    #do original idea of holdint the count 
    def get_game_data(self, filename):
        with open(filename, "r") as csvfile:
            datareader = csv.reader(csvfile)
            next(datareader)  # yield the header row
            for row in datareader:
                yield (row[0], row[1], int(row[2]), int(row[3]), row[4])
                #print(row)

    def save_game_data(self,game_data):
        sql = """INSERT INTO game_details(game_id, player_id, move_number, column_number,result)
                VALUES(%s, %s, %s, %s, %s);"""
        try:
            self.cur.execute(sql, game_data)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error('game_id {} insert had an error:{}'.format(game_data[0], error))

    def run_game_upload(self):
        for game_data in self.get_game_data(self.csv_loc):
            self.save_game_data(game_data)
        self.conn.close()

##run_game_upload()