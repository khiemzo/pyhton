i=5
while i>0:
    print('i=',i)
    i-=1;
k=3
while k<100:
    print('k=',k)
    k+=1;
s='thien khiem'
idx=10 # vị trí bắt đầu bạn muón xử lý của chuỗi
length = len(s)# lấy độ dài chuỗi làm mốc kết thúc
while 0<idx<length:
    print(idx,'stands for length',s[idx])
    idx-=1; #di chuyển index tới vị trí tiếp theo
g = 'How Kteam'
idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
length = len(g) # lấy độ dài chuỗi làm mốc kết thúc

while idx < length:
     print(idx, 'stands for', g[idx])
     idx += 1 # di chuyển index tới vị trí tiếp theo