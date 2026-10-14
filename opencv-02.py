import cv2, random

img = cv2.imread("conCho.png", 1)

print(img)
print(type(img))

print(img.shape)

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

vungchon = img[0:100]
cv2.imshow("anh", img)
cv2.waitKey(0)