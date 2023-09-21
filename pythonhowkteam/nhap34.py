x1 = float(input("Chiều dài hình chữ nhật 1: "))
y1 = float(input("Chiều rộng hình chữ nhật 1: "))
x2 = float(input("Chiều dài hình chữ nhật 2: "))
y2 = float(input("Chiều rộng hình chữ nhật 2: "))

dientich1 = x1 * y1
dientich2 = x2 * y2

if dientich1 > dientich2:
    print("Hình chữ nhật 1 lớn hơn hình chữ nhật 2.")
elif dientich1 < dientich2:
    print("Hình chữ nhật 2 lớn hơn hình chữ nhật 1.")
else:
    print("Hình chữ nhật 1 và hình chữ nhật 2 có diện tích bằng nhau.")
