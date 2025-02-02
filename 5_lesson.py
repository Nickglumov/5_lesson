import file_operations
import random
import os
from faker import Faker

fake = Faker("ru_RU")

output_dir = os.path.join(r"C:\python_scripts\5_lesson")
person_cards_dir = os.path.join(output_dir, "person_cards")
os.makedirs(person_cards_dir, exist_ok=True)

skills = [skill.replace("Стремительный прыжок", "С͒т͒р̋͠е͠м͒͠и'т͒е͠л̋͠н͒ы̋͠й͒͠ п̋͠р̋͠ы̋͠ж͒о̋к̋̋")
        for skill in ["Стремительный прыжок","Электрический выстрел", "Ледяной удар"]]
new_skills = ["Э͒͠͠л̋͠е̋͠к̋̋'т͒р̋͠и'ч̋͠е͠с͒'к̋̋и'й͒͠ в͒͠ы̋͠с͒т͒р̋͠е͠л̋͠", "Л̋͠е͠д̋я̋н͒о̋й͒͠ у͒͠д̋а͠р̋͠"]
for skill in new_skills:
    skills.append(skill)
select_skills = random.sample(skills,3)

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

