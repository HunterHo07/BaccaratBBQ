
# results from : https://wizardofodds.com/games/baccarat/basics/#simulations
# // read results from txt bac1 - bac10
# with open("real_results/bac1.txt") as file:
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]

with open('real_results/bac1.txt') as f:
    lines = f.read().splitlines()
# print(lines[0])


results_holder = []
#get the 25,000 results & clean it
for i in range(25000):
    results_holder = results_holder + [lines[i] + str("S")]

# remove all Tie from the results
# replacers = {',':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':'','T':''}
results_holder = [s.replace('T', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace(',', '') for s in results_holder] #
# results_holder = [s.replace(replacers) for s in results_holder] # 
# results_holder = [s.replace('1', '') for s in results_holder] #
# results_holder = [s.replace('2', '') for s in results_holder] #
# results_holder = [s.replace('3', '') for s in results_holder] #
# results_holder = [s.replace('4', '') for s in results_holder] #
# results_holder = [s.replace('5', '') for s in results_holder] #
# results_holder = [s.replace('6', '') for s in results_holder] #
# results_holder = [s.replace('7', '') for s in results_holder] #
# results_holder = [s.replace('8', '') for s in results_holder] #
# results_holder = [s.replace('9', '') for s in results_holder] #
# remove all , from the results
# results_holder = [s.replace(',', '') for s in results_holder] # 

# print(results_holder)

check_results = []
all_check_results = []
# print(check_results)
now           = 'NO'
past          = ''
win_count     = 1
game_count    = 1
for i in results_holder:
    for u in i:
        now = u
        # print(u)
        if now == past:
            win_count+=1
        elif past == '':
            pass
        else:
            check_results = check_results + [past+str(win_count)]
            win_count=1
        past = now
        if past == "S":
          past = ''
    # remove all start with Players or player win row - wait till Banker open 1
    if check_results[0][0] == "P":
        # print(check_results, "Before")
        check_results = check_results[1:]
        # print(check_results, "After")
    all_check_results.append(check_results)
    check_results=[]
    # print(i)

#clean up all results
# print(all_check_results)









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
  for test_1 in all_check_results:  #10k results about 4.5sec
    # test_1 = test_case()       # Take the results from random game
    # print(test_1)

    # Bet all & Check
    #Bet-1
    if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L_lose+=1
    else:
      W_win+=1

    if int(test_1[2][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L1_lose+=1
    else:
      W1_win+=1
      

    if skip2 > 4:
      if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L2_lose+=1
        skip2_win-=1
        # skip2=0
      else:
        W2_win+=1
        skip2_win+=1
        if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
          L2_lose+=3
          skip2_win-=3
          skip2=0
        else:
          W2_win+=1
          skip2_win+=1
          if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
            L2_lose+=3
            skip2_win-=3
          else:
            W2_win+=1
            skip2_win+=1


    if int(test_1[0][1:]) > 1 or int(test_1[2][1:]) > 2:
      skip2+=1

    if int(test_1[2][1:]) > 3:  #if 1st or 2nd B- is more than 3 win in the row
      L3_lose+=7
    else:
      W3_win+=1

    if int(test_1[2][1:]) > 4:  #if 1st or 2nd B- is more than 3 win in the row
      L4_lose+=15
    else:
      W4_win+=1

    if int(test_1[2][1:]) > 5:  #if 1st or 2nd B- is more than 3 win in the row
      L5_lose+=31
    else:
      W5_win+=1

      # #Bet-2
      # if int(test_1[2][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      #   L_lose+=1
      # else:
      #   W_win+=1

        # #Bet-3
        # if int(test_1[4][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        #   L_lose+=1
        # else:
        #   W_win+=1
    # print(test_1)


# ==================================================================== test 1

    #Bet-1
#     if skip1 > 2:
#       #Bet-1
#       if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
#         L1_lose+=1
#         skip1=0
#       else:
#         W1_win+=1
#         skip1_win+=1

#         #Bet-2
#         if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#           L1_lose+=3
#           skip1=0
#         else:
#           W1_win+=1
#           skip1_win+=1

#           #Bet-3
#           if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#             L1_lose+=3
#             skip1=0
#           else:
#             W1_win+=1
#             skip1_win+=1

#     if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
#       skip1+=1
#     if skip1_win > 8:
#       skip1_win=0
#       skip1=0





# # ==================================================================== test 2

#     #Bet-1
#     if skip2 > 2:
#       #Bet-1
#       if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
#         L2_lose+=1
#         skip2=0
#       else:
#         W2_win+=1
#         skip2_win+=1

#         #Bet-2
#         if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#           L2_lose+=3
#           skip2=0
#         else:
#           W2_win+=1
#           skip2_win+=1

#           #Bet-3
#           if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#             L2_lose+=3
#             skip2=0
#           else:
#             W2_win+=1
#             skip2_win+=1

#     if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
#       skip2+=1
#     if skip2_win > 7:
#       skip2_win=0
#       skip2=0



# # ==================================================================== test 3



#     #Bet-1
#     if skip3 > 2:
#       #Bet-1
#       if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
#         L3_lose+=1
#         skip3=0
#       else:
#         W3_win+=1
#         skip3_win+=1

#         #Bet-2
#         if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#           L3_lose+=3
#           skip3=0
#         else:
#           W3_win+=1
#           skip3_win+=1

#           #Bet-3
#           if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#             L3_lose+=3
#             skip3=0
#           else:
#             W3_win+=1
#             skip3_win+=1

#     if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
#       skip3+=1
#     if skip3_win > 6:
#       skip3_win=0
#       skip3=0



# # ==================================================================== test 4



#     #Bet-1
#     if skip4 > 2:
#       #Bet-1
#       if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
#         L4_lose+=1
#         skip4=0
#       else:
#         W4_win+=1
#         skip4_win+=1

#         #Bet-2
#         if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#           L4_lose+=3
#           skip4=0
#         else:
#           W4_win+=1
#           skip4_win+=1

#           #Bet-3
#           if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#             L4_lose+=3
#             skip4=0
#           else:
#             W4_win+=1
#             skip4_win+=1

#     if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
#       skip4+=1
#     if skip4_win > 5:
#       skip4_win=0
#       skip4=0



# # ==================================================================== test 5



#     #Bet-1
#     if skip5 > 2:
#       #Bet-1
#       if int(test_1[0][1:]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
#         L5_lose+=1
#         skip5=0
#       else:
#         W5_win+=1
#         skip5_win+=1

#         #Bet-2
#         if int(test_1[2][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#           L5_lose+=3
#           skip5=0
#         else:
#           W5_win+=1
#           skip5_win+=1

#           #Bet-3
#           if int(test_1[4][1:]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
#             L5_lose+=3
#             skip5=0
#           else:
#             W5_win+=1
#             skip5_win+=1

#     if int(test_1[0][1:]) > 2 and int(test_1[2][1:]) > 2:
#       skip5+=1
#     if skip5_win > 4:
#       skip5_win=0
#       skip5=0


# ==================================================================== test 4













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

# 1-0 Win-1: 21651  | Lose-1: 28161  || Total-1: -6510 | 43.47
# 1-1 Win-2: 763  | Lose-2: 884  || Total-2: -121 | 46.33
# 1-2 Win-3: 761  | Lose-3: 874  || Total-3: -113 | 46.54
test_7()
    

