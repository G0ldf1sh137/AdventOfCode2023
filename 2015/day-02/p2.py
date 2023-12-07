gifts = []
instruction_count = 0
floor_count = 0
with open("./input.txt") as INPUT:
  gifts = INPUT.read().splitlines()

def getSurfaceArea(l:int, w:int, h:int):
  return 2*(l*w + w*h + h*l)

def getSlack(l:int, w:int, h:int):
  return min(l*w, w*h, h*l)

result = 0

for gift in gifts:
  l,w,h = gift.split('x')
  sf = getSurfaceArea(int(l),int(w),int(h)) + getSlack(int(l),int(w),int(h))
  result += sf

print(result)