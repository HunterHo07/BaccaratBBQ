import math


data_holder = []
with open('C:\\Users\\user\\Desktop\\Desktop\\projects\\Output_dataP.txt', 'r') as f:
# with open('C:\\Users\\user\\Desktop\\Desktop\\projects\\Bac_all_clean.txt', 'r') as f:
	lines = f.readlines()
# print(lines[0])

for i in range(1000000):
# for i in range(249999):
	# data_in	= lines[i].replace("\n","")
	data_in	= lines[i]
	data_holder.append(data_in.split(","))
	# data_holder.append(lines[i])
	# print(lines[i])
# print(data_holder[45322])

def count_total(W_win,L_lose):
  total_0 = W_win + L_lose
  total = W_win - L_lose
  total_per = 0
  if total_0 > 0 : total_per = (W_win / total_0) * 100 - 50 #2.3 - 5.51
  return(W_win,L_lose,total_0,total_per,total)


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
  skip1_win= 0
  skip2_win= 0 
  skip3_win= 0
  skip4_win= 0
  skip5_win= 0
  for test_1 in data_holder:  #10k results about 4.5sec
    # print(test_1)
	
    # Bet-1
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      W_win+=1
    else:
      L_lose+=1
      if int(test_1[2][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        W_win+=1
      else:
        L_lose+=1
        # if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        #   W_win+=3
        # else:
        #   L_lose+=1
        #0 Win: 931137  | Lose: 957992  || Total: 1889129 | EV -0.71  || Profit/loss: -26855


    if skip1 > 2:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        W1_win+=1
        # skip1=0
      else:
        L1_lose+=1
        # skip1_win+=1
        # skip1=0
        #Bet-2
        if int(test_1[2][1:]) > 1:
          W1_win+=1
          skip1=0
        else:
          L1_lose+=1
          # skip1_win+=1
          # skip1=0
          #Bet-3
          # if int(test_1[4][1:]) > 1:
          #   W1_win+=1
          #   # skip1=0
          # else:
          #   L1_lose+=1
          #   # skip1_win+=1
    if skip1_win > 1:
      skip1=0
      # skip1_win=0
    if int(test_1[0][1:]) == 1 and int(test_1[2][1:]) == 1:
      skip1+=1


    # if skip2 > 5:
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L2_lose+=1
      # skip2=0
    else:
      W2_win+=0.95
      # skip2_win+=1
      #Bet-2
      if int(test_1[2][1:]) > 1:
        L2_lose+=1
        # skip2=0
      else:
        W2_win+=0.95
        # skip2_win+=1
        # Bet-3
        # if int(test_1[4][1:]) > 2:
        #   L2_lose+=3
        #   # skip2=0
        # else:
        #   W2_win+=0.95
          # skip2_win+=1
          # skip2=0
    # if skip2_win > 9:
    #   skip2=0
    #   skip2_win=0
    # # if int(test_1[0][1:]) > 3 or int(test_1[2][1:]) > 5:
    # if int(test_1[0][1:]) > 1 or int(test_1[2][1:]) > 1 or int(test_1[4][1:]) > 1:
    #   skip2+=1


    if skip3 > 5:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L3_lose+=1
        skip3=0
      else:
        W3_win+=0.95
        # skip3=0
        skip3_win+=0.95
        #Bet-2
        if int(test_1[2][1:]) > 1:
          L3_lose+=1
          # skip3=0
        else:
          W3_win+=0.95
          skip3=0
          skip3_win+=0.95
          #Bet-3
          # if int(test_1[4][1:]) > 1:
          #   W3_win+=1
          #   # skip3=0
          # else:
          #   L3_lose+=1
          #   # skip3_win+=0.95
    if skip3_win > 2:
      skip3=0
      skip3_win=0
    if int(test_1[0][1:]) > 1 or int(test_1[2][1:]) > 1:
      skip3+=1
    # 3 Win: 105016  | Lose: 106619  || Total: 211634.85 | EV -0.38  || Profit/loss: -1603.15

    
    # if skip4 > 5:
    #   if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
    #     L4_lose+=1
    #     skip4=0
    #   else:
    #     W4_win+=1
    #     skip4_win+=1
    #     #Bet-2
    #     if int(test_1[2][1:]) > 1:
    #       L4_lose+=1
    #       skip4=0
    #     else:
    #       W4_win+=1
    #       skip4_win+=1
    #       #Bet-3
    #       if int(test_1[4][1:]) > 2:
    #         L4_lose+=3
    #         skip4=0
    #       else:
    #         W4_win+=1
    #         skip4_win+=1
    #         # skip4=0
    # if skip4_win > 9:
    #   skip4=0
    #   skip4_win=0
    # # if int(test_1[0][1:]) > 3 or int(test_1[2][1:]) > 5:
    # if int(test_1[2][1:]) > 2:
    #   skip4+=1


    # if skip5 > 5:
    #   if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
    #     L5_lose+=1
    #     skip5=0
    #   else:
    #     W5_win+=1
    #     skip5_win+=1
    #     #Bet-2
    #     if int(test_1[2][1:]) > 1:
    #       L5_lose+=1
    #       # skip5=0
    #     else:
    #       skip5=0
    #       W5_win+=1
    #       skip5_win+=1
    #       #Bet-3
    #       if int(test_1[4][1:]) > 2:
    #         L5_lose+=3
    #         # skip5=0
    #       else:
    #         W5_win+=1
    #         skip5_win+=1
    # if skip5_win > 9:
    #   skip5=0
    #   skip5_win=0
    # # if int(test_1[0][1:]) > 3 or int(test_1[2][1:]) > 5:
    # if int(test_1[0][1:]) > 2 or int(test_1[2][1:]) > 2:
    #   skip5+=1


  #   # print(i,  "=" ,test_1)
  #   # print("Win-1:", round(W_win,2) , " | Win-2:", round(L_lose,2) , " || Total:", round(total,2))
  total_0 = count_total(W_win,L_lose)
  total_1 = count_total(W1_win,L1_lose)
  total_2 = count_total(W2_win,L2_lose)
  total_3 = count_total(W3_win,L3_lose)
  total_4 = count_total(W4_win,L4_lose)
  total_5 = count_total(W5_win,L5_lose)
  # print(skip2_win)
  print("0 Win:", round(total_0[0],None) , " | Lose:", round(total_0[1],None) , " || Total:", round(total_0[2],2) , "| EV", round(total_0[3],2) , " || Profit/loss:", round(total_0[4],2) ,)
  print("1 Win:", round(total_1[0],None) , " | Lose:", round(total_1[1],None) , " || Total:", round(total_1[2],2) , "| EV", round(total_1[3],2) , " || Profit/loss:", round(total_1[4],2) ,)
  print("2 Win:", round(total_2[0],None) , " | Lose:", round(total_2[1],None) , " || Total:", round(total_2[2],2) , "| EV", round(total_2[3],2) , " || Profit/loss:", round(total_2[4],2) ,)
  print("3 Win:", round(total_3[0],None) , " | Lose:", round(total_3[1],None) , " || Total:", round(total_3[2],2) , "| EV", round(total_3[3],2) , " || Profit/loss:", round(total_3[4],2) ,)
  print("4 Win:", round(total_4[0],None) , " | Lose:", round(total_4[1],None) , " || Total:", round(total_4[2],2) , "| EV", round(total_4[3],2) , " || Profit/loss:", round(total_4[4],2) ,)
  print("5 Win:", round(total_5[0],None) , " | Lose:", round(total_5[1],None) , " || Total:", round(total_5[2],2) , "| EV", round(total_5[3],2) , " || Profit/loss:", round(total_5[4],2) ,)

test_7()



















# 0 Win: 133430  | Lose: 136570  || Total: 270000 | EV -0.58  || Profit/loss: -3140