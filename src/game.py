import db
import analyser

class Game:
    def __init__(self, database):
        self.database = database
        self.words_list = self.database.words_list
    
    def run(self):
        print('-' * 80)
        print('Welcome to Wordle Helper!')
        print('')

        self.analyser = analyser.Analyser(self.database)
        
        try_count = 0
        while try_count < 6:
            try_count += 1
            print()
            while True:
                query = input(f'Your {self.count_string(try_count)} try(Type help to get help): ')
                try:
                    if self.words_list[query]:
                        break
                except:
                    if query == 'help':
                        recommend = self.analyser.get_best_word()
                        print('Recommended Word is: ' + recommend)
            
            while True:
                result = input('Submit Result(Black: 0/Green: 1/Yellow: 2): ')
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