from flask import Flask, render_template

app = Flask(__name__) # Создание приложения

@app.route('/') # Корневой каталог сайта
def index():
    return render_template('index.html')

@app.route('/order') # Страница индивидуального заказа
def order():
    return render_template('order.html')

@app.route('/about') # Страница "О нас"
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)