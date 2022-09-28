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
    



print(data_holder[45322])
