from html.parser import HTMLParser
from urllib import request

#获取属性的函数
def _attr(attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_h3 = False
        self.in_time = False
        self.in_span = False

#处理开始标签
    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and _attr(attrs, 'class') == 'event-title':
            self.in_h3 = True

        if tag == 'time':
            self.in_time = True

        if tag == 'span' and _attr(attrs, 'class') == 'event-location':
            self.in_span = True

#处理中间的数据
    def handle_data(self, data):
        #print("lastag: " lasttag)
        if self.in_h3 == True and self.lasttag == 'a':
            print("会议标题: ",data)

        if self.in_time == True and self.lasttag == 'time':
            print("会议时间: ",data)

        if self.in_span == True and self.lasttag == 'span':

            print("会议地点: ",data)

#处理结束标签
    def handle_endtag(self, tag):
        self.in_h3 = False
        self.in_time = False
        self.in_span = False
def getHtml():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data

p=MyHTMLParser()
p.feed(getHtml())
p.close()