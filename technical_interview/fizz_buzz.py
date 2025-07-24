'''
FizzBuzz is a common programming challenge where you print numbers from 1 to 100, but for multiples of 3, you print "FIZZ" instead of the number, and for multiples of 5, you print "BUZZ". For numbers that are multiples of both 3 and 5, you print "FIZZ BUZZ".
For example, the output for numbers 1 to 15 would be:
'''


def fizz_buzz():
    for i in range(1,100):
        if i%3==0:
            print(f"{i} FIZZ")
        elif i%5==0:
            print(f"{i} BUZZ")
        elif i%3==0 and i%5==0:
            print(f"{i} FIZZ BUZZ")
    
    
fizz_buzz()