try:
	import vk
except:
	print("Напиши: pip install vk")

from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')


def main ():

	print ("""

Наш уютный Телеграм: @Termuxtop
 ▌ ▐·▄ •▄ ▄• ▄▌ ▄▄▄· ▄▄▄·▄▄▄ .▄▄▄  
▪█·█▌█▌▄▌▪█▪██▌▐█ ▄█▐█ ▄█▀▄.▀·▀▄ █·
▐█▐█•▐▀▀▄·█▌▐█▌ ██▀· ██▀·▐▀▀▪▄▐▀▀▄ 
 ███ ▐█.█▌▐█▄█▌▐█▪·•▐█▪·•▐█▄▄▌▐█•█▌
. ▀  ·▀  ▀ ▀▀▀ .▀   .▀    ▀▀▀ .▀  ▀

[1] -> Накрутка репостов
[2] -> Накрутка лайков
[3] -> Накрутка подписчиков

	""")

	task = input ('Введите задачу:')

	tokens = input ('Введите название файл с токенами:')

	with open(tokens, 'r') as f:
		nums = f.read().splitlines()

	if task == '1':
		objectid = input ('Введите строковый ID объекта:')
		message = input ('Сообщение к репосту (необязательно):')

		for token in nums:
			try:
				session = vk.Session(access_token=token)
				api = vk.API(session ,v='5.92', lang='ru')

				api.wall.repost (object=objectid, message=message)

				print ('Репост сделан!')
				
			except:
				print ('Черт... Репост не сделан!')
				continue

	elif task == '2':
		id_person = input ('Введите ID страницы (для сообществ ID начинается с минуса):')
		id_post = input ('Введите ID поста:')

		for token in nums:
			try:
				session = vk.Session(access_token=token)
				api = vk.API(session ,v='5.92', lang='ru')

				api.likes.add (type='post', owner_id=id_person, item_id=id_post)

				print ('Лайк поставлен!')
				
			except:
				print ('Черт... Лайк не поставлен!')
				continue


	elif task == '3':
		id_group = input ('Введите ID страницы:')

		for token in nums:
			try:
				session = vk.Session(access_token=token)
				api = vk.API(session ,v='5.92', lang='ru')

				api.groups.join (group_id=id_group)

				print ('Подписка оформлена!')
				

			except:
				print ('Черт... Не могу подписаться!')
				continue
		


if __name__ == '__main__':
	clear()
	main()