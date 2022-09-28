import math


data_holder = []
with open('Output_data.txt', 'r') as f:
	lines = f.readlines()
# print(lines[0])

for i in range(270000):
	data_in	= lines[i].replace("[","").replace("'","").replace("]","").replace("\n","").replace(" ","")
	data_holder.append(data_in.split(","))
	# data_holder.append(lines[i])
	# print(lines[i])
    



# print(data_holder[45322])




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
  for test_1 in data_holder:  #10k results about 4.5sec
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
test_7()