import random
while True:
  user_choice=int(input("Enter your choice(0 for Rock,1 for Paper and 3 for Scissor):"))
  computer_choice=random.randint(0,2)
  print("Computer Choice:")
  print(computer_choice)

  if computer_choice==user_choice:
                print("It's a draw")
  elif computer_choice==2 and user_choice==0:
                print("You lose")
  elif computer_choice==0 and user_choice==2:
                print("You win")
  elif computer_choice>user_choice:
                print("You lose")
  elif computer_choice<user_choice:
                print("You win")
  else:
                break
