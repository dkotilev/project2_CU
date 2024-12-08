class Weather:
    def __init__(self, location, day, day_part, temperature, wind_speed, rain_probability, humidity):
        self.location = location
        self.day = day
        self.day_part = day_part
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.rain_probability = rain_probability
        self.humidity = humidity

        self.message = None
        self.validate()

    def validate(self):
        if self.temperature < 0:
            self.message = 'Слишком низкая температура'
            return
        elif self.temperature > 35:
            self.message = 'Слишком высокая температура'
        if self.wind_speed > 50:
            self.message = 'Слишком быстрый ветер'
            return
        if self.humidity < 20:
            self.message = 'Слишком низкая влажность воздуха'
            return
        if self.rain_probability > 70:
            self.message = 'С большой вероятностью будет дождь'
            return
        self.message = 'Всё отлично'
