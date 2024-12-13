import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load the data from the JSON file
foxes = load_data('./animals_data.json')

# Generate the output HTML content
def serialize_animal(animal_obj):
    output = ''
    name = animal_obj.get("name", "Unknown")
    taxonomy = animal_obj.get("taxonomy", {})
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})
    
    output += f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <ul class="card__text">
            <li><strong>Diet:</strong> {characteristics.get("diet", "Unknown")}</li>
            <li><strong>Location:</strong> {", ".join(locations)}</li>
    """
    if 'type' in characteristics:
        output += f'            <li><strong>Type:</strong> {characteristics["type"]}</li>'
    output += """
        </ul>
    </li>
    """
    return output

# Collect all serialized animal data
output = ''
for fox in foxes:
    output += serialize_animal(fox)

# Load the template HTML file
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Replace the placeholder in the template with the generated output
html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

# Save the final HTML content to a new file
with open('animals.html', 'w', encoding="utf-8") as file:
    file.write(html_content)

# Print the HTML content
print(html_content)
