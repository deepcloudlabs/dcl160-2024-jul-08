import re

meyveler = ["elma", "armut", "kiraz", "nar", "şeftali", "muz",
            "karpuz", "kavun", "kivi", "böğürtlen", "vişne", "karadut",
            "çilek", "kızılcık", "incir", "frenk üzümü", "ahududu", "12345"
            ]
pattern1 = "....."
pattern2 = "[a-z][a-z][a-z][a-z][a-z]"
pattern3 = "[a-z]{5}"
pattern4 = "[a-zıçöüğş ]{5}"
pattern5 = "[a-zıçöüğş ]{,5}"
pattern6 = "[a-zıçöüğş ]{5,}"
pattern7 = "\\W{5}"
for meyve in meyveler:
    if re.fullmatch(pattern7, meyve):
        print(meyve)
