a=6
if a-5>=0:
    print('a lon hon 0');
b=4
if b-1<=0:
    print('b lon hon 0')
elif b-3>=0:
    print('b bang 1')
elif b-4==0:
    print('b bang 0');
c=6
print('c bang 5' if c == 5 else 'c khac 5');
b = 2
if b - 1 < 0:
     print('b nhỏ hơn 1')
elif b - 1 > 0:
     print('b lớn hơn 1')
else:
     print('b bằng 1');
t = 3
match t:
     case 1: # Thực hiện lệnh bên trong nếu t = 1, tương đương với if t == 1
             print("t = 1")
     case 2: # Thực hiện lệnh bên trong nếu t = 2, tương đương với if t == 2
             print("t = 2")
     case 3: # Thực hiện lệnh bên trong nếu t = 3, tương đương với if t == 3
             print("t = 3")
     case _: # Lệnh bên trong được thực hiện nếu như tất cả các lệnh bên trên đều bị bỏ qua
      print("t > 3");
d=1
match d:
    case 1:
        print("d=1")
    case 1:
        print("d laf 1")


