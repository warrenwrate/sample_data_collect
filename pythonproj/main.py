import loadgame
import loadgamedetail
import loadplayer
import loadgameNgamedetails
from connections import Connections

class Program(Connections):
    def __init__(self):
        super().__init__()

    def main(self):
        load_player = loadplayer.Load_Player()
        self.logger.info("loading players")
        print('loading players...')
        load_player.run()
        #new way loading games
        load_game = loadgameNgamedetails.Load_Game()
        self.logger.info("loading games")
        print('loading games...')
        load_game.run_game_upload()
        '''
        # old way of up loading games and games detail
        load_game = loadgame.Load_Game()
        self.logger.info("loading games")
        print('loading games...')
        load_game.run_game_upload()

        self.logger.info("loading game details")
        print('loading games details...')
        load_game_detail = loadgamedetail.Load_Game_Detail()
        load_game_detail.run_game_upload()
        '''
        self.logger.info("loading complete")

    def tables_exist(self):
        tables = ['players', 'games', 'game_details']
        for table in tables:
            self.cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (table,))
            if not self.cur.fetchone()[0]:
                return False
        return True

if __name__ == '__main__':
    program = Program()
    if program.tables_exist():
        program.main()
    else:
        print("cannot run, one or more tales do not exist")
    
