ages = [18,34,55,24]

delta = int(input("Enter an age:"))

while delta!=0:
  if delta in ages:
    print("You have already entered that age: ")
  else:
    ages.append(delta)
  
  delta = int(input("Enter an age: "))
  
ages.sort()
print("List of ages in your list:", ages)
  