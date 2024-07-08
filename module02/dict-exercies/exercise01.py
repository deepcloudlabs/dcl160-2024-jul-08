# dictionary
area_codes = {
    "izmir": 232,
    "ankara": 312,
    "istanbul": {
        "anadolu": 216,
        "avrupa": 212
    }
}
print(area_codes["ankara"])
area_codes["antalya"] = 242
print(area_codes["antalya"])
print(area_codes.keys())
print(area_codes.values())
print(area_codes.items())  # pair(key,value) -> tuple
