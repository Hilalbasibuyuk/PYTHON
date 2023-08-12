
for i in range (1, 11): 
  for j in range (11-i): 
    print (" ", end = " ")
  for j in range (1, i):
    print ("*", end = " ")
    
  for i in range (i, 0, -1):
    print ("*", end = " ")
  
print () 



""" Exercise 2
for satir in range(1, 6):
    for sutun in range(1, (satir + 1)):
        print("* ", end=" ")
    print()
        
for x in range(1, 6):
    for sutun in range(1, (6 - x)):
        print("* ", end=" ")
    print()
"""
    