# car-customizer.py
# Define car brands, models, trims, and years
brands = ('Porsche', 'BMW', 'Audi', 'Mercedes')
porsche_years = [2012, 2016, 2022, 2025]
bmw_years = [2018, 2023, 2025]
audi_years = [2015, 2020, 2024]
mercedes_years = [2015, 2022, 2023]

#porsche models and trims
models_porsche = ['911', 'Cayman', 'Panamera']
trims_porsche = ['Base', 'S', 'GTS',]

#bmw models and trims
models_bmw = ['M3', 'M4', 'M5']
trims_bmw = ['Base', 'Competition', 'CS']

#audi models and trims
models_audi = ['RS3', 'RS6', 'R8']
audi_trims = ['Base', 'Performance', 'V10']

#mercedes models and trims
models_mercedes = ['C63', 'SL63', 'GT63']
trims_mercedes = ['Base', 'S', ]

#wheel options
wheel_options = ['18-inch', '19-inch', '20-inch', '21-inch']
wheel_brand = ['OEM', 'Volk Racing', 'BBS', 'HRE']
color_options = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Yellow']

# cosmetic options
cosmetic_options = ['Spoiler', 'Body Kit', 'Tinted Windows', 'Custom Paint']
paint_colors = ['Matte Black', 'Ruby Star Pink', 'Metallic Blue', 'Pearl Red']

# Function to display options and get user selection
choice1 = input("Welcome to the Car Customizer!\nSelect a brand:\n1. Porsche\n2. BMW\n3. Audi\n4. Mercedes\nEnter the number of your choice: ")

if choice1 == '1':
    brand = 'Porsche'
    models = models_porsche
    trims = trims_porsche  
    years = porsche_years
elif choice1 == '2':
    brand = 'BMW'
    models = models_bmw
    trims = trims_bmw
    years = bmw_years
elif choice1 == '3':
    brand = 'Audi'
    models = models_audi
    trims = audi_trims
    years = audi_years
elif choice1 == '4':
    brand = 'Mercedes'
    models = models_mercedes
    trims = trims_mercedes
    years = mercedes_years
else:
    print("Invalid choice. Exiting.")
    exit()

# Model selection
print("Select a model:")
for idx, model in enumerate(models, 1):
    print(f"{idx}. {model}")
model_choice = input("Enter the number of your choice: ")
selected_model = models[int(model_choice)-1] if model_choice.isdigit() and 1 <= int(model_choice) <= len(models) else None

# Trim selection
print("Select a trim:")
for idx, trim in enumerate(trims, 1):
    print(f"{idx}. {trim}")
trim_choice = input("Enter the number of your choice: ")
selected_trim = trims[int(trim_choice)-1] if trim_choice.isdigit() and 1 <= int(trim_choice) <= len(trims) else None

# Year selection
print("Select a year:")
for idx, year in enumerate(years, 1):
    print(f"{idx}. {year}")
year_choice = input("Enter the number of your choice: ")
selected_year = years[int(year_choice)-1] if year_choice.isdigit() and 1 <= int(year_choice) <= len(years) else None

# Wheel selection
print("Select a wheel size:")
for idx, wheel in enumerate(wheel_options, 1):
    print(f"{idx}. {wheel}")
wheel_choice = input("Enter the number of your choice: ")
selected_wheel = wheel_options[int(wheel_choice)-1] if wheel_choice.isdigit() and 1 <= int(wheel_choice) <= len(wheel_options) else None

print("Select a wheel brand:")
for idx, wbrand in enumerate(wheel_brand, 1):
    print(f"{idx}. {wbrand}")
wbrand_choice = input("Enter the number of your choice: ")
selected_wbrand = wheel_brand[int(wbrand_choice)-1] if wbrand_choice.isdigit() and 1 <= int(wbrand_choice) <= len(wheel_brand) else None

# Color selection
print("Select a color:")
for idx, color in enumerate(color_options, 1):
    print(f"{idx}. {color}")
color_choice = input("Enter the number of your choice: ")
selected_color = color_options[int(color_choice)-1] if color_choice.isdigit() and 1 <= int(color_choice) <= len(color_options) else None

# Cosmetic options (multiple selection)
print("Available cosmetic options:")
for idx, option in enumerate(cosmetic_options, 1):
    print(f"{idx}. {option}")
selected = input("Enter the numbers of the cosmetic options you want (separated by commas): ")
selected_indices = [int(x.strip()) for x in selected.split(",") if x.strip().isdigit()]
chosen_cosmetics = [cosmetic_options[i-1] for i in selected_indices if 1 <= i <= len(cosmetic_options)]

chosen_paint = None
if 'Custom Paint' in chosen_cosmetics:
    print("Available paint colors:")
    for idx, paint in enumerate(paint_colors, 1):
        print(f"{idx}. {paint}")
    paint_choice = input("Enter the number of the paint color you want: ")
    if paint_choice.isdigit() and 1 <= int(paint_choice) <= len(paint_colors):
        chosen_paint = paint_colors[int(paint_choice)-1]

# Show summary
print("\nYour selections:")
print(f"Brand: {brand}")
print(f"Model: {selected_model}")
print(f"Trim: {selected_trim}")
print(f"Year: {selected_year}")
print(f"Wheel: {selected_wheel} ({selected_wbrand})")
print(f"Color: {selected_color}")
print(f"Cosmetic options: {chosen_cosmetics}")
if chosen_paint:
    print(f"Custom Paint Color: {chosen_paint}")