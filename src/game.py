import db
import analyser

class Game:
    def __init__(self, database):
        self.database = database
    
    def run(self):
        print('-' * 80)
        print('Welcome to Wordle Helper')
        print('')

        self.analyser = analyser.Analyser(self.database)
        
        try_count = 0
        while try_count < 6:
            try_count += 1
            while True:
                query = input(f'Your {self.count_string(try_count)}:')
                try:
                    if self.database.get_word_list()[query]:
                        break
                except:
                    if query == 'help':
                        recommend = self.analyser.get_best_word()
                        print('Recommended Word is: ' + recommend)
            
            while True:
                result = input('Black: 0\nGreen: 1\nYellow: 2\nSubmit Result: ')
                if len(result) == 5 and (result.count('0') + result.count('1') + result.count('2') == 5):
                    break
            
            self.analyser.apply(query, result)

            if result == '1' * 5:
                print('Congraturation!')
                break

    def count_string(self, count):
        if count == 1:
            return str(count) + 'st'
        elif count == 2:
            return str(count) + 'nd'
        else:
            return str(count) + 'th'