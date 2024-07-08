ege = {"izmir": 232}
akdeniz = {"antalya": 242}
marmara = {"istanbul": {
    "anadolu": 216,
    "avrupa": 212
}}
cities = {*ege, *marmara, *akdeniz}  # packing keys
print(cities)
area_codes = {**ege, **marmara, **akdeniz}  # packing items(key-->value)
print(area_codes)

