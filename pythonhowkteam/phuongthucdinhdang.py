#công thức: <chuỗi>.center(width,[fillchar])
#công dụng:  Trả về một chuỗi được căn giữa với chiều rộng width.

Nếu fillchar là None (không được nhập vào) thì sẽ dùng kí tự khoảng trắng để căn, không thì sẽ căn bằng kí tự fillchar.
Một điều nữa là kí tự fillchar là một chuỗi có độ dài là 1.
 'abc'.center(12)
'    abc     '
 'abc'.center(12, '*')
'****abc*****'
 'abc'.center(12, '*a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: The fill character must be exactly one character long
#<chuỗi>.rjust(width, [fillchar])
Công dụng: Cách hoạt động tương tự như phương thức center, có điều là căn lề phải

>>> 'kteam'.rjust(12)
'       kteam'
>>> 'kteam'.rjust(12, '*')
'*******kteam'