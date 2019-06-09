# 
# Example file for parsing and processing HTML
#

#import html.parser.HTMLParser
from HTMLParser import HTMLParser

metacount = 0

class myHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: {0}".format(data))
        pos = self.getpos()
        print("\tAt line {0} position {1}".format(pos[0], pos[1]))

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1
        print("Encountered start tag: {0}".format(tag))
        pos = self.getpos()                                            
        print("\tAt line {0} position {1}".format(pos[0], pos[1]))

        if attrs.__len__() > 0:
            for a in attrs:
                print("\tAttributes: {0} = {1}".format(a[0], a[1]))
    
    def handle_endtag(self, tag):
        print("Encountered end tag: {0}".format(tag))
        pos = self.getpos()
        print("\tAt line {0} position {1}".format(pos[0], pos[1]))

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered data: {0}".format(data))
        pos = self.getpos()
        print("\tAt line {0} position {1}".format(pos[0], pos[1]))

def main():
    # Instantiate the parser and feed it some HTML
    parser = myHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

    print("Meta tag count: {0}".format(metacount))

if __name__ == "__main__":
    main()
