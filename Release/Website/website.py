from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/weather')
def get_weather():
    days = request.args.get('days', 7)
    data = get_some_days_tmp(days)
    return jsonify(data)

if __name__ == '__main__':
    import os 
    import sys
    path_to_module = os.path.abspath('../DataParsing/WeatherForecast')
    print(path_to_module)
    sys.path.insert(1, path_to_module)
    from parse_current_weather import get_some_days_tmp
    app.run(debug=True)