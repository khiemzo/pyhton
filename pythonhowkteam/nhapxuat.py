print('khiem'+str(34));
print('khiem', str(34));
print('khiem'+'khang');
print('khiem','khang');
print('khiêm','không','thích',sep='000');
print('khiêm','không','thích',sep="000");
print('khiêm','không','thích',sep='')

from time import sleep
your_name = "Henry"
your_great = "hello! My name is "
for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
    print()
# khi thục đầu dòng của print ngang với các chữ cái tự động tách ra thành từng dòng khác nhau 
your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
# khi chỉ xuống dòng và không thục đầu dòng thì chương trình sẽ thực hiện đúng với thứ tự dòng code phía trên bởi vì print lúc này đang là 1 lệnh mới