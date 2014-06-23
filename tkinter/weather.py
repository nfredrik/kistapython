import json
import urllib
from Tkinter import *


class WeatherReporter:
    def __init__(self, root):
        self.root = root
        self.top_frame()
        self.display_frame()

    def display_final(self, data):

        self.canvas.create_text(30, 45, fill='white', text='Score: 0')
        print data

    def show_weather_button_clicked(self):

        if not self.enteredlocation.get():
            return
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(5,5,305,41, fill='#F6AF06')
        data = self.get_weather_data()
        data = self.json_to_dict(data)
        self.display_final(data)

    def top_frame(self):
        topfrm= Frame(self.root)
        topfrm.grid(row=1, sticky='w')
        Label(topfrm, text='Enter Location').grid(row=1, column=2, sticky='w')
        self.enteredlocation = StringVar()
        Entry(topfrm, textvariable= self.enteredlocation).grid(row=1, column=2, sticky='w')
        Button(topfrm, text='Show Weather Info', command=self.show_weather_button_clicked).grid(row=1, column=3, sticky='w')

    def display_frame(self):
        displayfrm = Frame(self.root)
        displayfrm.grid(row=2, sticky='ew', columnspan=5)
        self.canvas= Canvas(displayfrm, height = '410', width='300',background='black', borderwidth=5)
        self.canvas.create_rectangle(5,5,305,415, fill= '#F6AF06')
        self.canvas.grid(row=2, sticky='w', columnspan=5)


    def json_to_dict(self, jdata):
        mydecoder = json.JSONDecoder()
        decodedjdata = mydecoder.decode(jdata)

        flatteneddict = {}
        for key, value in decodedjdata.items():
            if key == 'weather':
                for ke, va in value[0].items():
                    flatteneddict[str(ke)] = str(va).upper()
                    continue
            try:
                for k, v in value.items():
                    flatteneddict[str(k)] = str(v).upper()
            except:
                    flatteneddict[str(key)] = str(value).upper()

        return flatteneddict

    def get_weather_data(self):
        try:
            apiurl='http://api.openweathermap.org/data/2.5/weather?q=%s'%self.enteredlocation.get()
  
            print apiurl

            data = urllib.urlopen(apiurl)
            jdata = data.read()
            return jdata
        except IOError as e:
            tkMessageBox.showerror('Unable to connect', 'Unable to connect %s'%e)

def main():
    root=Tk()
    WeatherReporter(root)
    root.mainloop()



if __name__ == '__main__':
    main()
