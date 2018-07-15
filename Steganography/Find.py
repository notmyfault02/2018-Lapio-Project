from PIL import Image

filename=input('이미지 파일의 경로를 적어주세요(ex: 드라이브:\\\...\\\파일명.파일형식): ') #이미지 경로 입력
img = Image.open(filename) #입력한 경로의 이미지 불러오기
width, height=img.size
pixelmop=img.load()
r_arr = []

for i in range(0,7):
    r, g, b = pixelmop[i, 0]
    r_arr.append("{0:b}".format(r).zfill(8))
    print(r_arr[i])

lsb_arr = []
for j in range(0,7):
    lsb_arr.append(r_arr[j][7])

asc_arr = []
for i in range(0,7):
    asc_arr += lsb_arr[i]
    
asc_arr_new=""
for k in asc_arr:
    asc_arr_new+=str(k)
print(asc_arr_new)
print("숨겨진 글자는", chr(int(asc_arr_new,2)))
