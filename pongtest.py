# pong game 0.3
import pygame
import sys
import threading
#import socket
#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
class pong:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen_width = 1530
		self.screen_height = 810
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		pygame.display.set_caption("P0NG")
		self.ball = pygame.Rect(self.screen_width/2 - 15, self.screen_height/2 - 15, 30, 30)
		self.player = pygame.Rect(self.screen_width - 20, self.screen_height/2 - 70, 10, 140)
		self.opponent = pygame.Rect(10, self.screen_height/2 - 70, 10, 140)
		self.bg_color = (0, 0, 0)
		self.white = (255, 255, 255)
		self.ball_speed_x = 6
		self.ball_speed_y = 6
		self.player_speed = 0
		self.opp()

	def player_animation(self):
		self.player.y += self.player_speed
		if self.player.top <= 0:
			self.player.top = 0
		if self.player.bottom >= self.screen_height:
			self.player.bottom = self.screen_height
			
	def opponent_animation(self,n,e):
		self.opponent.y += self.opponent_speed
		if self.opponent.top <= 0:
			self.opponent.top = 0
		if self.opponent.bottom >= self.screen_height:
			self.opponent.bottom = self.screen_height	

	def opp(self):
		self.opponent_speed = 0
		self.player_speed = 0
		while True:
			# input
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit() 	
					sys.exit()

				if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN:
							self.player_speed += 7
						if event.key == pygame.K_UP:
							self.player_speed -= 7
				if event.type == pygame.KEYUP:
						if event.key == pygame.K_DOWN:
							self.player_speed -= 7
						if event.key == pygame.K_UP:
							self.player_speed += 7  
			self.player_animation()
			#client.sendall(str.encode("\n".join([str(player.top), str(player.bottom)])))
			#n, e = [int(i) for i in client.recv(2048).decode('utf-8').split('\n')]
			
		
			self.screen.fill(self.bg_color)
			pygame.draw.rect(self.screen, self.white, self.player)
			pygame.draw.rect(self.screen, self.white, self.opponent)
		
			# updates the game window
			pygame.display.flip()
			self.clock.tick(65)
if __name__ == '__main__':
	pong()
