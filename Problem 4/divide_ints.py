'''
Write a program that reads in two integers and prints their quotient 3 times

Name: Wesley Walker
Lab Time: Thursday @ 2PM

'''
def divide_ints():
    #Type your code here
    #Get input make sure it is numeric
    user_num = int(input())
    div_num = int(input())
    print((user_num // div_num),'',((user_num // div_num) // div_num),'',(((user_num // div_num) // div_num)// div_num))

    
if __name__ == "__main__":
    divide_ints()