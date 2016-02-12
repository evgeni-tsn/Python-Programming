def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

print(fib(50))
sum=0
for i in range(50):
    if fib(i)>=4000000:
        break
    elif fib(i)%2==0:
        sum+=fib(i)
print(sum)