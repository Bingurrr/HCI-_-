"""
  https://www.acmicpc.net/problem/1058
  2-친구 : 실제 친구 + 한다리 건너서 친구
  (ex A와 B가 친구이고 B와 C가 친구이면 A와C는 2-친구이다)
  2-친구가 가장 많은 사람이 가장 유명한 사람이다
  
  입력 :
    첫째 줄 : 사람수
    둘쨰 줄 ~ : N개의 줄에 각 사람이 친구이면 Y, 아니면 N
    
  출력 :
    가장 유명한 사람의 2-친구수
    
  내 풀이 : 
    예를 들어 A가 B,D,E 와 친구라고 했을 떄
    A의 2-친구수는 len({AUB + AUD + AUE})
"""
# 입력
N = int(input()) 
arr = []
answer = 0
# 집합 생성 후 친구일 경우 친구 번호를 집합에 담아둠
for i in range(N) :
  a = input()  
  friend = set()
  for j in range(len(a)) :
    if a[j] == 'Y' :
      friend.add(j)
  arr.append(friend)
#print(arr)
for x in arr :
  friends = x
  for y in x :
    #print(y)
    friends = friends | arr[y]
    #print(friends)
  if len(friends) > answer :
    answer = len(friends)

# 자기 자신은 친구가 아니니 -1해줌
if answer > 0 :
  answer -= 1

print(answer)

