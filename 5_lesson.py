import file_operations
import random
import os
from faker import Faker

fake = Faker("ru_RU")

output_dir = os.path.join(r"C:\python_scripts\5_lesson")
person_cards_dir = os.path.join(output_dir, "person_cards")
os.makedirs(person_cards_dir, exist_ok=True)

skills = [skill.replace("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                        "а͠б̋в͒͠г͒͠д̋е͠ё͒͠ж͒з̋̋͠ий͒͠к̋̋л̋͠м͒͠н͒о̋п̋͠р̋͠с͒т͒у͒͠ф̋̋͠х͒͠ц̋ч̋͠ш͒͠щ̋ъ̋͠ы̋͠ь̋э͒͠͠ю̋͠я̋А͠Б̋В͒͠Г͒͠Д̋ЕЁ͒͠Ж͒З̋̋͠ИЙ͒͠К̋̋Л̋͠М͒͠Н͒О̋П̋͠Р̋͠С͒Т͒У͒͠Ф̋̋͠Х͒͠Ц̋Ч̋͠Ш͒͠Щ̋Ъ̋͠Ы̋͠Ь̋Э͒͠͠Ю̋͠Я̋")
          for skill in ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар"]]
skills.append("Стремительный прыжок")
skills.append("Электрический выстрел")
skills.append("Ледяной удар")

def main():
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