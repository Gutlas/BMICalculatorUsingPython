#Hello Everybody! This will be my first project on Github.
#It is a BMI Calculator made using the Python language.
KG = float(input('Enter your weight in kilograms. '))
M = float(input('Enter your height in meters. '))
BMI=(KG/M**2) #This is the formula for Calculating the BMI.
print('Your BMI is',str(BMI))

if BMI < 18.5:
    print("You are underweight. This means you are probably not getting enough calories. The average person needs 2000 calories per day. It is best if you eat some more calories and eat healthy. Try to aim for approximately 2,500 calories per day until you reach your healthy weight. Ask your doctor some more tips, and if it is good for you to diet or not.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are at a healthy weight. This means you are getting the right amount of calories, and the correct amount of exercise. Keep up the healthy diet, and the exercise!")
elif BMI >= 25.0 and BMI <=29.9:
    print("You are overweight. This means you are probably not getting enough exercise, and too much calories. Get at least 1 hour of exercise daily. Try to decrease your calories intake to 1800 per day or 1700 hundred per day till the healthy weight is reached. Eat healthy also. Ask your doctor some more tips and if it is good for you to diet or not.")
else:
    print("You are overweight. This means you are probably not getting enough exercise, and too much calories. Get at least 1 hour of exercise daily. Try to decrease your calories intake to 1600 per day or 1500 hundred per day till the healthy weight is reached. Eat healthy also. Ask your doctor some more tips and if it is good for you to diet or not.")
