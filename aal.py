"""#armstrong

nmbr=int(input("Enter your number :"))
temp=nmbr
rem=0
sum=0
while temp>0:
    rem=temp%10
    sum+=rem**3
    temp//=10
if(nmbr==sum):
    print("yes")
else:
    print("No")"""

"""#remove duplicate char

word=input("Enter your word :")
for i in range(len(word)):
    count=1
    for j in range(i+1,len(word)):
        if(word[i]==word[j]):
            count+=1
    if(count<=1):
        print(word[i])"""

"""# string reverse
word="sriharan"
temp=""
for char in word:
    temp=char+temp
print(temp)"""

"""# largest in array

arr=[25,47,69,23,54]
temp=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
print(temp)"""

"""# adding all elements

arr=[25,47,69,23,54]
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)"""

"""
# digits sum

nmbr=1234
temp=nmbr
sum=0

while temp>0:
    rem=temp%10
    sum=sum+rem
    temp//=10
print(sum)"""


#number palindrome
"""
nmbr="1231"
temp=""
for char in nmbr:
    temp=char+temp
if(temp==nmbr):
    print("yes")
else:
    print("NO")"""

"""nmbr= 1221
sum=0
rem=0
temp=nmbr
while(temp>0):
    rem=temp%10
    sum=(sum*10)+rem
    temp//=10
if(sum==nmbr):
    print("yes")
else:
    print("NO")
"""

"""#factorial

nmbr=5
fact=1
for i in range(1,nmbr+1):
    fact*=i
print(fact)"""


# remove duplicate nmbr

"""nmbr=[25,47,69,25,36,47]
temp=[]
for i in range(len(nmbr)):
    if nmbr[i] not in temp:
        temp.append(nmbr[i])

print(temp)
"""


# mid element in arr

"""arr=[21,25,69,74,65,10]
arr.sort()
temp=len(arr)//2
print(arr[temp-1])
"""

#add all digits
"""nmbr=12345
rem,sum=0,0
while nmbr>0:
    rem=nmbr%10
    sum+=rem
    nmbr//=10
print(sum)
"""
# reverse a digit
"""nmbr=12345
sum,rem=0,0
while nmbr>0:
    rem=nmbr%10
    sum=(sum*10)+rem
    nmbr//=10
print(sum)"""

#remove duplicate digits

"""nmbr=1234565
temp=[]
for digit in str(nmbr):
   if int(digit) not in temp:
       temp.append(int(digit))
print(temp)"""

#remove duplicate nmbr

"""nmbr=1235432
temp1=[]
for digit in str(nmbr):
    if int(digit) not in temp1:
        temp1.append(int(digit))
print(temp1)
"""

#number reverse
"""nmbr=123456
rem,sum=0,0
while nmbr>0:
    rem=nmbr%10
    sum=(sum*10)+rem
    nmbr//=10
print(sum)"""

#add all digits

"""nmbr=1234
rem,sum=0,0

while nmbr>0:
    rem=nmbr%10
    sum+=rem
    nmbr//=10
print(sum)"""


#reverse all digits
"""nmbr=1234543
temp=[]
for digit in str(nmbr):
    if int(digit) not in temp:
        temp.append(int(digit))
print(temp)"""


#duplicate char

"""word=input("Enter your word: ")
temp=""
for char in word:
    if char not in temp:
        temp+=char
print(temp)"""

#factorial

"""nmbr=int(input("Enter your nmbr: "))
sum=1
for i in range(1,nmbr+1):
    sum*=i
print(sum)"""

