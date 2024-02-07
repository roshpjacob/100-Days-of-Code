print("BMI Categories:\n"
      "Underweight = <18.5\nNormal weight = 18.5-24.9\nOverweight = 25-29.9\nObesity falls in BMI>=30\n")

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in metres: '))
bmi = weight/(height**2)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("According to your BMI, you are underweight")
elif 18.5 <= bmi < 25:
    print("According to your BMI, your weight is normal.")
elif 25 <= bmi < 30:
    print("According to your BMI, you are OVERWEIGHT!"+
          "\nTake precautions in order to avoid obesity and get into normal weight")
else:
    print("According to your BMI, you are OBESE! "+
          "\nConsult physicians and professional trainers for strict diets and workout routines")

