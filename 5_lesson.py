import os
import random

from faker import Faker

import file_operations


def get_translate_skills():
    skills = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Ледяной выстрел",
        "Огненный заряд"
    ]
    runnic_letters = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }
    runnic_skills = []
    for skill in skills:
        split_skills = list(skill)
        translate_skill = skill
        for char in split_skills:
            translate_skill = translate_skill.replace(char, runnic_letters.get(char))
        runnic_skills.append(translate_skill)
    return runnic_skills


def main():
    fake = Faker("ru_RU")

    output_dir = ("person_cards")
    person_cards_dir = os.path.join(output_dir, "person_cards")
    os.makedirs(person_cards_dir, exist_ok=True)
    skills = get_translate_skills()
    for result_card in range(10):
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        select_skills = random.sample(skills, 3)

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": select_skills[0],
            "skill_2": select_skills[1],
            "skill_3": select_skills[2]
        }

        output_filename = os.path.join(person_cards_dir, "result{}.svg".format(result_card + 1))
        file_operations.render_template("charsheet.svg", output_filename, context)


if __name__ == "__main__":
    main()
