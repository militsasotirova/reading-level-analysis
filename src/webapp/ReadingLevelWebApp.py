import cherrypy, os
from analysis.ReadingLevel import ReadingLevel
from analysis.Statistics import Statistics
#import json

class ReadingLevelWebapp(object):
    @cherrypy.expose
    def index(self):
        return open('public/index.html')

    @cherrypy.expose
    @cherrypy.popargs('text') 
    def level(self, text = None):
        if (text == None or text == ''):
            stat = Statistics()
        else:
            stat = ReadingLevel().automatedReadabilityIndex(text)
        return stat.toJSON()
        '''
        html = 'Number of Sentences: ' + str(stat.sentences) + '<br/>' + \
                'Number of Words: ' + str(stat.words) + '<br/>' + \
                'Number of Characters: ' + str(stat.chars) + '<br/>' + \
                'Reading Level: ' + str(stat.level)
               
        return html
        '''
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.dir': os.path.abspath(os.getcwd() + '/public')
        },

        '/css': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'css'
        },

        '/fonts': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'fonts'
        },
            
        '/images': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'images'
        },

        '/js': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'js'
        },

        '/jquery': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'jquery'
        },

        '/materialize': {
            'tools.staticdir.on' : True,
            'tools.staticdir.root': 'materialize'
        },

        '/level': {
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/html')],
        }
    }

    # static files
    '''
    '/favicon.ico': {
        'tools.staticfile.on' : True,
        'tools.staticfile.filename' : os.path.abspath(os.getcwd()) + '/public/images/favicon.ico'
    },
    '/materialize/css/materialize.min.css': {
        'tools.staticfile.on' : True,
        'tools.staticfile.filename' : os.path.abspath(os.getcwd()) + '/public/materialize/css/materialize.min.css'
    },
    '/style.css': {
        'tools.staticfile.on' : True,
        'tools.staticfile.filename' : os.path.abspath(os.getcwd()) + '/public/style.css'
    },
    '''
    # static files

    webapp = ReadingLevelWebapp()
    #webapp.level = ReadingLevelWebapp().index
    cherrypy.config.update({
        #'server.socket_host': 'tris',
        'server.socket_port': int(os.environ.get('PORT', '8080'))
    })
    cherrypy.quickstart(webapp, '/', conf)#cherrypy.quickstart(webapp, '/analysis', conf)