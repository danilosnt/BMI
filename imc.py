def calculate_bmi(weight, height):
    if height <= 0:
        return None
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class I"
    elif 35 <= bmi < 39.9:
        return "Obesity Class II"
    else:
        return "Obesity Class III (Morbid)"

def main():
    print("--- BMI (Body Mass Index) Calculator ---")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters, e.g., 1.75): "))

        if weight <= 0:
            print("Error: Weight must be a positive value.")
            return

        bmi = calculate_bmi(weight, height)

        if bmi is None:
            print("Error: Height must be a positive value.")
        else:
            classification = classify_bmi(bmi)
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Classification: {classification}")

    except ValueError:
        print("\nError: Please enter valid numbers for weight and height.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()