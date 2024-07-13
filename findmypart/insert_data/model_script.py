import json

marks = [
    ("Honda", "Япония"),
    ("Toyota", "Япония"),
    ("Mazda", "Япония"),
    ("Kia", "Корея"),
    ("Audi", "Германия")
]

data_marks = [
    {
        "model": "partfinder.mark",
        "pk": pk + 1,
        "fields": {
            "name": mark,
            "producer_country_name": country
        }
    } for pk, (mark, country) in enumerate(marks)]

models = [
    ("Civic", 1),
    ("Fit", 1),
    ("Accord", 1),
    ("Stepwgn", 1),
    ("CR-V", 1),
    ("Corolla", 2),
    ("Prius", 2),
    ("Yaris", 2),
    ("Aqua", 2),
    ("Vitz", 2),
    ("Mazda 3", 3),
    ("Mazda 6", 3),
    ("Mazda 2", 3),
    ("CX-30", 3),
    ("CX-50", 3),
    ("K5", 4),
    ("Rio", 4),
    ("Sportage", 4),
    ("Ceed", 4),
    ("Soul", 4),
    ("A4", 5),
    ("Q3", 5),
    ("A6", 5),
    ("A8", 5),
    ("A3", 5)

]
data_models = [
    {
        "model": "partfinder.model",
        "pk": pk + 1,
        "fields": {
            "name": name,
            "mark_id": mark_id
        }
    } for pk, (name, mark_id) in enumerate(models)
]
data_marks.extend(data_models)

with open("model_fixtures.json", "w", encoding="utf-8") as file:
    json.dump(data_marks, file, ensure_ascii=False)
