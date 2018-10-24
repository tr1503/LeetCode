def missWord(self, s, t):
  missing = []
  a = s.split(' ')
  b = t.split(' ')
  i = 0
  j = 0
  while i < len(a):
    if a[i] == b[j]:
      missing.append(a[i])
     else:
      j += 1
    i += 1
  return missing
