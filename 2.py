#lab3 4.py modefy it
#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def filter_prime(thislist):
    for x in thislist:
        if x==1 or x==0:
            continue
        else:
            for y in range (2, int(x/2)+1):
                if x % y == 0:
                    break
            else:
                print(x)

mylist = [1, 6, 9, 0, 4, 11, 19, 20, 2]
newlist=filter_prime(mylist)

        