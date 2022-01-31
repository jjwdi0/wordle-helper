from re import L


class Analyser:
    def __init__(self, database):
        self.database = database
        self.candidates = [*self.database.words_list]
    
    def get_best_word(self):
        best_word = ''
        max_result = 1e9
        count = 0
        for word in self.candidates:
            if count * 100 // len(self.candidates) != (count + 1) * 100 // len(self.candidates):
                print(str((count + 1) * 100 // len(self.candidates)) + '''% completed''')
            count += 1
            results = {}
            for word2 in self.candidates:
                result = self.get_match_result(word, word2)
                try:
                    results[result] += 1
                except:
                    results[result] = 1
            
            if max_result > max(results.values()):
                max_result = max(results.values())
                best_word = word
        print()
        
        return best_word
    
    def get_match_result(self, word1, word2):
        result = ['0'] * len(word1)
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                result[i] = '1'
            else:
                count2[ord(word2[i]) - ord('a')] += 1
        
        for i in range(len(word1)):
            if result[i] != 1:
                idx = ord(word1[i]) - ord('a')
                if count1[idx] < count2[idx]:
                    result[i] = '2'
                
                count1[idx] += 1
        
        return ''.join(result)
    
    def apply(self, query, result):
        new_candidates = []
        for word in self.candidates:
            if self.get_match_result(query, word) == result:
                new_candidates.append(word)
        self.candidates = new_candidates