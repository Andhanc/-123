from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('preloader.html')  # Показать страницу загрузки (preloader)

@app.route('/index')
def index():
    return render_template('index.html')  # Показать основную страницу

@app.route('/about')
def about():
    return render_template('about.html')  # Страница "О нас"

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Страница "Контакты"

if __name__ == '__main__':
    app.run(debug=True)
