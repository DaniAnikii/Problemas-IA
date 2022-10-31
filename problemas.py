def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  a = 0.0
  b = 0.0
  for i in G:
    for u in i:
      if u == 0:
          a += 1
      if u == 1:
          b += 1
  return b/(a+b)

#O(n)


def getSum(A: int, B: int, C: int) -> int:
  # Write your code here
  return A+B+C

#O(n)

def getWrongAnswers(N: int, C: str) -> str:
  strings = []
  for i in (C):
      strings.append(i)
  for i in range(N):
     if strings[i] == "A":
          strings[i] = "B"
     elif strings[i] == "B":
           strings[i] = "A"
  res = ""
  for i in strings:
      res = res + i
  return res

#O(n)
