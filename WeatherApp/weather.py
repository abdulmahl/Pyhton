import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3568c1ec2fec38dc33e44c1816b1d347"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    temperature_min = int(json_data['main']['temp_min'] - 273.15)
    temperature_max = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%H: %M: %S", time.gmtime(json_data['sys']['sunrise'] + 7200))
    sunset = time.strftime("%H: %M: %S", time.gmtime(json_data['sys']['sunset'] + 7200))

    condition_information = f"{condition}\n {str(temperature)}°C"
    weather_info = f"\n Max Temperature: {str(temperature_max)} \n Min Temperature: {str(temperature_min)} \n Pressure: {str(pressure)} \n Humidity: {str(humidity)} \n Wind Speed: {str(wind_speed)} \n Sunrise @ {sunrise} \n Sunset @ {sunset}"
    label1.config(text= condition_information)
    label2.config(text= weather_info)

canvas = tk.Tk()
canvas.geometry("500x350")
canvas.title("Simple Weather Widget")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font= t)
textfield.pack(pady= 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font= t)
label1.pack()

label2 = tk.Label(canvas, font= f)
label2.pack()

canvas.mainloop()