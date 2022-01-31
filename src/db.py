import json

class DB:
    words_list = {}
    
    def __init__(self, path):
        self.words_list.clear()
        self.path = path
    
    def read(self):
        with open(self.path) as json_file:
            self.words_list = json.load(json_file)
    
    def test(self):
        print(self.words_list)