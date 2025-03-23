import json


def load_data(file_path):
    """ Loads a JSON file """
    with (open(file_path, "r") as handle):
        return json.load(handle)


def serialize_animal(animal_obj):
    """This function allows for the serialization of a single animal object."""
    name_diet_location_type = ''
    name_diet_location_type += '<li class="cards__item">\n'
    name_diet_location_type += f'<div class="card__title">{animal_obj["name"]}</div>\n</br>'
    name_diet_location_type += f'<div class="card__text"><b>Diet: </b>{animal_obj["characteristics"]["diet"]}<br>\n'
    name_diet_location_type += f'<div class="card__text"><b>Location: </b>{animal_obj["locations"][0]}<br>\n'
    if "type" in animal_obj["characteristics"]:
        name_diet_location_type += f'<div class="card__text"><b>Type: </b>{animal_obj["characteristics"]["type"]}<br>\n'
    return name_diet_location_type


def get_animal_info(animals_list):
    """This function returns the animals' name, diet, location and, if provided, type in a string."""
    name_diet_loc_type = ""
    for animal in animals_list:
        name_diet_loc_type += serialize_animal(animal)
    return name_diet_loc_type


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
