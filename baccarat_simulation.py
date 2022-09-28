import random
from math import *

#step 1
# Create Baccarat Deck & Shuffle & Discards
def create_shoe():
	cards_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 	# 13-cards created	['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 10, J, Q, K = 0 | A = 1
	deck = cards_set * 4 									          # 4 set of cards 13cards each
	table_deck = deck * 8 								          # 8 of decks for 1 table
	random.shuffle(table_deck)						          # shuffle Deck 1
	random.shuffle(table_deck)						          # shuffle Deck 2-time to be sure
	discard = table_deck[0]								          # discard process, draw 1st card of the deck
	if discard == 0: discard = 10							      # discard process, if 1st card is face or ten then discards 10
	table_deck_ready = table_deck[discard+1:]				# discard process, if 1st card is face or ten then discards 10 + 1, Else follow the number + 1
 # insert RED cards = cut cards to stop the deck from casino
	red = random.randint(290,320)			              # Get a random cut card position by random (208 = 50%) (300-320 = 25% left)
	# red = random.randint(27,30)			              # Get a random cut card position by random (208 = 50%) (260-290 = 30% left) Testing use
	table_deck_ready.insert(red,"STOP")             # Insert RED-CARD for Last round game of Baccarat cut-cards.
	check_deck = [discard, table_deck_ready ,table_deck]	#discards number, already discarded decks, original decks that has shuffle
	# print(*check_deck,sep='\n')							# To check the table deck ready
	return table_deck_ready
# play_shoe()


#Step 2
# Play the game
def play_game():										        # Game start play
  Start_Play_Deck = create_shoe()							# Take the ready deck to action and start to play the game of baccarat
  Game_results= []                         # record game results
  Win_row     = 1                               # record same winning side count / Start with 1
  Win_results = ""                        # record which side winning, P, B, T
  Win_results_past = ""                   # record which side winning, P, B, T from the past 1 game compare with past and now
  Table_deck  = Start_Play_Deck						# Mirror the ready deck for this table (So we can always check back the original deck)
  Red_Card    = False
  Game_Count  = 0                          # game counter
  win_p       = 0
  win_b       = 0
  #repeat the deck till RED-Card draw and stop
  while Red_Card == False:
      # print(Table_deck)									    # check original deck before play
      Game_Count+=1
      #draw hand from the decks
      for i in range(4):
        check_card = Table_deck.pop(0)
        if check_card == "STOP":                    #check if the red card is draw
          Red_Card = True
          # print("STOP")
          check_card = Table_deck.pop(0)
        if i == 0: player1 = check_card							#player draw 1st card
        if i == 1: banker1 = check_card							#banker draw 2nd card
        if i == 2: player2 = check_card							#player draw 1st card
        if i == 3: banker2 = check_card							#player draw 2nd card
      
      # print(player1 ,player2)								#check player face-up cards
      # print(banker1, banker2)								#check banker face-up cards
      
      #check player & banker hand total value
      player_hand = (player1 + player2) % 10				#Process player hands & -10 if the both cards add-up more than 10
      banker_hand = (banker1 + banker2) % 10				#Process banker hands & -10 if the both cards add-up more than 10
      player3 = ''
      banker3 = ''
      # print(Table_deck)									#check Decks after drew cards

# banker 9,8 = Done | 7
# Player 9,8 = Done
      if (player_hand < 8 and banker_hand < 8):			#if no natural win then check for 3rd card draw for player or banker
        #check player or banker need to draw 3rd card
          if player_hand <= 5:                           #player total 0,1,2,3,4 5, then player draw 3rd card
            check_card = Table_deck.pop(0)
            if check_card == "STOP":                          #check if the red card is draw
              Red_Card = True
              check_card = Table_deck.pop(0)
            player3 = check_card							                #player draw 3rd card
            player_hand = (player1 + player2 + player3) % 10	#Process player hands & -10 if the both cards add-up more than 10

            #check banker 3rd card draw condition
            if(banker_hand <= 2) or (banker_hand == 3 and player3 != 8) or (banker_hand == 4 and player3 >= 2 and player3 <= 7) or (banker_hand == 5 and player3 >= 4 and player3 <= 7) or (banker_hand == 6 and (player3 == 6 or player3 == 7)):
              check_card = Table_deck.pop(0)
              if check_card == "STOP":                        #check if the red card is draw
                Red_Card = True
                check_card = Table_deck.pop(0)
              banker3 = check_card							              #banker draw 3rd card
              banker_hand = (banker1 + banker2 + banker3) % 10#Process banker hands & -10 if the both cards add-up more than 10

          elif banker_hand <= 5 and (player_hand == 6 or player_hand == 7):
            check_card = Table_deck.pop(0)
            if check_card == "STOP":                        #check if the red card is draw
              Red_Card = True
              check_card = Table_deck.pop(0)
            banker3 = check_card							              #banker draw 3rd card
            banker_hand = (banker1 + banker2 + banker3) % 10#Process banker hands & -10 if the both cards add-up more than 10

      
      # print('Player_Hand:', player1, player2, player3,'=', player_hand)					#check player face-up cards ***********************
      # print('Banker_Hand:', banker1, banker2, banker3,'=', banker_hand)					#check banker face-up cards ***********************
      # print(Table_deck)									#check Decks after drew cards

      
      #check player or banker win or Tie
      if (player_hand > banker_hand):
        Win_results = "P"
        win_p+=1
        # print("P-WIN")
      elif (player_hand < banker_hand):
        Win_results = "B"
        win_b+=1
        # print("BB-WIN")
      else:
        # print("TIE")
        # Win_results = "T"           # Skip Tie
        Win_row -= 1
        pass

      #check if winning in row
      if Win_results_past == Win_results: 
        Win_row += 1
      elif Win_results_past == '':
        pass
      else:
        Game_results = Game_results + [Win_results_past+str(Win_row)]
        Win_row = 1
      if Red_Card == True:
        Game_results = Game_results + [Win_results_past+str(Win_row)]


      # print(Win_results_past ,Win_results)            # Check each winning row
      Win_results_past = Win_results
      # print(Game_Count, Game_results)
  return(Game_Count, Game_results, win_p, win_b)
# play_game()


# Step 3 Test check simulation results is correct of 49 vs 51
def test_1():
  skip  = 0                   # count skip condition meet
  Player= 0
  Banker= 0
  for i in range(1,10001):  #10k results about 4.5sec
    results = play_game()       # Take the results from random game
    results_p = results[2]        # take out the number of the game
    results_b = results[3]        # take out the number of the game

    Player +=results_p
    Banker +=results_b

  Total = Player + Banker
  Player_per = (Player / Total) * 100
  Banker_per = (Banker / Total) * 100
    
  print("Player:",Player , round(Player_per,2) ,"| Banker:", Banker, round(Banker_per,2),  " | Total:",Total)
# test_1()


# Step 4 remove P & T
def test_case():
  results = play_game()       # Take the results from random game
  results = results[1]        # take out the number of the game
  results_test1=results

  # Clean up the test results
  # while results_test1[0][0] == "P" or results_test1[0][0] == "T":  # pop 1st T or P
  # while results_test1[2][0] == "P" or results_test1[2][0] == "T":
  #   results_test1.pop(2)

  if results_test1[0][0] == "P":  # pop 1st T or P
    results_test1 = results_test1[1:]

  # print(results)
  # print(results_test1)
  return(results_test1)

# step Y create & store data
def create_data():
  # import json
  store_data = []
  # with open('data.json', 'w') as f:
  #   for i in range(100):
  #     json.dump(test_case(), f)
  with open('Output_data1.txt', 'w') as f:
    for i in range(3000):
      f.write(f"{test_case()}\n")
# create_data()


# Step x play many tables simulation
def test_2():
  skip  = 0                   # count skip condition meet
  win   = 0
  lose  = 0
  for i in range(1,10001):  #10k results about 4.5sec
    # print(i,test_case())
    # print("Test")
    # play_game()

    #test case for testing simulation (skip-4 1-B3 or 2-B3)
    test_1 = test_case()
    #test case after skip & bet
    if skip > 3:
      # print("start")
      if int(test_1[0][1]) > 2 or int(test_1[2][1]) > 2:
        lose += 1
      else:
        win += 1
      skip = 0
      # print("Win = ",win, " | Lose =", lose)


    if int(test_1[0][1]) > 2 or int(test_1[2][1]) > 2:
      skip+=1
      # print("Skip", skip)



    # print(i,  "=" ,test_1)
  print("Win = ",win, " | Lose =", lose)
# test_2()

# Step x play many tables simulation
def test_3():
  win   = 0
  lose  = 0
  for i in range(1,1001):  #10k results about 4.5sec
    test_1 = test_case()       # Take the results from random game
    # print(test_1)

    # Bet all & Check
    #Bet-1
    if int(test_1[0][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
      win+=2.85
    else:
      if int(test_1[0][1]) == 1:
        lose+=1
      if int(test_1[0][1]) == 2:
        lose+=1.05

      #Bet-2
      if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        win+=2.85
      else:
        if int(test_1[2][1]) == 1:
          lose+=1
        if int(test_1[2][1]) == 2:
          lose+=1.05

    # print(i,  "=" ,test_1)
    total = win - lose
  print("Lose-1:", round(lose,2) , " | Win-2:", round(win,2) , " || Total:", round(total,2))
# test_3()

# Step x play many tables simulation
def test_4():
  win   = 0
  lose  = 0
  win_1 = 0
  lose_1= 0
  skip  = 0   # wait for condition
  for i in range(1,1001):  #10k results about 4.5sec
    test_1 = test_case()       # Take the results from random game
    # print(test_1)

    if skip > 1:
      skip =0
      # Bet all & Check
      #Bet-1
      if int(test_1[0][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        win+=2.85
      else:
        if int(test_1[0][1]) == 1:
          lose+=1
        if int(test_1[0][1]) == 2:
          lose+=1.05

        #Bet-2
        if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
          win+=2.85
        else:
          if int(test_1[2][1]) == 1:
            lose+=1
          if int(test_1[2][1]) == 2:
            lose+=1.05
    if int(test_1[0][1]) < 3 and int(test_1[2][1]) < 3:
      skip+=1


    if int(test_1[0][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        win_1+=2.85
    else:
      if int(test_1[0][1]) == 1:
        lose_1+=1
      if int(test_1[0][1]) == 2:
        lose_1+=1.05

      #Bet-2
      if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win_1 in the row
        win_1+=2.85
      else:
        if int(test_1[2][1]) == 1:
          lose_1+=1
        if int(test_1[2][1]) == 2:
          lose_1+=1.05

    # print(i,  "=" ,test_1)
  total = win - lose
  total_1 = win_1 - lose_1
  total_2 = win_1 + lose_1
  total_per = (win_1 / total_2) * 100 #2.3 - 5.51
  print("Lose-1:", round(lose,2) , " | Win-2:", round(win,2) , " || Total:", round(total,2))
  print("Lose-1_1:", round(lose_1,2) , " | Win-2:", round(win_1,2) , " || Total:", round(total_1,2), " | ",round(total_per,2))
# test_4()

# Step x play many tables simulation
def test_5():
  W_win   = 0
  L_lose  = 0
  for i in range(1,1001):  #10k results about 4.5sec
    test_1 = test_case()       # Take the results from random game
    # print(test_1)

    # Bet all & Check
    #Bet-1
    if int(test_1[0][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
      L_lose+=3
    else:
      W_win+=1

      #Bet-2
      if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        L_lose+=3
      else:
        W_win+=1

    # print(i,  "=" ,test_1)
    # print("Win-1:", round(W_win,2) , " | Win-2:", round(L_lose,2) , " || Total:", round(total,2))
  total = W_win - L_lose
  total_1 = W_win + L_lose
  total_per = (W_win / total_1) * 100 #2.3 - 5.51
  print("Win-1:", round(W_win,2) , " | Lose-2:", round(L_lose,2) , " || Total:", round(total,2) , "|", round(total_per,2))
# test_5()

# Step x play many tables simulation
def test_6():
  P_P1 = 0
  P_P2 = 0
  P_P3 = 0
  P_P4 = 0
  P_P5 = 0
  P_P6 = 0
  skip    = 0   # wait for condition
  for i in range(1,10001):  #10k results about 4.5sec
    test_1 = test_case()       # Take the results from random game
    # print(test_1)

    if int(test_1[0][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      P_P1+=1
    else:
      P_P2+=1

    if int(test_1[2][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      P_P3+=1
    else:
      P_P4+=1

    if int(test_1[4][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      P_P5+=1
    else:
      P_P6+=1

      
    # print(i,  "=" ,test_1)
  print("BB1:", round(P_P1,2) , "BP1:", round(P_P2,2) ,"BB2:", round(P_P3,2) ,"BP2:", round(P_P4,2) ,"BB3:", round(P_P5,2) ,"BP3:", round(P_P6,2) ,)
# test_6()





# Step 5 play many tables simulation
def test_7():
  W_win   = 0
  L_lose  = 0
  W1_win   = 0
  L1_lose  = 0
  W2_win   = 0
  L2_lose  = 0
  W3_win   = 0
  L3_lose  = 0
  W4_win   = 0
  L4_lose  = 0
  W5_win   = 0
  L5_lose  = 0
  skip     = 0 
  skip1    = 0 
  skip2    = 0 
  skip3    = 0 
  skip4    = 0 
  skip5    = 0 
  skip_win = 0
  skip1_win= 0
  skip2_win= 0 
  skip3_win= 0
  skip4_win= 0
  skip5_win= 0
  for i in range(1,10001):  #10k results about 4.5sec
    test_1 = test_case()       # Take the results from random game
    # print(test_1)
# Bet all & Check
    #Bet-1
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L_lose+=1
    else:
      W_win+=1
      #Bet-2
      if int(test_1[2][1:]) > 2:
        L_lose+=3
      else:
        W_win+=1
        #Bet-3
        if int(test_1[4][1:]) > 2:
          L_lose+=3
        else:
          W_win+=1
    
    # if skip1 > 4:
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L1_lose+=1
      skip1=0
    else:
      W1_win+=1
      #Bet-2
      if int(test_1[2][1:]) > 1:
        L1_lose+=1
      else:
        W1_win+=1
        #Bet-3
        if int(test_1[4][1:]) > 1:
          L1_lose+=1
        else:
          W1_win+=1
    # if int(test_1[0][1:]) > 1:
    #   skip1+=1

    # if skip2 > 4:
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L2_lose+=1
    else:
      W2_win+=1
      skip2_win+=1
      #Bet-2
      if int(test_1[2][1:]) > 1:
        L2_lose+=1
        skip2=0
      else:
        W2_win+=1
        #Bet-3
        if int(test_1[4][1:]) > 2:
          L2_lose+=3
        else:
          W2_win+=1
      # if skip2_win > 0:
      #   skip2=0
    # if int(test_1[0][1:]) > 1:
    #   skip2+=1

    if skip3 > 4:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L3_lose+=1
      else:
        W3_win+=1
        #Bet-2
        if int(test_1[2][1:]) > 2:
          L3_lose+=3
          skip3=0
        else:
          W3_win+=1
          #Bet-3
          if int(test_1[4][1:]) > 2:
            L3_lose+=3
          else:
            W3_win+=1
        if skip3_win > 1:
          skip3=0
    if int(test_1[0][1:]) > 1:
      skip3+=1

    
    if skip4 > 4:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L4_lose+=1
      else:
        W4_win+=1
        skip4_win+=1
        #Bet-2
        if int(test_1[2][1:]) > 2:
          L4_lose+=3
          skip4=0
        else:
          W4_win+=1
          #Bet-3
          if int(test_1[4][1:]) > 2:
            L4_lose+=3
          else:
            W4_win+=1
        if skip4_win > 2:
          skip4=0
    if int(test_1[0][1:]) > 1:
      skip4+=1


    if skip5 > 4:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L5_lose+=1
      else:
        W5_win+=1
        skip5_win+=1
        #Bet-2
        if int(test_1[2][1:]) > 2:
          L5_lose+=3
          skip5=0
        else:
          W5_win+=1
          #Bet-3
          if int(test_1[4][1:]) > 2:
            L5_lose+=3
          else:
            W5_win+=1
        if skip5_win > 3:
          skip5=0
    if int(test_1[0][1:]) > 1:
      skip5+=1







    # # Bet all & Check
    # #Bet-1
    # if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
    #   L1_lose+=1
    # else:
    #   W1_win+=1

    #   #Bet-2
    #   if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #     L1_lose+=3
    #   else:
    #     W1_win+=1

    #     #Bet-3
    #     if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #       L1_lose+=3
    #     else:
    #       W1_win+=1


    # #Bet-1
    # if skip > 2:
    #   #Bet-1
    #   if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
    #     L2_lose+=1
    #     skip=0
    #   else:
    #     W2_win+=1
    #     skip_win+=1

    #     #Bet-2
    #     if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #       L2_lose+=3
    #       skip=0
    #     else:
    #       W2_win+=1
    #       skip_win+=1

    #       #Bet-3
    #       if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #         L2_lose+=3
    #         skip=0
    #       else:
    #         W2_win+=1
    #         skip_win+=1

    # if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
    #   skip+=1
    # if skip_win > 7:
    #   skip_win=0
    #   skip=0


    # #Bet-1
    # if skip1 > 2:
    #   #Bet-1
    #   if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
    #     L3_lose+=1
    #     skip1=0
    #   else:
    #     W3_win+=1
    #     skip1_win+=1

    #     #Bet-2
    #     if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #       L3_lose+=3
    #       skip1=0
    #     else:
    #       W3_win+=1
    #       skip1_win+=1

    #       #Bet-3
    #       if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
    #         L3_lose+=3
    #         skip1=0
    #       else:
    #         W3_win+=1
    #         skip1_win+=1

    # if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
    #   skip1+=1
    # if skip1_win > 6:
    #   skip1_win=0
    #   skip1=0



    # print(i,  "=" ,test_1)
    # print("Win-1:", round(W_win,2) , " | Win-2:", round(L_lose,2) , " || Total:", round(total,2))
  total5 = W5_win - L5_lose
  total_5 = W5_win + L5_lose
  if total_5 == 0 : total_per5 = 0 
  else : total_per5 = (W5_win / total_5) * 100 - 50 #2.3 - 5.51
  total4 = W4_win - L4_lose
  total_4 = W4_win + L4_lose
  if total_4 == 0 : total_per4 = 0
  else:  total_per4 = (W4_win / total_4) * 100 - 50 #2.3 - 5.51
  total3 = W3_win - L3_lose
  total_3 = W3_win + L3_lose
  if total_3 == 0 : total_per3 = 0
  else:total_per3 = (W3_win / total_3) * 100 - 50 #2.3 - 5.51
  total2 = W2_win - L2_lose
  total_2 = W2_win + L2_lose
  if total_2 == 0 : total_per2 = 0
  else:total_per2 =  (W2_win / total_2) * 100 - 50 #2.3 - 5.51
  total1 = W1_win - L1_lose
  total_1 = W1_win + L1_lose
  if total_1 == 0 : total_per1 = 0
  else: total_per1 = (W1_win / total_1) * 100 - 50 #2.3 - 5.51
  total = W_win - L_lose
  total_0 = W_win + L_lose
  if total_0 == 0 : total_per = 0
  else: total_per = (W_win / total_0) * 100 - 50 #2.3 - 5.51
  print("0 Win:", round(W_win,2) , " | Lose:", round(L_lose,2) , " || Total:", round(total_0,2) , "| EV", round(total_per,2) , " || Profit/loss:", round(total,2) ,)
  print("1 Win:", round(W1_win,2) , " | Lose:", round(L1_lose,2) , " || Total:", round(total_1,2) , "| EV", round(total_per1,2), " || Profit/loss:", round(total1,2) ,)
  print("2 Win:", round(W2_win,2) , " | Lose:", round(L2_lose,2) , " || Total:", round(total_2,2) , "| EV", round(total_per2,2), " || Profit/loss:", round(total2,2) ,)
  print("3 Win:", round(W3_win,2) , " | Lose:", round(L3_lose,2) , " || Total:", round(total_3,2) , "| EV", round(total_per3,2), " || Profit/loss:", round(total3,2) ,)
  print("4 Win:", round(W4_win,2) , " | Lose:", round(L4_lose,2) , " || Total:", round(total_4,2) , "| EV", round(total_per4,2), " || Profit/loss:", round(total4,2) ,)
  print("5 Win:", round(W5_win,2) , " | Lose:", round(L5_lose,2) , " || Total:", round(total_5,2) , "| EV", round(total_per5,2), " || Profit/loss:", round(total5,2) ,)
# 1-2 Win-3: 3005  | Lose-3: 2451  || Total: 554 | 55.08
# 1-1 Win-2: 3008  | Lose-2: 2478  || Total: 530 | 54.83
# 1-0 Win-1: 113706  | Lose-2: 115821  || Total: -2115 | 49.54
# test_7()


# 0 Win: 1134018  | Lose: 1167739  || Total: 2301757 | EV -0.73  || Profit/loss: -33721
# 1 Win: 225643  | Lose: 233225  || Total: 458868 | EV -0.83  || Profit/loss: -7582
# 2 Win: 193411  | Lose: 198260  || Total: 391671 | EV -0.62  || Profit/loss: -4849
# 3 Win: 507250  | Lose: 519347  || Total: 1026597 | EV -0.59  || Profit/loss: -12097
# 4 Win: 193412  | Lose: 198263  || Total: 391675 | EV -0.62  || Profit/loss: -4851
# 5 Win: 193412  | Lose: 198271  || Total: 391683 | EV -0.62  || Profit/loss: -4859
