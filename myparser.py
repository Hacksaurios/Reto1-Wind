from xml.sax import handler

class Windmill():
    def __init__(self):
        self.id = ''
        self.lon = ''
        self.lat = ''
        self.systempower = ''
        self.speed = ''
        self.speedlimit = ''
        self.speedavrg = ''
        self.accuracy = ''

    def __str__(self):
        return f'{self.id},{self.lon},{self.lat},{self.systempower},{self.speed},{self.speedlimit},{self.speedavrg},{self.accuracy}'


class ContentGenerator(handler.ContentHandler):

    def __init__(self,  windmills:list):
        self.windmillList = windmills
        self.current=''
        self.aux=True

    def startElement(self, name, attrs):
        if name == 'coordinates':
            self.aux=False
        elif name == 'element' and self.aux:
            self.windmill = Windmill()
        self.current = name

    def endElement(self, name):
        if name == 'coordinates':
            self.aux=True
        elif name == 'element' and self.aux:
            self.windmillList.append(self.windmill)

    def characters(self, content):
        if self.current == 'id':
            if self.windmill.id=='':
                self.windmill.id = content
        elif self.current == 'element' and self.aux==False:
            if self.windmill.lon=='':
                self.windmill.lon = content
            elif self.windmill.lat=='' or self.windmill.lat == '\n' or self.windmill.lat == '               ':
                self.windmill.lat = content
        elif self.current == 'windmill.system.power':
            if self.windmill.systempower=='':
                self.windmill.systempower = content
        elif self.current == 'windmill.system.sensor.blades.speed':
            if self.windmill.speed=='':
                self.windmill.speed = content
        elif self.current == 'windmill.config.blades.speed.limit':
            if self.windmill.speedlimit=='':
                self.windmill.speedlimit = content
        elif self.current == 'windmill.system.blades.speed.average':
            if self.windmill.speedavrg=='':
                self.windmill.speedavrg = content
        elif self.current == 'windmill.system.sensor.accuracy':
            if self.windmill.accuracy=='':
                self.windmill.accuracy = content