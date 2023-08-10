from collections import Counter
t = int(input())

test_cases = []

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    assert len(arr) == n
    test_cases.append(arr)
    
    
def find_intruder(a):
    count = Counter(a)
    
    intruder = min(count, key=count.get)
    
    return a.index(intruder) + 1


for arr in test_cases:
    print(find_intruder(arr))

              