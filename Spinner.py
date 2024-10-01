import random

class Spinner:
    def __init__(self, filename):
        self.synonym_dict = {}
        # Read the synonym file and populate the dictionary
        with open(filename, 'r') as file:
            for line in file:
                word, synonyms = line.strip().split(':')
                self.synonym_dict[word] = synonyms.split(',')

    def spin_text(self, text):
        words = text.split()
        new_text = []
        for word in words:
            if word in self.synonym_dict:
                # 50% chance to replace the word with a synonym
                if random.randint(1, 100) > 50:
                    new_word = random.choice(self.synonym_dict[word])
                    new_text.append(new_word)
                else:
                    new_text.append(word)
            else:
                new_text.append(word)
        # Join the list into a single string and return the result
        return ' '.join(new_text)
