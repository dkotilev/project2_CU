from flask import Flask, render_template, request

from api import API
from config import api_key

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def main_page_post():
    try:
        form = request.form
        start_point, end_point = form['startPoint'], form['endPoint']
    except Exception as e:
        print(e)
        return render_template('error.html', error_message='Ошибка данных из формы')
    api = API(api_key=api_key)
    try:
        start_point_weather = api.weather(start_point)
        end_point_weather = api.weather(end_point)

    except IndexError:
        return render_template('error.html', error_message='Не найдена такая точка')
    except Exception:
        return render_template('error.html', error_message='Ошибка доступа к API')
    return render_template('view.html', start_points=start_point_weather, end_points=end_point_weather,
                           day_format={'Day': 'День',
                                       'Night': 'Ночь'})


if __name__ == '__main__':
    app.run()
