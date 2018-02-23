from scipy import misc

image = misc.imread('img.jpg')
r = image[:,:,0]

with open("r.txt", 'a') as txt:
    for i in r:
        txt.write(str(i))
print(r)
g = image[:,:,1]

with open("g.txt", 'a') as txt:
    for i in r:
        txt.write(str(i))
print(r)
b = image[:,:,2]

with open("b.txt", 'a') as txt:
    for i in r:
        txt.write(str(i))
print(r)



