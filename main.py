from ultralytics import YOLO
from api import print_recipes
model = YOLO("best.onnx", task="detect")

results = model("image.jpg")
ingredients = ""

for result in results:
    boxes = result.boxes
    names = result.names
    list = [0] * 100
    for i in boxes.cls:
        list[int(i.item())] += 1
    for j in range(0, 100):import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
from api import print_recipes

def select_image():
    # Mở hộp thoại để chọn hình ảnh và lấy đường dẫn của hình ảnh đã chọn
    file_path = filedialog.askopenfilename()
    # Hiển thị đường dẫn của hình ảnh trên giao diện người dùng (tùy chọn)
    image_path_label.config(text="Selected Image: " + file_path)
    # Gọi hàm detect_objects với đường dẫn của hình ảnh đã chọn
    detect_objects(file_path)

def detect_objects(image_path):
    # Khởi tạo mô hình YOLO với tệp mô hình 'best.onnx' và cấu hình 'detect'
    model = YOLO("best.onnx", task="detect")
    # Phát hiện các đối tượng trong hình ảnh và lưu kết quả vào biến results
    results = model(image_path)
    # Khởi tạo biến ingredients để lưu trữ danh sách các nguyên liệu
    ingredients = ""
    # Duyệt qua từng kết quả phát hiện
    for result in results:
        # Lấy thông tin về hộp giới hạn (boxes) và tên các đối tượng (names) từ kết quả phát hiện hiện tại
        boxes = result.boxes
        names = result.names
        # Khởi tạo một danh sách đếm để đếm số lần xuất hiện của mỗi loại đối tượng
        count_list = [0] * 100
        # Duyệt qua các lớp của các hộp giới hạn và tăng giá trị tương ứng trong danh sách đếm
        for i in boxes.cls:
            count_list[int(i.item())] += 1
        # Duyệt qua danh sách đếm và in ra số lần xuất hiện và tên của từng đối tượng
        for j in range(0, 100):
            if count_list[j] != 0:
                print(count_list[j], " ", names[j])
                # Thêm tên đối tượng vào biến ingredients với ký tự phân tách là ','
                ingredients += names[j] + ",+"
    # Gọi hàm print_recipes với danh sách nguyên liệu, loại bỏ ký tự phân tách cuối cùng (',+') 
    print_recipes(ingredients[:-2])

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Object Detection")

# Tạo nút để chọn hình ảnh
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

# Label để hiển thị đường dẫn của hình ảnh đã chọn
image_path_label = tk.Label(root, text="")
image_path_label.pack()

# Chạy cửa sổ chính
root.mainloop()

        if list[j] != 0:
            print(list[j]," ", names[j])
            ingredients += names[j] + ",+"

print_recipes(ingredients[:-2])
