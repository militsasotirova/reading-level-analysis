import urllib.request, http.cookiejar
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import sys
import string
import math

class Frequency:
    def removePunct(self, words):
        for word in words:
            if word in string.punctuation:
                words.remove(word)
        return words
    
    def removeProperNouns(self, words):
        partsOfSpeech = pos_tag(words)
        for group in partsOfSpeech:
            word = group[0]
            pos = group[1]
            if (pos == 'NNP') or (pos == 'NNPS'):
                words.remove(word)
        return words
    
    def removeCommonWords(self, words):
        #mostCommonWords20 = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at']
        file = open('mostCommonWords.txt', 'r')
        mostCommonWords100 = [word.replace('\n', '') for word in file.readlines()]
        words = [word.lower() for word in words]        
        for word in mostCommonWords100:
            while word in words:
                words.remove(word)
        return words
    
    def lemma(self, words):
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]  
        return words
    
    def removeRepeats(self, words):
        for word in words:
            while words.count(word) > 4:
                words.remove(word)
        return words
    
    def remove_nums_and_punct(self, words):
        for word in words:
            for char in word:
                if char in string.punctuation:
                    words.remove(word)
                    break
                if char.isdigit():
                    words.remove(word)
                    break
        return words
    
    def prepare(self, textStr):
        words = word_tokenize(textStr)
        words = self.removePunct(words)
        words = self.removeProperNouns(words)
        words = self.removeCommonWords(words)
        words = self.lemma(words)
        words = self.removeRepeats(words)
        words = self.remove_nums_and_punct(words)
        return words
      
    def calc_avg_freq(self, listOfWords, frequencies): #frequencies is a dict
        result = 0
        for word in listOfWords:
            freq = frequencies[word]
            if freq == 0:
                freq = 0.0001
            if freq == 1:
                freq = 2
            result += 1 / math.log(freq)
        return result / len(listOfWords)
        
    def find_avg_freq(self, text):
        listOfRelevantWords = self.prepare(text)
        wordsToFindFreq = []
        for word in listOfRelevantWords:
            if not word in wordsToFindFreq:
                wordsToFindFreq.append(word)
        frequencies = Frequency.produceFrom(wordsToFindFreq)
        avg_freq = self.calc_avg_freq(listOfRelevantWords, frequencies)
        return avg_freq  
    
    @staticmethod
    def create_dict_from_file(file):
        stored_words = {}
        f = open(file)
        for line in f.readlines():
            if not line is '\n':
                line_info = line.split()
                stored_words[line_info[0].strip()] = int(line_info[1].strip())
        return stored_words
   
    @staticmethod
    def produceFrom(source): #source will be a list of words
        f = open('stored_words.txt','a+')
        f.write('\n')
        stored_words = Frequency.create_dict_from_file('stored_words.txt')

        app_id = 'app_id', '700ba0b6'
        app_key = 'app_key', 'fe982dda9ba9522587a23ee8653a32fa'
        
        frequencies = {}
        language = 'en'
        httpsHandler = urllib.request.HTTPSHandler(debuglevel = 0) #debug HTTP request-response
        cookies = http.cookiejar.CookieJar() #create object that maintains cookies across connections
        opener = urllib.request.build_opener(httpsHandler, urllib.request.HTTPCookieProcessor(cookies)) #creates new request opener
        opener.addheaders.append(app_id)
        opener.addheaders.append(app_key)
        base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/' + language + '/?corpus=nmc&wordform='
        
        for wordform in source:
            if not wordform in stored_words:
                url =  base_url + wordform
                data = opener.open(url)
                result =  data.read().decode('utf-8')
                unparsed = result.partition('"frequency": ')[2].partition(',')[0] #finds the needed stats/results
                unparsed = unparsed.strip()
                frequency = int(unparsed)
                frequencies[wordform] = frequency
                f.write(wordform + ' ' + str(frequency) + '\n')
            else:
                frequencies[wordform] = stored_words[wordform]
        
        return frequencies
    
if __name__ == '__main__':
    winnie = 'In after-years he liked to think that he had been in Very Great Danger during the Terrible Flood, but the only danger he had really been in was the last half-hour of his imprisonment, when Owl, who had just flown up, sat on a branch of his tree to comfort him, and told him a very long story about an aunt who had once laid a seagull\'s egg by mistake, and the story went on and on, rather like this sentence, until Piglet who was listening out of his window without much hope, went to sleep quietly and naturally, slipping slowly out of the window towards the water until he was only hanging on by his toes, at which moment, luckily, a sudden loud squawk from Owl, which was really part of the story, being what his aunt said, woke the Piglet up and just gave him time to jerk himself back into safety and say, "How interesting, and did she?" when — well, you can imagine his joy when at last he saw the good ship, Brain of Pooh (Captain, C. Robin; 1st Mate, P. Bear) coming over the sea to rescue him.'
    age = 'Therefore, whenever anything happened that Mrs. Archer wanted to know about, she asked Mr. Jackson to dine; and as she honoured few people with her invitations, and as she and her daughter Janey were an excellent audience, Mr. Jackson usually came himself instead of sending his sister. If he could have dictated all the conditions, he would have chosen the evenings when Newland was out; not because the young man was uncongenial to him (the two got on capitally at their club) but because the old anecdotist sometimes felt, on Newland\'s part, a tendency to weigh his evidence that the ladies of the family never showed.'
    default = 'The rule of rhythm in prose is not so intricate. Here, too, we write in groups, or phrases, as I prefer to call them, for the prose phrase is greatly longer and is much more nonchalantly uttered than the group in verse; so that not only is there a greater interval of continuous sound between the pauses, but, for that very reason, word is linked more readily to word by a more summary enunciation. Still, the phrase is the strict analogue of the group, and successive phrases, like successive groups, must differ openly in length and rhythm. The rule of scansion in verse is to suggest no measure but the one in hand; in prose, to suggest no measure at all. Prose must be rhythmical, and it may be as much so as you will; but it must not be metrical. It may be anything, but it must not be verse.'
    test = 'Gaily bedight a galant knight in sunshine and in shadow had journeyed long singing a song in search of El Dorado. But he grew old, this knight so bold and over his heart a shadow fell as he found no spot of ground that looked like El Dorado.'
    t = 'Greece. Washingtons. I love pie.'
    try:
        f = Frequency()
        print('prose: ', f.find_avg_freq(default)) #0.08699651998960121
        print('age of innocence: ', f.find_avg_freq(age)) #0.0.07815229099484537
        print('winnie the pooh: ', f.find_avg_freq(winnie)) #0.07667978256991864
        print('test: ', f.find_avg_freq(test)) #0.11557782064749739
        
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise # well-known exception that the caller will digest 