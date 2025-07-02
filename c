m = 1000
while m < 1500:
  print(m)
  m += 100

  s = 2000
while s < 5000:
  print(s)
  if s == 100:
    break
  s += 100

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

