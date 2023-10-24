#!python3
#from _typeshed import Self
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests
# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains


class main():
    
    def __init__(self) -> None:
        self.req = requests.get('https://sdcaf.hungrybeagle.com/menu.php')
        self.data = json.loads(self.req.text)
        for i in range(0,3):
            self.getdata(i)
    #ogaboga
    def getdata(self,x = 0):
        date = (self.data['menu'][x]['date'])
        dayname = (self.data['menu'][x]['dayname'])
        soup = (self.data['menu'][x]['soup'])
        shortorder = (self.data['menu'][x]['shortorder'])
        entree = (self.data['menu'][x]['entree'])
        notes = (self.data['menu'][x]['notes'])
        print(f"The date is {date}, With day {dayname}. The soup for the week is: {soup}, Shortorder: {shortorder}, Entree: {entree}. Notes: {notes}\n")
        #print(date, dayname, soup, shortorder, entree, notes)
    
    
main()