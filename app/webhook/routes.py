from datetime import datetime
from app.extensions import events_collection
from flask import Blueprint, json, request, jsonify

from app.main.utils import create_event_data, handle_pull_request

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    # Get the JSON payload from the webhook request
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')
    # Extract the required data based on event type
    event_data = None

    if event_type == "push":
        reuqest_id = payload["after"]
        author = payload["pusher"]["name"]
        to_branch = payload["ref"].split('/')[-1]
        event_data = create_event_data(author, reuqest_id, "push", None, to_branch)

    elif event_type == "pull_request":
        event_data = handle_pull_request(payload)

    if not event_data:
        return jsonify({"status": "Event type not supported or no relevant action"}), 400

    # Insert event data into MongoDB
    events_collection.insert_one(event_data)

    return jsonify({"status": "success"}), 200
