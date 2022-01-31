import db
import game

if __name__ == '__main__':
    database = db.DB('./data/words.json')
    database.read()
    game = game.Game(database)
    game.run()