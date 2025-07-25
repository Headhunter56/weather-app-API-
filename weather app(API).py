from tkinter import *
import requests
from plyer import notification
import time
import json


last_responce=0
def weather():
    city = city_name.get()
    api = "06a6281ef78bd0942fba1926f54fa63d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    responce = requests.get(url)
    data = responce.json()




    if responce.status_code==200:
        print("success")
        temperatur = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]['speed']
        result_label.config(text=f'{description.capitalize()},{temperatur}C\nhumidity:{humidity}%\nwind:{wind}%')
        window.after(10000,weather)


        global last_responce
        current_time=time.time()
        if current_time-last_responce >=10:

            notification.notify(
                title=f'Weather in {city}',
                message=f'{description.capitalize()},{temperatur}C'
            )
            last_responce=current_time

        with open('weather_log.txt','a')as file:
            file.write(f'{description.capitalize()}')
            file.write(f'Temperature:{temperatur}')
            file.write(f'Humidity:{humidity}')
            file.write(f'Temperature:{temperatur}')
            file.write(f'Humdity:{humidity}')
            # file.write(f'\n {humidity},{wind}C')
    else:
        result_label.config(text='city not found')


window=Tk()
window.title('Weather app')
window.geometry("300x200")

city_name=Entry(window)
city_name.grid(row=0,column=1)
city_name.pack(pady=5)

submit=Button(window,text='submit',command=weather)
submit.pack(pady=5)

result_label=Label(window,text='')
result_label.pack(pady=10)

refresh_button=Button(window,text='Refresh',command=weather)
refresh_button.pack(pady=5)


window.mainloop()