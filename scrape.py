#!/opt/homebrew/bin/python3
# given a parameterized url, return the html object.

from bs4 import BeautifulSoup as souper
import datetime
import math
import time
import requests

def fetch (url):
    return requests.get(url)

def main ():
    start = datetime.datetime.now()
    url = input("\033[31;1;3murl: \033[0m")
    response = fetch (url)
    try: 
        soup = souper(response, 'html.parser')
        print ("soup", soup)
    except:
        # tempted to say continue
        pass

    # should show 200, or something went wrong
    print ("\033[31;4;9mstatus: "+ str(response.status_code) + "\033[0m")
    name = math.trunc(time.time())
    name = 'html/' + str(name) + '.html'

    # write to file
    with open(name, 'wb') as file:
        file.write(response.content)
        file.close()
    print ('\033[51;1;7mfile written!\033[0m')
    finish = datetime.datetime.now() - start
    print ('\033[55;9;10mtime: ' + str(finish) + "\033[0m")

    
if __name__ == '__main__':
    main ()
