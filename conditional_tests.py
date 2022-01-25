my_name = "Mehmet"
if my_name == "Mehmet":
    print("Beste navnet på jord")

if my_name != "Mehmet":
    print("Du har ikke det beste navnet")

if my_name.lower() == "mehmet":
    print("HVORFOR SKRIVER DU THE MAN NAME PÅ SMÅ BOKSTAVER?")

age = 18
under_age = 17
if age == 18:
    print(f"Du kan dra på utesteder fordi du er {age} år!")

if age != 18:
    print(f"Du er ikke med i 18 years old gang")

if age > 18:
    print(f"Du er over 18 år, du er {age} år!")

if age < 18:
    print(f"Du er for liten til å dra på fester fordi du er under 18, du er {age} år!")

if under_age < 18 or age == 17:
    print("Du er 17 år, du må vente ett år til!")

mad_list = ["cake", "sandwich", "coke"]

if "cake" in mad_list:
    print("I love cake!")

if "cake" not in mad_list:
    print("I want cake!")

