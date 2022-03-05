import random
high=1000
low=1
guesses=1
print("think of a number from {} to {}. I will guess it within 10 tries.".format(low,high))

answer=random.randint(low,high)
while True:
    guess = low + (high-low) // 2
    x=input("my guess is {} please press h if the number is higher l if the number is lower, or c if the guess is correct ".format(guess)).casefold()
    if x=="h":
        low=guess + 1 
       
    elif x=="l":
        high = guess-1
        
    elif x == "c":
        print("noce i got it in {} tries".format(guesses))
        break
    else:
        print("hit h,l,c")
guesses+=guesses+1