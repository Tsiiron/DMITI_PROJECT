from flask import Flask, render_template
import simple_script  # Импортируйте ваш Python скрипт для обработки данных

app = Flask(__name__)

@app.route('/')
def index():
    # Здесь можно вызвать функции вашего скрипта и передать результат в шаблон
    data = simple_script.process_data()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)