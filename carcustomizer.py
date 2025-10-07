# car-customizer.py
from abc import ABC, abstractmethod

# Abstract Car class (Abstraction)
class Car(ABC):
    def __init__(self, brand, model, trim, year):
        self._brand = brand          # Encapsulation (protected attribute)
        self._model = model
        self._trim = trim
        self._year = year
        self._wheels = None
        self._color = None
        self._cosmetics = []

    @abstractmethod
    def display_info(self):
        pass

    # Getter and setter for wheels (Encapsulation)
    def set_wheels(self, size, brand):
        self._wheels = f"{size} ({brand})"
    
    def get_wheels(self):
        return self._wheels
    
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def add_cosmetic(self, cosmetic):
        self._cosmetics.append(cosmetic)

    def get_cosmetics(self):
        return self._cosmetics


# Inheritance: Brand-specific classes
class Porsche(Car):
    def display_info(self):  # Polymorphism: overriding abstract method
        print(f"Porsche {self._model} {self._trim} ({self._year})")
        print(f"Color: {self._color}")
        print(f"Wheels: {self._wheels}")
        print(f"Cosmetic Options: {self._cosmetics}")

class BMW(Car):
    def display_info(self):
        print(f"BMW {self._model} {self._trim} ({self._year})")
        print(f"Color: {self._color}")
        print(f"Wheels: {self._wheels}")
        print(f"Cosmetic Options: {self._cosmetics}")

class Audi(Car):
    def display_info(self):
        print(f"Audi {self._model} {self._trim} ({self._year})")
        print(f"Color: {self._color}")
        print(f"Wheels: {self._wheels}")
        print(f"Cosmetic Options: {self._cosmetics}")

class Mercedes(Car):
    def display_info(self):
        print(f"Mercedes {self._model} {self._trim} ({self._year})")
        print(f"Color: {self._color}")
        print(f"Wheels: {self._wheels}")
        print(f"Cosmetic Options: {self._cosmetics}")


# Brand options
brands = {
    '1': ('Porsche', Porsche, ['911', 'Cayman', 'Panamera'], ['Base', 'S', 'GTS'], [2012, 2016, 2022, 2025]),
    '2': ('BMW', BMW, ['M3', 'M4', 'M5'], ['Base', 'Competition', 'CS'], [2018, 2023, 2025]),
    '3': ('Audi', Audi, ['RS3', 'RS6', 'R8'], ['Base', 'Performance', 'V10'], [2015, 2020, 2024]),
    '4': ('Mercedes', Mercedes, ['C63', 'SL63', 'GT63'], ['Base', 'S'], [2015, 2022, 2023])
}

wheel_options = ['18-inch', '19-inch', '20-inch', '21-inch']
wheel_brands = ['OEM', 'Volk Racing', 'BBS', 'HRE']
color_options = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Yellow']
cosmetic_options = ['Spoiler', 'Body Kit', 'Tinted Windows', 'Custom Paint']
paint_colors = ['Matte Black', 'Ruby Star Pink', 'Metallic Blue', 'Pearl Red']

# User selects brand
choice1 = input("Welcome to the Car Customizer!\nSelect a brand:\n1. Porsche\n2. BMW\n3. Audi\n4. Mercedes\nEnter the number of your choice: ")
if choice1 not in brands:
    print("Invalid choice. Exiting.")
    exit()

brand_name, brand_class, models, trims, years = brands[choice1]

# Model, Trim, Year selection
def select_option(options, prompt):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = input("Enter the number of your choice: ")
    return options[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= len(options) else None

selected_model = select_option(models, "Select a model:")
selected_trim = select_option(trims, "Select a trim:")
selected_year = select_option(years, "Select a year:")

# Create car instance (polymorphic behavior via parent class)
car = brand_class(brand_name, selected_model, selected_trim, selected_year)

# Wheels
selected_wheel = select_option(wheel_options, "Select a wheel size:")
selected_wbrand = select_option(wheel_brands, "Select a wheel brand:")
car.set_wheels(selected_wheel, selected_wbrand)

# Color
selected_color = select_option(color_options, "Select a color:")
car.set_color(selected_color)

# Cosmetic options
print("Available cosmetic options:")
for idx, option in enumerate(cosmetic_options, 1):
    print(f"{idx}. {option}")
selected = input("Enter the numbers of the cosmetic options you want (separated by commas): ")
selected_indices = [int(x.strip()) for x in selected.split(",") if x.strip().isdigit()]
for i in selected_indices:
    if 1 <= i <= len(cosmetic_options):
        car.add_cosmetic(cosmetic_options[i-1])

# Custom paint
if 'Custom Paint' in car.get_cosmetics():
    chosen_paint = select_option(paint_colors, "Select a custom paint color:")
    car.add_cosmetic(f"Custom Paint: {chosen_paint}")

# Show summary
print("\nYour selections:")
car.display_info()
