import random

def user (x):
     random_comp_no=random.randint(0,x)
     userno=int(input(f"enter number from 0 to {x}"))
     print(f"the computers no is {random_comp_no}")
     if userno==random_comp_no:
         print("YAY, congrats  YOU GUESSED THE RIGHT NO")


     while userno != random_comp_no:
          userno= int(input("enter a new number : "))
          if userno < random_comp_no:
             print("please enter a new greater no ")
          elif userno > random_comp_no:
             userno=int(input(f"please enter a new number lesser than previous number : "))
          elif userno==random_comp_no:
              print(" congrats , you've guessed the riight nooo :")






def computer_guess(x):
     low=1
     high=x
     user_response=""
     while user_response!='c':


         if low !=high:
             guess_comp = random.randint(low, high)
         else:
              guess_comp=low
         user_response = input(f"computer guess {guess_comp}, is it low (l) , high (h) or correct (c)?")
         if user_response == 'l':
            low = guess_comp + 1
         elif user_response == 'h':
            high = guess_comp - 1

     print("computer guessed the right number")


computer_guess(10)
