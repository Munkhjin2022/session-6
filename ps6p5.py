
First=0
Second=1

for nx in range(1,21):
  if nx<=1:
      next=nx
  else:
      next=First+Second
      First=Second
      Second=next

  print(next) 