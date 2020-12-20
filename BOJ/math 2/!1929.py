#시간초과
#반복문 돌릴 때 이미 제거한 수 빼고 돌리는 방법 찾아야 함
#[True] 리스트를 만들어서 체크

import math
M, N = map(int, input().split())

prime_list = []
for i in range(M, N+1) :
  prime_list.append(i)

remove_list = []
for i in range(2, int(math.sqrt(N))+1) :
  if i not in remove_list :
    for num in prime_list :
      if num % i == 0 and num != i :
        prime_list.remove(num)
        remove_list.append(num)

for prime_num in prime_list :
  print(prime_num)