length = 0
cnt = 1
arr = []

for i in range(5):
  word = input()
  arr.append(word)
  length = max(len(word), length)

for i in range(length):
  for j in range(5):
    if i <= len(arr[j]) - 1:
      print(arr[j][i], end = "")
    else:
      continue