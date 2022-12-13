import uuid


def create_global_pipedream_ping_dictionary():
    return {"global_uuid": uuid.uuid4().hex, "gui_run_dictionaries": []}
