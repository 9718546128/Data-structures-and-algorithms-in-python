def linear_search(alist,key):
  for item in alist:
    if item == key:
      return True

  return False

key = 10
alist = [20,50,40,60,10,80]
print("item {} found in  {} ?: {}".format(key, alist, linear_search(alist, key)))
