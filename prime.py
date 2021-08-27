n=input('Enter the number you want to check: ')
try:
    n=int(n)
except:
    print('Wrong input.')
    quit()
if n==1 or n==0:
    print('This is neither prime nor composite')
else:
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        print("This is a prime number")
    else:
        print('This  is a composite number.')

def getResult(n):
   
    st = str(n)
     
    for i in st:
       
        if(n % int(i) == 0):
            return 'Yes'
           
    return 'No'
 
 
n = 9876543
 
print(getResult(n))