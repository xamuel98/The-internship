n = str(input("Enter your card number to validate, e.g. 5399834521636555: "))
i = len(n) - 2
temp1 = ""
temp2 = ""
m = []
while i >= 0:
  temp1 = temp1 + n[i]
  v = n[i]
  d = int(v) * 2

  a = str(d)

  g = 0

  if len(a) == 2:
    b = int(a)

    sum = 0

    c = b % 10

    sum += c

    e = b // 10

    sum += e
    d = sum
    # print(v, d)

  # else:

  # print(v, d)
  m.append(d)
  # print(m)
  j = 0
  s = 0
  while j < len(m):
    s += m[j]
    j += 1
  i -= 2
# print(s)
z = []
h = len(n) - 1
while h >= 0:
  temp2 = temp2 + n[h]
  w = n[h]
  z.append(w)
  # print(z)
  p = 0
  q = 0
  while p < len(z):
    q += int(z[p])
    p += 1
  h -= 2
# print(q)
sq = s + q
if sq % 10 == 0:
  print("Credit Card Number is Valid")
else:
  print("Invalid Credit Card Number")
