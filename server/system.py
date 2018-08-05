import requests, os

class system():

	def check_network(Status):
		try:
			Request = requests.get("https://music.163.com")
			Delay = str(int(Request.elapsed.microseconds/1000)) + 'ms'
			return Delay
		except:
			if Status == 'Init':
				print('\33[1;37;41m无法与网易云音乐建立连接，无法使用本程序。\33[0m')
				exit()
			else:
				pass

	def clear(Platform):
		if Platform == 'Windows':
			ClearCommand = 'cls'
		else:
			ClearCommand = 'clear'
		os.system(ClearCommand)
