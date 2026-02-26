list=[1,-2,3,-4,78.97] #Printing list elements
print(list)    #output=[1,-2,3,-4,78.97]

tuple=tuple(list) #converting list to tuple
print(type(tuple)) #<class 'tuple'>

positive_count=0
negative_count=0
positive_numbers=[]
for i in tuple:
    if i>0:
      positive_count+=1
      positive_numbers.append(i)
    elif i<0:
       negative_count+=1

print("Tuple",tuple)  #ouput=Tuple=(1,-2,3,-4,78.97)
print("Positive Count",positive_count) #printing positive count  #output=3
print("Negative count",negative_count)  #printing Negative count #output=2
print("List",positive_numbers)   #printing positive numbers  #output=list[1,3,78.97]

print("2"+"3"*2)  #concatinating the string and after taht + operator it will print 3 two times #233


