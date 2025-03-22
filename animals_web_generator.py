import json


def load_data(file_path):
    """ Loads a JSON file """
    with (open(file_path, "r") as handle):
        return json.load(handle)


def get_animal_info(animals_list):
    output = ""
    for animal in animals_list:
        output += f"Name: {animal["name"]}<br>\n"
        output += f"Diet: {animal["characteristics"]["diet"]}<br>\n"
        output += f"Location: {animal["locations"][0]}<br>\n"
        if "type" in animal["characteristics"]:
            output += f"Type: {animal["characteristics"]["type"]}<br>\n"
        output += "<br>\n"
    return output


def main():
    animals_data = load_data('animals_data.json')
    formatted_data = get_animal_info(animals_data)

    with open("animals_template.html", "r") as file:
        template_content = file.read()
        replace_text = template_content.replace("__REPLACE_ANIMALS_INFO__", formatted_data)
        print(replace_text)

    with open("new_animals_template.html", "w") as file:
        file.write(replace_text)


if __name__ == "__main__":
    main()
