print ("Guess a Number From 1 to 100")
import random
guesses = 5
num = random.randint(1,100)
answer = 0 
while num!= answer and guesses > 0 :
  answer = int (input("guess the Number"))
  guesses -= 1 
  if answer < num:
    print ("Higher Number Of Guesses Left: " +str (guesses))
    if answer > num:
      print ("Lower, number of the guesses left : " +str guesses))
      else:
        print ("Correct, the number was: " +str (guesses))
        if answer !+ num:
          print ("That was your last last guess, sorry,the number was: " +str(num)
