import urllib.parse, urllib.request, http.cookiejar
from decimal import Decimal
#import sys
import json

URL = 'http://aihaiyang.com/software/l2sca/single/'

class Metrics:
    dict = {}
    def __init__(self, unparsed):
        unparsed = unparsed.strip() #removes whitespaces from beginning + end of string 
        unparsed = unparsed.replace('\n', '') #strip new lines
        unparsed = unparsed.replace(' ', '') #strip spaces
        
        firstDigitIndex = -1
        for i, c in enumerate(unparsed):
            if c.isdigit():
                firstDigitIndex = i
                break
        if firstDigitIndex == -1:
            raise Exception('missing digit')
        
        keys = unparsed[:firstDigitIndex].split(',')
        vals = unparsed[firstDigitIndex:].split(',')
        
        if not len(keys) == len(vals):
            raise Exception('keys length of ', len(keys), ' diff from vals length of ', len(vals))
        
        index = 0
        for key in keys:
            self.dict[key] = vals[index]
            index += 1
            
    def clauses(self):
        return self.dict['C']
    
    def sentences(self):
        return self.dict['S']
    
    def clausesPerSentence(self):
        return self.dict['C/S']
    
    def __str__(self):
        result = str(self.dict)
        result = result.replace('{', '{\n\t').replace('}', '\n}').replace(', ', ',\n\t')
        return result
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    @staticmethod
    def produceFrom(source):
        debug = urllib.request.HTTPHandler(debuglevel = 1) #debug HTTP request-response
    
        cookies = http.cookiejar.CookieJar() #create object that maintains cookies across connections
        opener = urllib.request.build_opener(debug, urllib.request.HTTPCookieProcessor(cookies)) #creates new request opener
        get = opener.open(URL) #GET method (there's only one arg)
    
        if not get.code == 200: #if not successful, error
            return str(get.status) + ' ' + get.reason
    
        #print(cookies)
    
        csrftoken = '?' #default value, expecting csrf is missing
        for c in cookies: #iterates thru cookies gathered in the GET request
            if c.name == 'csrftoken': #if expected csrf found 
                csrftoken = c.value #store the value for the hidden field in the form
    
        if csrftoken == '?': #if not found, return error
            return 'missing csrftoken'
    
        form = urllib.parse.urlencode({ #values for the form for the POST method
            'csrfmiddlewaretoken': csrftoken,
            'q1': source,
            'q2': '',
            'measures': 'c_t'})
        form = form.encode('utf-8') #encode the dictionary that is the form content
        response = opener.open(URL, form) #issue a POST method request (there's 2 args)
    
        if not response.code == 200: #if not successful, error
            return str(response.status) + ' ' + response.reason
    
        html = response.read().decode('utf-8') #convert bytes to string; unparsed html that is the response
        #print(html)
        unparsed = html.partition('</legend>')[2].partition('</fieldset>')[0] #finds the needed stats/results
        unparsed = unparsed.replace('<br/>', '') #clean html leftovers
    
        return Metrics(unparsed)