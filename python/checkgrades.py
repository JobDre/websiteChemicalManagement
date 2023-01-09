
# >90 = A
# >80 = B
# >70 = C
# >60 = D
# <60 = F

grade = int(input("Enter score: "))

if grade >100:
  print("check the values! Number greater than maximum score")
elif grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

print("_____Pass List____")
if grade >= 60 and grade <=100:
  print("You have passed")
else:
  print("Retake")