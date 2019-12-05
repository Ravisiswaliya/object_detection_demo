import requests
import random

a = 0
for i in url:
	a = a+1
	b = 'photo'+str(a)+'.jpg'
	f = open(b,'wb')
	f.write(requests.get(i).content)
	f.close()
	print(a)

with open('women_t_shirt_images.txt') as f:
   x = f.read()
   #print(type(x))
   lines = x.split('\n')
   #print(lines)
   for i,l in enumerate(lines[1:300]):
   	b = 'photo'+str(random.randint(1,400))+'.jpg'
   	f = open(b,'wb')
   	f.write(requests.get(l).content)
   	f.close()
   	print(i)







