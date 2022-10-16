import random

from src.Instructor import Instructor
from src.Path import Weather, Path

weather_conditions = ['CLOUDY', 'SUNNY', 'BLIZZARD']

random_weather = random.choice(weather_conditions)
random_temperature = random.randint(-10, 8)
random_wind = random.randint(0, 50)

current_weather = Weather(random_weather, random_wind, random_temperature)
print(current_weather.weather + ', ' + str(current_weather.wind) + ', ' + str(current_weather.temperature))

instructor1 = Instructor('Zielony', 'Teletubiś', '090909090')
instructor2 = Instructor('Fioletowy', 'Teletubiś', '777888999')
instructor3 = Instructor('Czerwony', 'Teletubiś', '098765432')
instructor4 = Instructor('Żółty', 'Teletubiś', '234567890')

blue_instructors = [instructor1, instructor2, instructor3, instructor4]
red_instructors = [instructor1, instructor2, instructor4]
black_instructors = [instructor2]

blue_path = Path('BLUE', 2200, blue_instructors)
red_path = Path('RED', 6000, red_instructors)
black_path = Path('BLACK', 3000, black_instructors)

paths = [blue_path, red_path, black_path]

for path in paths:
    path.change_status(current_weather)
    print(path.color + ' - ' + path.status)
    for instructor in path.instructors:
        print(instructor.name)