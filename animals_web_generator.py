import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


print(load_data('./animals_data.json'))

foxes = load_data('./animals_data.json')

for name, taxonomy, locations, characteristics in (fox.values() for fox in foxes):
    print(f'Name: {name}')
    print(f'Diet: {characteristics["diet"]}')
    print(f'Location: {locations[0]}')
    if 'type' in characteristics:
        print(f'Type: {characteristics["type"]}')
    print(f'---------------------------')

