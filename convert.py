import json
import re

# Store dictionary keys to lookup later, to ensure they remain in order
intro_url_list = [
    "title-page",
    "bofm-title",
    "introduction",
    "three",
    "eight",
    "js",
    "explanation"
]

books_and_number_of_chapters = {
    "1-ne": 22,
    "2-ne": 33,
    "jacob": 7,
    "enos": 1,
    "jarom": 1,
    "omni": 1,
    "w-of-m": 1,
    "mosiah": 29,
    "alma": 63,
    "hel": 16,
    "3-ne": 30,
    "4-ne": 1,
    "morm": 9,
    "ether": 15,
    "moro": 10
}

# Load the data from json files
def load_data(lang:str) -> dict:
    # Encoding must be specified, as .json files are usually ascii
    with open(f"data/{lang}.json", "r", encoding="utf8") as file:
        return json.load(file)


# Remove any bbcode flags if desired
def remove_bbcode(chapter:str) -> str:
    return re.sub("\[[^\]]+\]", "", chapter)


# Save the data once it is converted
def save_data(data_to_save, filename:str) -> None:
    # Encoding specified to accommodate any language
    with open(filename, "w", encoding="utf8") as file:
        file.write(data_to_save)


# Iterates through the dictionary data and converts it into a string
def convert_dictionary_to_string(data_to_convert:dict) -> str:
    return_string = ""
    for code in intro_url_list:
        return_string += data_to_convert[code + " 0"]
    for code in books_and_number_of_chapters.keys():
        for i in range(books_and_number_of_chapters[code]):
            return_string += data_to_convert[f"{code} {i+1}"]
    return return_string


# Call this function to convert a .json file into a .txt file
def convert_to_txt(lang:str, include_bbcode:bool=True) -> None:
    json_data = load_data(lang)
    string_data = convert_dictionary_to_string(json_data)
    if not include_bbcode:
        string_data = remove_bbcode(string_data)
    save_data(string_data, f"{lang}.txt")


# Uncomment and change arguments to fit your needs
convert_to_txt("fra", False)
