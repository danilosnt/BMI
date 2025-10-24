# BMI Calculator

This command-line tool prompts the user to enter their weight in kilograms (kg) and their height in meters (m).

It then calculates the BMI value based on the formula $BMI = \frac{\text{weight}}{\text{height}^2}$ and prints the result, along with its corresponding classification.

The script also includes basic error handling for invalid inputs (like non-numeric values or a height/weight of zero).

## Classifications

The calculation uses the following standard classifications:

* **Less than 18.5:** Underweight
* **18.5 to 24.9:** Normal weight
* **25.0 to 29.9:** Overweight
* **30.0 to 34.9:** Obesity Class I
* **35.0 to 39.9:** Obesity Class II
* **40.0 or greater:** Obesity Class III (Morbid)
