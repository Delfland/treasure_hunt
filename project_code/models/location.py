class Location:
    
    def __init__(self, name, clue, user, game, found, id = None):
        self.name = name
        self.clue = clue
        self.user = user
        self.game = game
        self.found = found
        self.id = id
