from app.extensions import events_collection
from flask import Blueprint, json, request, jsonify, render_template

main = Blueprint('Main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/get-latest-events', methods=['GET'])
def get_latest_events():
    # Fetch the latest 10 events from MongoDB, sorted by timestamp (descending)
    events = list(events_collection.find().sort('timestamp', -1).limit(10))

    # Transform the events into a more UI-friendly format
    formatted_events = []
    for event in events:
        if event['action_type'] == 'push':
            formatted_events.append(f"{event['author']} pushed to {event['to_branch']} on {event['timestamp']}")
        elif event['action_type'] == 'pull_request':
            formatted_events.append(
                f"{event['author']} submitted a pull request from {event['from_branch']} to {event['to_branch']} on {event['timestamp']}")
        elif event['action_type'] == 'merge':
            formatted_events.append(
                f"{event['author']} merged branch {event['from_branch']} to {event['to_branch']} on {event['timestamp']}")

    return jsonify(formatted_events)