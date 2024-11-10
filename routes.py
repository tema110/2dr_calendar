from flask import Blueprint, jsonify, request
from models import db, Event

bp = Blueprint('routes', __name__)

@bp.route('/events', methods=['GET'])
def fetch_events():
    events = Event.query.all()
    print("Запрос событий:", events)  # Логирование списка событий
    response = jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'date': event.date,
        'time': event.time,
        'completed': event.completed
    } for event in events])
    print("Ответ на запрос:", response)  # Логирование ответа
    return response

@bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(
        title=data['title'],
        description=data.get('description', ''),
        date=data['date'],
        time=data.get('time', '')
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created successfully'}), 201

@bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'error': 'Event not found'}), 404
    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    event.date = data.get('date', event.date)
    event.time = data.get('time', event.time)
    event.completed = data.get('completed', event.completed)
    db.session.commit()
    return