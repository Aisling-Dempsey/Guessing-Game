from random import randint

# greet player
# get player name
# choose random number between 1 and 100
# while True:
#     get guess
#     if guess is incorrect:
#         give hint
#     else:
#         congratulate player

name = raw_input("What's your name? ")
number = randint(1,100)
list_guess = []
guess = None

print "Hi, %s! Let's play a guessing game." % name 
print "Don't tell anyone, but the number is " + str(number)
print "Shhh...The number is %d" % number

# This is the while loop - in progress!
while guess != number:
    guess = int(raw_input("Guess a number between 1 and 100: " ))

    if guess in list_guess:
        print "You've already guessed that, try again!"

    elif 1 > guess  or guess > 100 :
        print "You're way out of range! What are you smoking?"
        list_guess.append(guess)

    elif guess > number:
        print "Too high, guess again."
        list_guess.append(guess)

    elif guess < number:
        print 'Your guess is too low, try again!'
        list_guess.append(guess)

if guess == number:
    list_guess.append(guess)
    print "Congratulations! You've guessed the number! It took you %d guesses." % len(list_guess)


#this is the recursive method

# def game():
#     guess = int(raw_input("Guess a number between 1 and 100: " ))
#     # print guess

#     if guess in list_guess:
#         print "You've already guessed that, try again!"
#         game()

#     elif 1 > guess  or guess > 100 :
#         print "You're way out of range! What are you smoking?"
#         list_guess.append(guess)
#         game()

#     elif guess < number:
#         print 'Your guess is too low, try again!'
#         list_guess.append(guess)
#         game()

#     elif guess > number:
#         print "Your guess is too high, try again!"
#         list_guess.append(guess)
#         game()

#     else:
#         print "Congratulations! You've guessed the number! It took you %d guesses." % len(list_guess)

# game()