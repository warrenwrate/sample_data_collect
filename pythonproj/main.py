import loadgame
import loadgamedetail
import loadplayer
from connections import Connections

class Program(Connections):
    def __init__(self):
        super().__init__()

    def main(self):
        load_player = loadplayer.Load_Player()
        self.logger.info("loading players")
        load_player.run()
        load_game = loadgame.Load_Game()
        self.logger.info("loading players")
        load_game.run_game_upload()
        self.logger.info("loading game details")
        load_game_detail = loadgamedetail.Load_Game_Detail()
        load_game_detail.run_game_upload()
        self.logger.info("loading complete")

if __name__ == '__main__':
    program = Program()
    program.main()
    
