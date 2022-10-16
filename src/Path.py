class Path:
    def __init__(self, color, length, instructors):

        self.status = None
        self.color = color
        self.length = length
        self.instructors = instructors

    def change_status(self, current_weather):

        if (current_weather.temperature > 2 or current_weather.wind > 39 or current_weather.weather == 'BLIZZARD') and self.color == 'RED':
            self.status = 'CLOSED'
        elif (current_weather.temperature > 7 or current_weather.wind > 49) and self.color == 'BLUE':
            self.status = 'CLOSED'
        elif (current_weather.temperature > -2 or current_weather.wind > 35 or current_weather.weather == 'BLIZZARD') and self.color == 'BLACK':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'


class Weather:
    def __init__(self, weather, wind, temperature):
        self.weather = weather
        self.wind = wind
        self.temperature = temperature