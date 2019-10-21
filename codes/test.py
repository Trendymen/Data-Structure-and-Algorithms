# 第一种算法
sum,n = 0,100

for i in range(n+1):

    sum = sum + i
print(sum)


# 第二种算法
sum , n  =  0,100
sum  = (1+n)*n/2
print(sum)
# 第一种算法执行了1+(n+1)+n=2n+2次。
# 第二种算法，是1+1=2次

# 平方阶
i = 0
n = 100
for  i in range(n+1):
    for j in range(n+1 - i):
        print("I love FishC.com\n")
# 对数阶
i = 1
n = 100
while i < n:
    i = i * 2
    print(i)


def function(count):
    print("{}".format(count))
n = 100
for i in range(n+0):
    function(i)

def function2(count):
    for j in range(n-i):
        print(j)
for i in range(n+0):
    function2(i)


