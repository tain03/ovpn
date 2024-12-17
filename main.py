import os

# Đường dẫn thư mục chứa các thư mục con
parent_folder = r"C:\Users\hieu3\Desktop\ovpn"

# Duyệt qua tất cả các thư mục và file con
for root, dirs, files in os.walk(parent_folder):
    for file in files:
        # Kiểm tra nếu file có đuôi .txt
        if file.endswith('.txt'):
            # Xây dựng đường dẫn cũ và mới
            old_file_path = os.path.join(root, file)
            new_file_name = file.replace('.txt', '.ovpn')
            new_file_path = os.path.join(root, new_file_name)

            # Đổi tên file
            os.rename(old_file_path, new_file_path)
            print(f"Đã đổi tên {old_file_path} thành {new_file_path}")
