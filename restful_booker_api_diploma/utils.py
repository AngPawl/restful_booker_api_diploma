import json
import os


def load_schema(file_name):
    root_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(root_dir)

    path = os.path.join(project_dir, root_dir, 'json_schemes', file_name)

    with open(path) as file:
        json_schema = json.loads(file.read())

    return json_schema
