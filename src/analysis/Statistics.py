import json

class Statistics():
    def __init__(self):
        self.sentences = 0
        self.words = 0
        self.chars = 0
        self.level = 0
        self.clauses = 0
        self.clausesPerSent = 0
        self.avg_frequency = 0
        self.final_reading_level = 0
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
          
    def calculateLevel(self):
        if self.words == 0:
            self.level = 0
        
        else:
            self.level = round(4.71 * ( float(self.chars) / float(self.words) ) + 0.5 * ( float(self.words) / float(self.sentences) ) - 21.43, 1)
    
    def __str__(self):
        return 'number of sentences: ' + str(self.sentences) + '\n' + \
                'number of words: ' + str(self.words) + '\n' + \
                'number of characters: ' + str(self.chars) + '\n' + \
                'reading level: ' + str(self.level) + '\n' + \
                'number of clauses: ' + str(self.clauses) + '\n' + \
                'clauses per sentence: ' + str(self.clausesPerSent)