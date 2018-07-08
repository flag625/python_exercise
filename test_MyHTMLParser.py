from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

def _attrs(attrlist,attrname):
    for attr in attrlist:
        if attr[0]==attrname:
            return attr[1]
        return None

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_h3=False
        self.in_time=False
        self.in_span=False

    def handle_starttag(self, tag, attrs):
        #print('<%s>'%tag)
        if tag=='h3'and _attrs(attrs,'class')=='event-title':
            self.in_h3=True
        if tag=='time':
            self.in_time=True
        if tag=='span' and _attrs(attrs,'class')=='event-location':
            self.in_span=True

    def handle_data(self, data):
        #print(data)
        if self.in_h3:
            print('Event Title: %s'%data)
        if self.in_time:
            print('Event Date: %s'%data)
        if self.in_span:
            print('Event Location: %s'%data)

    def handle_endtag(self, tag):
        #print('</%s>'%tag)
        self.in_h3=False
        self.in_time=False
        self.in_span=False

    def handle_startendtag(self,tag,attrs):
        #print('<%s/>'%tag)
        pass

    def handle_comment(self, data):
        #print('<!-',data,'->')
        pass

    def handle_entityref(self, name):
        #print('&%s:'%name)
        pass

    def handle_charref(self, name):
        #print('&#%s:'%name)
        pass

def get_Html():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data

p = MyHTMLParser()
p.feed(get_Html())
p.close()