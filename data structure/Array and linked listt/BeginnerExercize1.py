def recur(num,i,max):
   if i==len(num):
      return max
   if num[i]>max:
    max=num[i]
   return recur(num,i+1,max)

def string(count):
   str=input("enter name :")
   for i in str:
     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
       count=count+1
   return count
     

num=[5,8,9,6,7]
maximum=recur(num,0,num[0])
print("maximum number is :",maximum)
vowel=string(0)
print("total vowel in string is :",vowel)


