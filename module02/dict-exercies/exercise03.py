area_codes = {
    "izmir": 232,
    "ankara": 312,
    "istanbul": {
        "anadolu": 216,
        "avrupa": 212
    }
}
first_city, second_city, *others = area_codes  # unpacking keys
print(first_city)
print(second_city)
print(others)
