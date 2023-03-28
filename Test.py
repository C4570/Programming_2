def recursion_3(num, cont = 1):
  num = num // 10
  if num < 1:
    return cont
  else: 
    cont += 1
    return recursion_3(num, cont)

print(recursion_3(1))