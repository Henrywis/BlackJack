# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *
import copy

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# USER'S TURN
player_name = []
player_count = int(input("Welcome to Blackjack! How many players? "))
for i in range(player_count):
  score = 3
  player_name.append([input("What is player {}'s name? ".format(i+1)), score])


question = 'y'

while question == 'y':
  for player in player_name:
    user_hand = draw_starting_hand(player[0] + "'s")
    should_hit = 'y'
    while user_hand < 21:
      should_hit = (input("You have {}. Hit (y/n)? ".format(user_hand)))
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        user_hand = user_hand + draw_card()
    print_end_turn_status(user_hand)
    player.append(user_hand)
    
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)


  print_header('GAME RESULT')
  # print(player_name_copy)
  # check = print_end_game_status(player_name_copy[row][2], dealer_hand)
  
    
    

  # GAME REyySULT
  # print_header('GAME RESULT')
  # # print(player_name_copy)
  # # check = print_end_game_status(player_name_copy[row][2], dealer_hand)
  for row in range(len(player_name)):
    # player_name_copy = copy.deepcopy(player_name)
    check = print_end_game_status(player_name[row][2], dealer_hand)
    if check == 1:
      player_name[row][1] += 1
      print(player_name[row][0] + " wins! Score: " + str(player_name[row][1]))
    elif check == 0:
      print(player_name[row][0] + " pushes. Score: " + str(player_name[row][1]))
    elif check == -1:
      player_name[row][1] -= 1
      print(player_name[row][0] + " loses! Score: " + str(player_name[row][1]))
    if player_name[row][1] == 0:
        print(player_name[row][0] + " eliminated!")
    player_name[row].pop()

  player_name_copy = copy.deepcopy(player_name)
  for each_row in player_name_copy:
      if each_row[1] == 0:
        player_name.remove(each_row)

    
    # if player_name[row][1] == 0:
    #   print(player_name[row][0] + " eliminated!")
    #   player_name.remove(player_name[row])
  
  
  if len(player_name) > 0:
    question = input("Do you want to play another hand (y/n)? ")
  else:
    print("All players eliminated!")
    break

