"""
'kkkkk'.count('k')
5
'kkkkk'.count('kk')
2
'kkkkk'.count('k', 3)
2
 'kkkkk'.count('k', 3, 4)
1
"""
'kkkkkkk'.count('k')
print('kkkkkkk'.count('k'))
"""
<chuỗi>.startswith(prefix[, start[, end]])

Công dụng: Trả về  giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False.

Hai yếu tố start, end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.
Ví dụ:

>>> 'how kteam free education'.startswith('ho')
True
>>> 'how kteam free education'.startswith('ha')
False
>>> 'how kteam free education'.startswith('ho', 4)
False
"""