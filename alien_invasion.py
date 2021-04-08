import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""管理游戏资源和行为的类"""

	def __init__(self):
		"""初始化游戏并创建游戏资源"""
		pygame.init()
		self.settings=Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship=Ship(self)


	def run_game(self):
		"""开始游戏的循环"""
		while True:
			#监听键盘和鼠标事件
			self._check_events()
			self._update_screen()

			
	def _check_events(self):
		"""监听键盘和鼠标事件"""
		for event in pygame.event.get():

				#如果鼠标点击屏幕右上角的关闭，就退出整个游戏
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.ship.rect.x +=2
					elif event.key == pygame.K_LEFT:
						self.ship.rect.x -=2
				#elif event.type == pygame.KEYUP:
				#	self.ship.rect.y +=2

	def _update_screen(self):
		#每次循环都重绘屏幕
			
			self.screen.fill(self.settings.background_color)
			self.ship.blitmyship()

			#让最近绘制的屏幕可见
			pygame.display.flip()


if __name__ == '__main__':
	#创建游戏实例并运行游戏
	ai = AlienInvasion()
	ai.run_game()
