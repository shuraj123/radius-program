n = int(input("enter  how many no of terms :"))
n1,n2 = 0,1
count  = 0
if n <= 0 :
    print("please enter a  positive number:")
elif  n==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonacci numbers of sequence  are :")
    while count < n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count += 1
