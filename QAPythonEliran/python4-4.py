import random
print('pick number between 0-100')
high=100
low=0
x = random.randint(low, high)
sb=str(input(f"{x} is low or high?: "))
while sb!= 'right':
    if sb=='high':
        high=x-1
        x = random.randint(low, high)
        sb = input(f"{x} is low or high?: ")

    if sb=='low':
        low=x+1
        x = random.randint(low , high)
        sb = input(f"{x} is low or high?: ")
if sb=='right':
    print('you are right!')






