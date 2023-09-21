
name = input("Nhập tên của bạn: ")
print()

if age < 18:
    print("Xin chào,", name + "!")
    print("Bạn không thể lái xe ô tô vì bạn chưa đủ tuổi.")
else:
    driving_license = input("Bạn có bằng lái xe không? (Có/Không): ")
    print("Xin chào,", name + "!")
    if driving_license.lower() == "có":
        print("Bạn có thể lái xe ô tô.")
    else:
        print("Bạn không thể lái xe ô tô vì bạn không có bằng lái.")

