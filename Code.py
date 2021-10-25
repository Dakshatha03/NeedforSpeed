n,totalTime = map(int,input().split())
speedToDistance = {}
for i in range(n):
    distance, speed = map(int,input().split())
    if speed not in speedToDistance:
        speedToDistance[speed] = 0
    speedToDistance[speed] += distance
print(speedToDistance)

def solve(c):
    computedTime = 0
    for speed in speedToDistance:
      distance = speedToDistance[speed]
      possibleSpeed = (speed + c)
      if possibleSpeed < distance / totalTime:
        computedTime = totalTime + 1
        break
      computedTime += distance / possibleSpeed
    return computedTime


lower = -1000000000
upper = 1000000000
c = 0
while True:
    flag = solve(c)
    if flag > totalTime:
      lower = c
    else:
      upper = c
    newc = (lower + upper) / 2
    if abs(newc - c) < 0.00000001:
      break
    c = newc
print(c)
