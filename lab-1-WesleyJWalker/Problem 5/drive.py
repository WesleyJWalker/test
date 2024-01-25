'''
Read in the users milage and cost per gallon of gas. Then output the cost to drive 20, 75, and 500 miles.

Name: Wesley Walker
Lab Time: Thursday @ 2PM
'''

def drive():
    #Type your code here
    #Get input make sure it is numeric
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    twenty = (20 * (dollars_per_gallon / miles_per_gallon))
    seventyfive = (75 * (dollars_per_gallon / miles_per_gallon))
    fivehundred = (500 * (dollars_per_gallon / miles_per_gallon))
    print(f'{twenty:.2f} {seventyfive:.2f} {fivehundred:.2f}')
    

if __name__ == "__main__":
    drive()