print("Welcome to my General Football Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Then let's play")
score = 0

answer = input("Which footballer has won the Premier League with both Leicester City and Manchester City?")
if answer.lower() == "riyad mahrez":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is Juventus’ nickname?")
if answer.lower() == "the old lady":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which striker was the first to score more than 20 goals in the Premier League for 5 consecutive seasons?")
if answer.lower() == "thierry henry":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("As of 2023, how many Ballon d’Or awards has Lionel Messi won?")
if answer.lower() == "7":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which nation has won the African Cup of Nations the most?")
if answer.lower() == "egypt":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which player holds the record for the most goals scored in a single Premier League season?")
if answer.lower() == "erling haaland":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who scored the fastest hat-trick in Premier League history?")
if answer.lower() == "sadio mane":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the first African player to win the FIFA World Player of the Year award?")
if answer.lower() == "george weah":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " +str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")