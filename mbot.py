
from ftl import ftl, combat
from steam import steam
import logging

def logs():
    mypath = str("logs/")
    fname = mypath + "/ftl.log"
    logging.basicConfig(
        filename=fname,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
        filemode = 'w'
        )

logs()
# combat.fight()

# steam.start_steam()
# ftl.play_game(ftl.new_game())

ftl.restart_game()
ftl.play_game()

# ftl.handle_encounter()