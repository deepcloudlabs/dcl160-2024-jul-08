x = 42  # scalar
# 4, 8, 15, 16, 23, 42
# "jack", "kate", "james", "ben", "jin", "sun"
"""
    Collections:
    i. linear collection
        1. tuple -> ordered, immutable, allows duplicates
          numbers = (4, 8, 15, 16, 23, 42)
        2. list -> ordered, mutable, allows duplicates
          numbers = [4, 8, 15, 16, 23, 42, 15, 8, 15]
        3. set -> un-ordered, mutable, unique
        numbers = {4, 8, 15, 16, 23, 42}
    ii. associative collection
        1. dict(inoary): key --> value
        str --> int
        str --> dict: str->int
        area_codes = {
            "izmir": 232,
            "ankara": 312,
            "istanbul": {
                "anadolu": 216,
                "avrupa": 212
            }
        }
        area_codes["istanbul"]["avrupa"]
        area_codes["izmir"]
"""
