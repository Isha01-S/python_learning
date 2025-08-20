'''7. Write a python function to remove a given word from a list and strip it at the same
time.'''
def rem(l, word):
    n= []
    for item in l:
        if not(word==item):
            n.append(item.strip(word))
    return n


l=["Isha", "Diya", "Bhagyashree", "Kriti","a"]

print(rem(l,"a"))
