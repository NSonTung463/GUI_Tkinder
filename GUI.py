import tkinter as tk
import requests
from PIL import Image, ImageTk
HEIGHT = 500
WIDTH = 600
root = tk.Tk()

#b592a59f0de6e1befc3f40e6e20ae75f
def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    #final_str = 'hello'
    return final_str


def get_weather(city):
    weather_key = 'b592a59f0de6e1befc3f40e6e20ae75f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img





canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#01b29a', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#026459', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()