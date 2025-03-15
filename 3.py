#lab3 just remember
#Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def perm(self):
    perms = permutations(self)

    res = [''.join(x) for x in perms]
    print(res)

mystring = input()
perm(mystring)