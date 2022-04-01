"""
  문제 링크 : https://www.acmicpc.net/problem/16928
  주사위 이동할 수 있는거리 1~6
  을 이용하여 bfs를 만듦
  사다리와 뱀이 있는 곳에는 이동할 수 있는곳을 변경해줌
  직관적이게 풀었다 주사위로 이동할 수 있는거리인 1~6까지 이동하게 했고
  뱀과 사다리가 나오면 그 거리로 다시 이동하게 했다
  여기서 이미 방문한 곳은 다시계산하지 않았고
  목적지까지 걸린 횟수를 최소가 되도록 갱신해주었다.  
"""

from collections import deque
N, M = map(int, input().split())
a = [] # 사다리
b = [] # 뱀
arr = [i for i in range(101)]
visited = [0 for _ in range(101)]
visited[100] = 999999999 # 도착지점 작은값이 오면 계속 갱신
for _ in range(N) : 
  x, y = map(int, input().split())
  a.append((x,y))
  arr[x] = y
for _ in range(M) : 
  x, y = map(int, input().split())
  b.append((x,y))
  arr[x] = y

move = (1,2,3,4,5,6)

def bfs() :
  dq = deque()
  pos = 1
  arr[1] = 1
  dq.append(arr[1])
  while dq :
    pos = dq.popleft()
    for i in range(6) :
      new_pos = pos + move[i]
      if new_pos >= 100 :
        if visited[100] > visited[pos] + 1 :
          visited[100] = visited[pos] + 1
      elif visited[new_pos] != 0 :
        continue
      elif visited[new_pos] == 0 and arr[new_pos] == 0:
        visited[new_pos] = visited[pos] + 1
        dq.append(new_pos)
      elif arr[new_pos] != 0 :
        new_pos = arr[new_pos]
        if visited[new_pos] == 0 :
          visited[new_pos] = visited[pos] + 1
          dq.append(new_pos)
bfs()
print(visited[100])
