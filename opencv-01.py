import cv2

print("Phiên bản OpenCV:", cv2.__version__)

# Đọc file ảnh và kiểm tra đường dẫn
img = cv2.imread("anh_phong_canh.png")

if img is None:
    print("Lỗi: Không tìm thấy file ảnh trong thư mục hiện tại!")
    exit()

# Hiển thị kích thước ảnh
height, width, channels  = img.shape 
print(f"Kích thước ảnh gốc: Cao = {height}px, Rộng = {width}px, Kênh màu = {channels}")
print(img.shape)

# Hiển thị ảnh gốc
cv2.imshow("Anh Goc", img)

# Tăng/giảm kích thước ảnh
img_32 = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
img_128 = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)
img_256 = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
img_512 = cv2.resize(img, (512, 512), interpolation=cv2.INTER_LINEAR)

''' Chuyển đổi không gian màu sang ảnh xám và ảnh nhị phân
    Chuyển từ BGR sang Grayscale bằng cv2.cvtColor()'''
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

nguong_thong_minh, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Ngưỡng OpenCV tự động tính ra là:", nguong_thong_minh)

# Vẽ hình và chèn thông tin lên bản sao của ảnh
img_draw = img.copy()

# Vẽ đường thẳng ngang
cv2.line(img_draw, (198, 256), (263, 262), (255, 0, 255), thickness=3)

# Vẽ hình chữ nhật
cv2.rectangle(img_draw, (90, 45), (370, 285), (0, 255, 0), thickness=2)

# Vẽ hình tròn
cv2.circle(img_draw, (184, 163), 23, (0, 0, 255), thickness=3)

cv2.circle(img_draw, (271, 163), 23, (204, 0, 204), thickness=3)

# Chèn mã sinh viên và họ tên
cv2.putText(
    img_draw,
    "MSV: 20233453 - Ho ten: Do Phat Dat",
    (20, 38),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 255, 255),
    2,
    cv2.LINE_AA
)

# Hiển thị các ảnh đã tạo
cv2.imshow("Resize 32x32", img_32)
cv2.imshow("Resize 128x128", img_128)
cv2.imshow("Resize 256x256", img_256)
cv2.imshow("Anh Xam", gray_img)
cv2.imshow("Anh Nhi Phan", binary_img)
cv2.imshow("Anh Chen Chu", img_draw)

# Lưu tất cả ảnh đã thay đổi ra file mới
cv2.imwrite("anh_32x32.png", img_32)
cv2.imwrite("anh_128x128.png", img_128)
cv2.imwrite("anh_256x256.png", img_256)
cv2.imwrite("anh_512x512.png", img_512)
cv2.imwrite("anh_xam.png", gray_img)
cv2.imwrite("anh_nhi_phan.png", binary_img)
cv2.imwrite("anh_ket_qua.jpg", img_draw)

cv2.waitKey(0)
cv2.destroyAllWindows()