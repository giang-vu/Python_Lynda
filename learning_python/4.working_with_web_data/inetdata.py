# 
# Example file for retrieving data from the internet
#

import urllib

def main():
    webUrl = urllib.urlopen("http://www.google.com")
    print("Result code: " + str(webUrl.getcode()))

    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()
