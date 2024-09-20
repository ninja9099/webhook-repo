
from datetime import  datetime
def create_event_data(author, request_id, action_type, from_branch, to_branch):
    return {
        "author": author,
        "reqest_id": request_id,
        "action_type": action_type,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": datetime.now().isoformat()
    }

# Helper function to handle pull request events
def handle_pull_request(payload):
    action = payload["action"]
    reuqest_id = payload["pull_request"]["id"]
    author = payload["pull_request"]["user"]["login"]
    from_branch = payload["pull_request"]["head"]["ref"]
    to_branch = payload["pull_request"]["base"]["ref"]

    if action == "opened":
        return create_event_data(author, reuqest_id, "pull_request", from_branch, to_branch)

    elif action == "closed" and payload["pull_request"]["merged"]:
        return create_event_data(author, reuqest_id,  "merge", from_branch, to_branch)

    return None