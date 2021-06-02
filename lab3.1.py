#printing right angle triangle pattern
rows=int(input('enter how many rows i.e., height of the right angled triangle:'))
for i in range(rows):
 for j in range(i+1):
  print('*',end=' ')
 print('\r')
