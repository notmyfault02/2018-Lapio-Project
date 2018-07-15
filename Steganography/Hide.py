from PIL import Image

path = "C:\\Users\\DSM2018\\Desktop\\hello.png"

img = Image.open(path)
c_input = "{0:b}".format(ord(input("숨길 글자 >> ")))
c_input = [int(i) for i in c_input]

pixelmap = img.load()
pixelmop = img.load()

r_d=[]
c_index = 0
for i in range(0,7):
    if c_index > 6:
        break
    r, g, b = pixelmap[i, 0]
    r_d.append((r >> 1 << 1) + c_input[i])
    print("{0}:{1} {2:08b} {3:08b}".format(i, 0, r, r_d[i]))
    c_index+=1
    pixelmop[i, 0]= (r_d[i], g, b)
    

img.save("C:\\Users\\DSM2018\\Desktop\\hahaha.png")
print("바탕화면 hahaha.png 확인")