import eel
import pyowm

owm = pyowm.OWM("6e40265159fce2b4294642d753db39f8")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    obs = mgr.weather_at_place(place)
    w = obs.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + place + " сейчас " + str(temp) + " градусов"


eel.init("web")
eel.start("main.html", size=(700, 700))