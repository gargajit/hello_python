import random

list = [2, 4, 5, 7, 8, 10]
#choice()   Returns a random element from the given sequence
q = random.choice(list)
print(q)

#choices()  Returns a list with a random selection from the given sequence
print(random.choices(list))
