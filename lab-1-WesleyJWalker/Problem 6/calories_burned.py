''' 
Write a program to take in the four inputs and calculate the average calories burned.
Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 

Name: Wesley Walker
Lab Time: Thursday @ 2PM
'''

def calculate_calories_burned():
    #Type your code here
    #Get input make sure it is numeric
    age_years = float(input())
    weight = float(input())
    heartRate = float(input())
    time = float(input())
    calsBurned = ((((0.2757 * age_years) + (0.03295 * weight) + (1.0781 * heartRate) - 75.4991) * time)/8.368)
    print(f'Calories: {calsBurned:.2f} calories')

if __name__ == "__main__":
    calculate_calories_burned()