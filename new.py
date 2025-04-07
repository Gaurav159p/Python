# print('''Lines 
# in 
#     different
# lines''')

# Sum of Consecutive sqaures
n = int(input())
answer = 0
for i in range(n+1):
    answer = answer + i*i
print(answer)

# Avg calc
n = int(input())
answer = 0
for i in range(n):
    m = int(input())
    answer = answer + m
answer = answer/n
print(answer)