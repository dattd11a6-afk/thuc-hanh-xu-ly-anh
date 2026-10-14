import cv2

# Đọc ảnh gốc
img = cv2.imread('C:\\Users\\Lenovo\\Pictures\\hinh-anh\\conCho.png')

if img is None:
    print("Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn.")
else:
    # Xử lý
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 100, 200) # Thường tìm cạnh trên ảnh xám sẽ tốt hơn
    # Thay đổi thành kích thước cố định: Rộng 500px, Cao 300px
    resized_img = cv2.resize(img, (500, 300))
    # (5, 5) là kích thước kernel (phải là số lẻ), số càng lớn ảnh càng mờ
    blurred_img = cv2.GaussianBlur(img, (3, 3), 0)
    
    # Hiển thị
    cv2.imshow('Anh Goc', img)
    cv2.imshow('Anh Xam', gray_img)
    cv2.imshow('Thay doi kich thuoc anh', resized_img)
    cv2.imshow('Lam mo anh', blurred_img)
    cv2.imshow('Tim Canh (Edges)', edges)

    # Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ hiển thị
    cv2.waitKey(0)
    cv2.destroyAllWindows() # Đóng tất cả cửa sổ sau khi nhấn phím
