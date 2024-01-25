'''
In this assignment you will write a program that takes in three inputs (x,y,z) and 
uses the math module to output x to the power of z, x to the power of (y to the power of z), 
the absolute value of (x-y), and the square root of (x to the power of z).

Name: Wesley Walker
Lab Time: Thursday @ 2PM

'''
import math

def math_func():
    #Type your code here
    x = float(input())
    y = float(input())
    z = float(input())
    pow1 = math.pow(x,z)
    pow2 = math.pow(x, math.pow(y,z))
    abs = math.fabs(x - y)
    sqr = math.sqrt(math.pow(x,z))
    print(f'{pow1:.2f} {pow2:.2f} {abs:.2f} {sqr:.2f}')

    print()
    
if __name__ == "__main__":
    math_func()