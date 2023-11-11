password = 'a123456'
x = input('請輸入密碼：')
while x != password:
	print('密碼錯誤！ 還有2次機會')
	x1 = input('請輸入密碼：')
	if x1 != password:
		print('密碼錯誤！ 還有1次機會')
		x2 = input('請輸入密碼：')
		if x2 != password:
			print('登入失敗！')
			break
		else:
			print('登入成功！')
			break
	else:
		print('登入成功！')
		break
else:
	print('登入成功！')



