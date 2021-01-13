from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from get_data import get_news_data, get_sleep_data, get_all_sleep_data
from outliers import get_outliers
from correlation import check_correlation

app = Flask(__name__)

def sleep_data(sleep_index):
    data = get_sleep_data(sleep_index)
    outliers = get_outliers(data)
    x_accel = []
    y_accel = []
    z_accel = []
    in_mic = []
    ex_mic = []
    cancelled_sound = []
    for i in range(len(data[0])):
        time = data[0][i]*1000
        x_accel.append([time, data[1][i]])
        y_accel.append([time, data[2][i]])
        z_accel.append([time, data[3][i]])
        in_mic.append([time, data[4][i]])
        ex_mic.append([time, data[5][i]])
        cancelled_sound.append([time, data[6][i]])
    return([outliers, x_accel, y_accel, z_accel, in_mic, ex_mic, cancelled_sound])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sleep/1')
def sleep1():
    data = sleep_data(0)
    return render_template('sleep.html', date = "02-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])

@app.route('/sleep/2')
def sleep2():
    data = sleep_data(1)
    return render_template('sleep.html', date = "03-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/sleep/3')
def sleep3():
    data = sleep_data(2)
    return render_template('sleep.html', date = "04-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/sleep/4')
def sleep4():
    data = sleep_data(3)
    return render_template('sleep.html', date = "05-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/sleep/5')
def sleep5():
    data = sleep_data(4)
    return render_template('sleep.html', date = "06-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/sleep/6')
def sleep6():
    data = sleep_data(5)
    return render_template('sleep.html', date = "07-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/sleep/7')
def sleep7():
    data = sleep_data(6)
    return render_template('sleep.html', date = "08-01-21", outliers = data[0], x_accel = data[1], y_accel = data[2], z_accel = data[3], in_mic = data[4], ex_mic = data[5], cancelled_sound = data[6])


@app.route('/news')
def news():
    news_data = get_news_data()
    return render_template('news.html', news_data = news_data)
    #return render_template('success.html')

@app.route('/comparison')
def comparison():
    news_data = get_news_data()
    sleep_data = get_all_sleep_data()

    restlessness = []
    internal = []
    external = []
    for i in sleep_data:
        outliers = get_outliers(i)
        restlessness.append(outliers[0])
        internal.append(outliers[1])
        external.append(outliers[2])

    guardian_correlation = check_correlation(restlessness, news_data[2])
    bbc_correlation = check_correlation(restlessness, news_data[3])
    internal_correlation = check_correlation(restlessness, internal)
    external_correlation = check_correlation(restlessness, external)

    return render_template('comparison.html', news_data = [news_data[2], news_data[3]], outliers = [restlessness, internal, external], correlation = [guardian_correlation, bbc_correlation, internal_correlation, external_correlation])

if __name__ == '__main__':
    app.run()
