import json


def load_data(file_path):
    """ Loads a JSON file """
    with (open(file_path, "r") as handle):
        return json.load(handle)


def get_animal_info(animals_list):
    """This function retrieves the name, diet, location and, if provided, type
    of each animal and returns it in a string."""
    name_diet_location_type = ""
    for animal in animals_list:
        name_diet_location_type += '<li class="cards__item">'
        name_diet_location_type += f"Name: {animal["name"]}<br>\n"
        name_diet_location_type += f"Diet: {animal["characteristics"]["diet"]}<br>\n"
        name_diet_location_type += f"Location: {animal["locations"][0]}<br>\n"
        if "type" in animal["characteristics"]:
            name_diet_location_type += f"Type: {animal["characteristics"]["type"]}<br>\n"
        name_diet_location_type += '</li>'
    return name_diet_location_type


def main():
    """This function reads animal data from 'animals_data.json', inserts it into 'animals_template.html',
    and writes the result to 'new_animals_template.html'."""

    animals_data = load_data('animals_data.json')
    formatted_data = get_animal_info(animals_data)

    with open("animals_template.html", "r") as file:
        animals_template_content = file.read()
        actual_animal_data = animals_template_content.replace("__REPLACE_ANIMALS_INFO__", formatted_data)
        print(actual_animal_data)

    with open("new_animals_template.html", "w") as file:
        file.write(actual_animal_data)


if __name__ == "__main__":
    main()
