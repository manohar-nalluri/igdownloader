import requests 
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description=''''--->By this python script you can save videos and photos of non private insta account''')
args = parser.parse_args()
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
class instagram_saver:
	def __init__(self,link_address):
		link=requests.get(f'{link_address}').text
		self.soup=BeautifulSoup(link,'lxml')
		self.meta=self.soup.head.findAll('meta',{'content': True})
		
		
	def image_saver(self):
		try:
			image_link=self.meta[9]['content']
			image_source=requests.get(f'{image_link}')
			print(green+'Enter name to save as')
			print()
			name=input(cyan+'-->')
			size=len(image_source.content)/1000
			with open(f'{name}.png','wb') as image:
				image.write(image_source.content)
			print(f'[+]size: {size}kb')
			print(yellow+f'''[+]Image saved as {name}.png''')
		except:
			print(red+'[-]oops i think its an private account ')
		
		
	def video_saver(self):
		try:
			video_link=self.meta[22]['content']
			video_source=requests.get(f'{video_link}')
			print(green+'Enter name to save as')
			print()
			name=input(cyan+'-->')
			size=len(video_source.content)/1000
			with open(f'{name}.mp4','wb') as video:
				video.write(video_source.content)
			print(f'[+]size: {size}kb')
			print(yellow+f'[+]video saved as {name}.mp4')
		except:
			print(red+'[-]oops i think its an private account')
			
		

try:		
	print(red+'''
╔══╗───╔╗───────────────╔╗
╚║║╬═╗╔╝╠═╦╦╦╦═╦╦╗╔═╦═╗╔╝╠═╦╦╗
╔║║╣╬║║╬║╬║║║║║║║╚╣╬║╬╚╣╬║╩╣╔╝
╚══╬╗║╚═╩═╩══╩╩═╩═╩═╩══╩═╩═╩╝
───╚═╝''')
	print(clear+'='*30)
	print(yellow+bold+'<--code by manu-->'.center(30,' '))
	print(green+'''1.video
2.image
''')
	information=int(input(cyan+'-->'))
	print()
	
	if information==1:
			print(green+'''$paste url of the post
	
''')
			box=instagram_saver(link_address=input(cyan+'-->'))
			box.video_saver()
	elif information==2:
			print(green+'''$paste url of the post
	
''')
			box=instagram_saver(link_address=input(cyan+'-->'))
			box.image_saver()
	else:
			print(red+bold+'[-]Input valid number and try again')
except:
	print(red+bold+'''[-]oops!  check the url''')

		
	
		
		


