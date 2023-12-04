gifts = []
instruction_count = 0
floor_count = 0
with open("./input.txt") as INPUT:
  gifts = INPUT.read().splitlines()

def getMinPerimeter(l:int, w:int, h:int):
  return 2*min(l+w, w+h, h+l)

def getVolume(l:int, w:int, h:int):
  return l*w*h

result = 0

for gift in gifts:
  l,w,h = gift.split('x')
  ribbon = getMinPerimeter(int(l),int(w),int(h)) + getVolume(int(l),int(w),int(h))
  # print(ribbon)
  result += ribbon

print(result)