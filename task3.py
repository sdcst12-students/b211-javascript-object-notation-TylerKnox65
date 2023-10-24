#Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. 
# We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads 
# into a variable that we can use. Retrieve the data and present it in a more organized format. 
# You may use text output or a window using Tkinter.  
# Our goal is to format the result in a reasonably organized format.
from time import time
#from typing_extensions import runtime
import requests
import json
import tkinter
import datetime


class main():

    def __init__(self) -> None:
        self.openwindow()
        
        self.getdata()
    def run(self):
        try:
            a = float(self.A_entry.get())
            b = float(self.B_entry.get())
            temperature = self.getdata(a,b)
            self.lsum["text"] = f"The temp is: {temperature}"
        except:
            temperature = self.getdata()
            self.lsum["text"] = f"The temp is: {temperature}"
    def openwindow(self):
        window = tkinter.Tk()
        window.title("Weather API fetcher")
        window.geometry("400x200")
        btn = tkinter.Button(window, text = 'Find current temp !', bd = '5',command = self.run)
        self.Label_a = tkinter.Label(window,text="Latitude")
        self.A_entry = tkinter.Entry(window, font=("calibri", 10))
        self.Label_b = tkinter.Label(window,text="Longitude")
        self.B_entry = tkinter.Entry(window, font=("calibri"))
        self.Label_c = tkinter.Label(window,text="Leave blank for current location")
        self.Label_a.grid(row=1, column=1)
        self.A_entry.grid(row=1, column=2)
        self.Label_b.grid(row=2, column=1)
        self.B_entry.grid(row=2, column=2)
        self.Label_c.grid(row=3, column=1)
        btn.grid(row=3, column=2)  
        self.lsum = tkinter.Label(window, text = '')
        self.lsum.grid(row=4, column=1)
        window.mainloop()
    def getdata(self, latitude = 52.52, longitude = 13.41):
        data = json.loads(requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m').text)
        #print(data)
        timestamp = datetime.datetime.now()
        x = str(timestamp)
        x = x.split(":")
        x.pop()[1]
        x.pop()[1]
        x = str(x)[2:-2]+":00"
        x = list(x)
        for i in x:
            if i == " ":
                x[x.index(i)] = "T"
        x = "".join(x)
        num = data["hourly"]["time"].index(x)
        temperature = data["hourly"]["temperature_2m"][num] #FoUND TEMP
        return temperature
    
    #osawoga uwu     
main()