from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/weather')
def get_weather():
    days = request.args.get('days', 7)
    data = get_some_days_tmp(days)

    with open('../DataProcessing/interval.json', 'r') as file:
        file_content = file.read()
        intervals = json.loads(file_content)

    new_data = {}
    # new_data = {date : [[day_tmp, night_tmp], [day_interval, night_interval], [day_truth, night_truth]]}
    for date, tmp in data.items():
        print(date, tmp)
        day_tmp = tmp["day"]
        night_tmp = tmp["night"]

        i_day, i_month = date.split("/")
        interval_date = i_day + "/" + i_month
        day_interval = intervals[interval_date]["day"]
        night_interval = intervals[interval_date]["night"]
        day_truth = day_interval[0] <= day_tmp <= day_interval[1]
        night_truth = night_interval[0] <= night_tmp <= night_interval[1]
        new_data[date] = [[day_tmp, night_tmp], [day_interval, night_interval], [day_truth, night_truth]]
    
    for date, values in new_data.items():
        print(date, values)

    print(new_data)

    return jsonify(new_data)

if __name__ == '__main__':
    import os 
    import sys
    sys.path.insert(1, os.path.abspath('../DataParsing/WeatherForecast'))
    from parse_current_weather import get_some_days_tmp
    app.run(debug=True)