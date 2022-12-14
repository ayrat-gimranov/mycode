#!/usr/bin/python3

def main():
    classinfo = {
    "all": [
        {
            "name": "Aaron",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Alexandra",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Alice",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Angela",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Ayrat",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Blake",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Shape of: A Giant Shark",
        },
        {
            "name": "Brandon",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Carl",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Transformation",
        },
        {
            "name": "Chris",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Pyrokinesis",
        },
        {
            "name": "Christian",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Deepak",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Explosive Shouts",
        },
        {
            "name": "Dennis",
            "skill level": "great",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Felicia",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Zoolingualism",
        },
        {
            "name": "Gabriel",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Height Manipulation",
        },
        {
            "name": "Julian",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Hydrokinesis",
        },
        {
            "name": "Kelly",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lashay",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Stretchy",
        },
        {
            "name": "Nabin",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Steel Skin",
        },
        {
            "name": "Pratibha",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Teleportation",
        },
        {
            "name": "Quentin",
            "skill level": "remarkable",
            "spirit animal": "Lynx",
            "super power": "Polyglot",
        },
        {
            "name": "Will",
            "skill level": "super",
            "spirit animal": "Fox",
            "super power": "Eat Anything",
        }]
    }
    
    info = classinfo.get('all')

    # part 1, 2

    my_input = input('WHat is your name?')
    for student in info:

        if student.get('name') == my_input:
            print(student.get('name'))

            name = student.get('name')
            spirit_animal = student.get('spirit animal')
            skills = student.get('skill level')
            super_power = student.get('super power')
            
            print(f"My name is {name} and my spirit animal is {spirit_animal}.")
            print(f"My name is {name} and my skills are {skills}.")
            print(f"My name is {name} and my super power is {super_power}.")
    
    # part 3
    for student in info:
    
        name = student.get('name')
        spirit_animal = student.get('spirit animal')
        skills = student.get('skill level')
        super_power = student.get('super power')

        print(f"{name}, a {skills} {spirit_animal} of a programmer, possesses a {super_power} factor for moonlighting as a superhero!")

if __name__ == "__main__":
    main()
