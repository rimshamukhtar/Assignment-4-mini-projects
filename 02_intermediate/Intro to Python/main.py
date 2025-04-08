# Planetary Weight Calculator

# Dictionary to store gravitational constants for each planet
planet_gravity = {
    'Mercury': 37.6,
    'Venus': 88.9,
    'Mars': 37.8,
    'Jupiter': 236.0,
    'Saturn': 108.1,
    'Uranus': 81.5,
    'Neptune': 114.0
}

def main():
    # Prompt the user to enter their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user to enter the planet name
    planet = input("Enter a planet: ")

    # Check if the entered planet is valid
    if planet in planet_gravity:
        # Calculate the weight on the selected planet
        planet_weight = earth_weight * (planet_gravity[planet] / 100)
        
        # Output the equivalent weight on that planet rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        print("Invalid planet name entered.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
