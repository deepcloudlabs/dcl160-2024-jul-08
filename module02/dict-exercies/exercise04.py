area_codes = {
    "izmir": 232,
    "ankara": 312,
    "istanbul": {
        "anadolu": 216,
        "avrupa": 212
    }
}

print("ankara" in area_codes)
print("edirne" in area_codes)
print(area_codes["ankara"])
cities = {  # dictionary
    "ege": [  # list -> set
        {  # dictionary
            "izmir": (100000, 23345)  # tuple
        }
    ]
}
