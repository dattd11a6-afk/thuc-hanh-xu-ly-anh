import cv2
import numpy as np

img = cv2.imread('dog.png') 

if img is None:
    print("Lỗi: Không đọc được ảnh. Vui lòng kiểm tra lại đường dẫn file!")
    exit()

height, width, channels = img.shape
print(f"Kích thước ảnh gốc: {width}x{height}, Kênh màu: {channels}")

# R-G-B
B, G, R = cv2.split(img)

cv2.imshow("1. Kenh Red (R)", R)
cv2.imshow("1. Kenh Green (G)", G)
cv2.imshow("1. Kenh Blue (B)", B)

# Chuyển ảnh màu RGB thành ảnh xám theo công thức trung bình cộng
img_float = img.astype(np.float32)
gray_avg = (img_float[:,:,2] + img_float[:,:,1] + img_float[:,:,0]) / 3.0
gray_avg = gray_avg.astype(np.uint8) # Ép kiểu về số nguyên 8-bit

# Chuyển ảnh màu RGB thành ảnh xám theo phương pháp trọng số (Luminosity)
gray_lum_float = 0.299 * R.astype(np.float32) + 0.587 * G.astype(np.float32) + 0.114 * B.astype(np.float32)
gray_lum = gray_lum_float.astype(np.uint8)

_, binary_avg = cv2.threshold(gray_avg, 127, 255, cv2.THRESH_BINARY)
_, binary_lum = cv2.threshold(gray_lum, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("2. Xam (Trung binh cong)", gray_avg)
cv2.imshow("2. Xam (Trong so Luminosity)", gray_lum)
cv2.imshow("2. Nhi phan (Tu anh Luminosity)", binary_lum)

# HSV
R_norm = R.astype(np.float32) / 255.0
G_norm = G.astype(np.float32) / 255.0
B_norm = B.astype(np.float32) / 255.0

Cmax = np.maximum(np.maximum(R_norm, G_norm), B_norm)
Cmin = np.minimum(np.minimum(R_norm, G_norm), B_norm)
delta = Cmax - Cmin

H = np.zeros_like(Cmax)

with np.errstate(divide='ignore', invalid='ignore'):
    mask_r = (Cmax == R_norm) & (delta != 0)

    H[mask_r] = 60 * (((G_norm[mask_r] - B_norm[mask_r]) / delta[mask_r]) % 6)
    
    mask_g = (Cmax == G_norm) & (delta != 0)
    H[mask_g] = 60 * (((B_norm[mask_g] - R_norm[mask_g]) / delta[mask_g]) + 2)
    
    mask_b = (Cmax == B_norm) & (delta != 0)
    H[mask_b] = 60 * (((R_norm[mask_b] - G_norm[mask_b]) / delta[mask_b]) + 4)

S = np.zeros_like(Cmax)
with np.errstate(divide='ignore', invalid='ignore'):
    mask_s = Cmax != 0
    S[mask_s] = delta[mask_s] / Cmax[mask_s]

V = Cmax

H_cv2 = (H / 2.0).astype(np.uint8)
S_cv2 = (S * 255.0).astype(np.uint8)
V_cv2 = (V * 255.0).astype(np.uint8)

img_hsv = cv2.merge((H_cv2, S_cv2, V_cv2))
cv2.imshow("3. Mo hinh HSV", img_hsv)

# CMY
C = 255 - R
M = 255 - G
Y = 255 - B

img_cmy = cv2.merge((Y, M, C)) 
cv2.imshow("3. Mo hinh CMY", img_cmy)

# CMYK
R_norm = R.astype(float) / 255.0
G_norm = G.astype(float) / 255.0
B_norm = B.astype(float) / 255.0

# Tìm K
K = 1 - np.maximum(np.maximum(R_norm, G_norm), B_norm)

# Tìm CMY mới và bỏ qua cảnh báo 0
with np.errstate(divide='ignore', invalid='ignore'):
    C_cmyk = (1 - R_norm - K) / (1 - K)
    M_cmyk = (1 - G_norm - K) / (1 - K)
    Y_cmyk = (1 - B_norm - K) / (1 - K)
    
    C_cmyk[K == 1] = 0
    M_cmyk[K == 1] = 0
    Y_cmyk[K == 1] = 0

C_print = (C_cmyk * 255).astype(np.uint8)
M_print = (M_cmyk * 255).astype(np.uint8)
Y_print = (Y_cmyk * 255).astype(np.uint8)
K_print = (K * 255).astype(np.uint8)

cv2.imshow("3. CMYK - Kenh K (Black)", K_print)

cv2.waitKey(0)
cv2.destroyAllWindows()