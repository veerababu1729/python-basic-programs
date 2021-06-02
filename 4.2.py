str1,str2=input("enter two strings:").split()
if(len(str1)!=len(str2)):
   print("entered strings are not equal")
   exit()
else:
  for i in range(0,len(str1)):
      print(str1[i]+str2[i],end='')
      
  
