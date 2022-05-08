
class IQ_Game:
    def __init__(self):
        while True:
            print(''' Welecoom To IQ Game
                        Please choose the game you want to play:
                        1- Guessesing Game
                        2- Quiz Game
                        3- rockPaperScissorsGame
                        4- Translate
                       
                        (if you want to quit the game, please press the "X")

            ''')
            choose = input()
            if choose == "X":
                print("Good Bye :)")
                break

            if int(choose) == 1:
                print('''Welecoom To Guessesing Game :) 

                        It is a game in which you predict the given word while giving you specific opportunities to try
                    ''')
                self.guessesingGame()

            if int(choose) == 2:
                print('''Welecoom To Quiz Game :) 

                        It is a game that tests you with questions in the field of hardware
                    ''')
                self.quizGame()

            if int(choose) == 3:
                print("Welecoom To Rock Paper Scissors Game :) ")

                self.rockPaperScissorsGame()

            if int(choose) == 4:
                print('''Welecoom To Translate Game :) 

                        It is a game that replaces all the letters of the sentence "A" to "X".
                    ''')
                self.translate()

    def guessesingGame(self):

        secret_word = "AhmadZa"
        guess = ""
        guess_count = 0
        guess_limit = 4
        out_of_guesses = False
        print(
            f"Welcome to Guessing Game \n The word you would expect consists of {len(secret_word)} letters \n The first letter is {secret_word[0]}, the last letter is {secret_word[-1]}")

        while guess != secret_word.lower() and not out_of_guesses:
            if guess_count < guess_limit:
                print(f"You have {guess_limit} attempts")
                guess = input("Enter guess:")
                guess_limit -= 1

                if guess_limit == 2:
                    Hint = input("Do you want a hint (Y \ N):")
                    if Hint.upper() == "N":
                        print(f"You have {guess_limit} attempts")
                        continue
                    elif Hint.upper() == "Y":
                        print(f"Hint: {secret_word[:3]} ")

                if guess_limit == 0:
                    continue

            else:
                out_of_guesses = True

        if out_of_guesses:
            print("You lost in the guessing game")

        else:
            print("You Win")

    def quizGame(self):

        print("Welcome to Quiz Game")
        scores = 0
        quastions = 0
        playing = input("Do you Want to Play? ")

        if playing != "yes":
            quit()

        print("Ok, Let's Play :")

        answer = input("What is CPU stands for? ")
        quastions += 1
        if answer.lower() == "central processing unit":
            print("Correct :)")
            scores += 1
        else:
            print("Not Correct :(")

        answer = input("What is GPU stands for? ")
        quastions += 1
        if answer.lower() == "graphics processing unit":
            print("Correct :)")
            scores += 1
        else:
            print("Not Correct :(")

        answer = input("What is RAM stands for? ")
        quastions += 1
        if answer.lower() == "random access memory":
            print("Correct :)")
            scores += 1
        else:
            print("Not Correct :(")

        answer = input("What is PSU stands for? ")
        quastions += 1
        if answer.lower() == "power supply":
            print("Correct :)")
            scores += 1
        else:
            print("Not Correct :(")

        print(f"You got {scores} answers correct !")
        print(f"You get {(scores / quastions) * 100} answer correct!")

    def rockPaperScissorsGame(self):
        import random

        user_wins = 0
        computer_wins = 0

        options = ["rock", "paper", "scissors"]

        while True:
            user_input = input("Type Rock, Paper or Scissors or Q to quit")

            if user_input == "q":
                break

            if user_input not in options:
                continue

            random_number = random.randint(0, 2)
            computer_pick = options[random_number]

            print(f"Computer picked {computer_pick}.")

            if user_input == "rock" and computer_pick == "scissors":
                print("You Win!")
                user_wins += 1

            elif user_input == "scissors" and computer_pick == "paper":
                print("You Win!")
                user_wins += 1

            elif user_input == "paper" and computer_pick == "rock":
                print("You Win!")
                user_wins += 1

            else:
                print("You Lost!")
                computer_wins += 1

        print(f"You won {user_wins} times.")
        print(f"Ther computer won {user_wins} times.")
        print("Goodby :)")

    def translate(self):

        str = input("Enter a Phrase: ")
        translation = ""
        while True:
            for letter in str:
                if letter.lower() in "aeiou":
                    if letter.isupper():
                        translation += "X"
                    else:
                        translation += "x"

                else:
                    translation += letter
            print(translation)
            return translation


IQ_Game()
