from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from models import db, Event
from routes import bp as routes_bp
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
app.register_blueprint(routes_bp)

# Создание базы данных при первом запуске
with app.app_context():
    db.create_all()
    logging.debug("База данных создана")

    if not Event.query.all():
        test_event = Event(title="Test Event", date="2024-11-08", type="medication")
        db.session.add(test_event)
        db.session.commit()
        logging.debug("Тестовое событие добавлено в базу данных")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
