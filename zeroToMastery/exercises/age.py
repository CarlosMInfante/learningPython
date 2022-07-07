from datetime import date

birth_year = input("What year were you born? ")
current_year = date.today().year
current_age = int(current_year) - int(birth_year)
print(f"Your age is {current_age}.")
