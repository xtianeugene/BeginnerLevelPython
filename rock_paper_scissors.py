import random


def main():
     choices = ["rock", "paper", "scissors"]
     score = {"you": 0, "cpu": 0}
     while True:
         you = input("rock/paper/scissors (or 'q' to quit): ").lower()
         if you == "q":
             break
         if you not in choices:
             continue
         cpu = random.choice(choices)
         print(f"CPU chose {cpu}")
         if you == cpu:
             print("Tie!")
         elif (you, cpu) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
             print("You win!")
             score["you"] += 1
         else:
             print("CPU wins!")
             score["cpu"] += 1
         print(f"Score: You {score['you']} - CPU {score['cpu']}")

if __name__ == "__main__":
     main()