from dataclasses import dataclass
import json


@dataclass
class Task:
    name: str
    siblings: bool = None
    mother: str = None
    father: str = None
    siblings_by_mother: list[str, ...] | str = None
    owner: str = None
    owner_species: str = None
    species_occupation: str = None
    occupation_class: str = None
    occupation_subclass: str = None

data = open('test_data_logic_task.json')
jsonData = json.loads(data.read())

def jaonWalk(dicts: list) -> list:
    tasks = []
    for dict in dicts:
        tasks.append(toDeep(dict['fields'], Task(dict['fields'][0]['value'])))

    return tasks

def toDeep(dicts, task) -> Task:
    for dict in dicts:
        match dict['id']:
            case 2:
                task.siblings = dict['value']
                if len(dict) == 5:
                    toDeep(dict['fields'], task)
            case 3:
                task.mother = dict['value']
                if len(dict) == 5:
                    toDeep(dict['fields'], task)
            case 4:
                task.father = dict['value']
            case 5:
                task.siblings_by_mother = dict['value']
            case 6:
                task.owner = dict['value']
                if len(dict) == 5:
                    toDeep(dict['fields'], task)
            case 7:
                task.owner_species = dict['value']
                if len(dict) == 5:
                    toDeep(dict['fields'], task)
            case 8:
                task.species_occupation = dict['value']
                if len(dict) == 5:
                    toDeep(dict['fields'], task)
            case 9:
                task.occupation_class = dict['value']
            case 10:
                task.occupation_subclass = dict['value']
    return task

Tasks = jaonWalk(jsonData['task'])

for task in Tasks:
    print(task)

