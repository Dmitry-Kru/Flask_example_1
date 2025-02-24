from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем текущие дату и время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Передаем их в шаблон
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)