#密碼重試程式
#password = 'a123456'
#讓使用只重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功!""
#如果不正確 就印出"密碼錯誤！ 還有＿次機會！"

password = 'a123456'
y = 2
while 0 <= y < 3:
	x = input('請輸入密碼：')
	if x == password:
		print('登入成功！')
		break
	else:
		if y > 0:
			print('密碼錯誤！還有', y , '次機會！')
			y = y - 1
		else:
			print('登入失敗！')
			break
else:
	print('登入失敗！')

