temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]
temp_total =0
count = 0
for temp in temperatures:
   temp_total +=temp
   count +=1
avg_temp = temp_total/count

print (avg_temp)