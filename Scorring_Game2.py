import random
import json
import datetime
from operator import itemgetter

current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0
score_link = "score_list.json"
wrong_guesses = []

with open(score_link, "r") as score_file:
    score_list = json.loads(score_file.read())
    sorted_score_list = sorted(score_list, key=itemgetter("attempts"))
    for score_dict in sorted_score_list[:3]:
        wrong_guesses_string = ', '.join(str(e) for e in score_dict["wrong_guesses"])
        score_text = "{0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}.".format(
            score_dict["player_name"],
            score_dict["attempts"],
            score_dict["time"],
            score_dict["secret_number"],
            wrong_guesses_string)

        print(score_text)

player_name = input("Player Name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append(
            {
                "player_name": player_name,
                "attempts": attempts,
                "time": str(current_time),
                "secret_number": str(secret),
                "wrong_guesses": wrong_guesses
            }
        )

        with open(score_link, "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")

    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
