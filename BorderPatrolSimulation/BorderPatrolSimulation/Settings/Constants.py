import json

Constants = {}


def import_settings():
    global Constants
    try:
        with open("BorderPatrolSimulation/Settings/Settings.json", "r") as file:
            Constants = json.load(file)
    except:
        return False
    return True
