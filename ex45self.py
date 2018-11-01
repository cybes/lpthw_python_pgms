
class GoldFishRoom(object):
	def enter(self):
	
		print "You are in the Gold Fish room, Choose the number of Gold fishes"
		action = int(raw_input(">"))
		if action < 10 :
			print "You are good to go with the %s number of Gold fish, enjoy" %action
		else:
			#print "You have taken more number of gold fish"
			#return 'Gold'
			a_map.fish_more('Gold')
		
class KoiFishRoom(object):
	def enter(self):
		print "You are in the Koi Fish room, Choose the number of Koi fishes"
		action = int(raw_input(">"))
		if action < 5:
			print "You are good to go with the %s number of Koi Fish, enjoy" %action
		else:	
			a_map.fish_more('Koi')
		
class SharkFishRoom(object):
	def enter(self):
		print "You are in the shark Fish room, Choose the number of shark fishes"
		action = int(raw_input(">"))
		if action < 3:
			print "You are good to go with the %s number of shark Fish, enjoy" %action
		else:
			a_map.fish_more('Shark')
		
class PlatyFishRoom(object):
	def enter(self):
		print "You are in the platy Fish room, Choose the number of platy fishes"
		action = int(raw_input(">"))
		if action < 10:
			print "You are good to go with the %s number of shark Fish, enjoy" %action
		else:
			a_map.fish_more('Platy')
		
class GuppiFishRoom(object):
	def enter(self):
		print "You are in Guppi Fish room, Choose the number of Guppi Fishes"
		action = int(raw_input(">"))
		if action < 20:
			print "You are good to go with the %s number of shark Fish, enjoy" %action
		else:
			a_map.fish_more('Guppi')
		

	
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Testing", current_scene 
		while True:
			
			next_scene_name = current_scene.enter()
			print next_scene_name, "Testing"
			current_scene = self.scene_map.next_scene(next_scene_name)
			print current_scene, "Testing"
			if current_scene == None:
				exit(1)
		
class CorridorRoom(object):
	#def __init__(self,fishtype):
	#	self.fishtype = fishtype
	def enter(self):
		print "You are in an aquarium shop and going to buy some fish for your aquarium"
		print "How many gallons of water would your glass tank hold?"
		action = int(raw_input(">"))
		if action > 10:
			i = 0
			print "As your tank is large you can choose big fish like gold, koi, shark"
			#print self.largefish
			return a_map.largefish[i]
		else:
			i = 0
			print "Your tank is small so you need to choose small fish like platy,guppi"
			#print smallfish
			return a_map.smallfish[i]
class Map(object):
	scenes = {'Gold': GoldFishRoom(),
	'Koi': KoiFishRoom(), 'Shark': SharkFishRoom(),
	'Platy': PlatyFishRoom(), 'Guppi': GuppiFishRoom(), 'corridor': CorridorRoom()}
	largefish = ['Gold','Koi','Shark']
	smallfish = ['Platy','Guppi']
	
	def __init__(self,startscene):
		
		self.startscene = startscene
		
	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.startscene)
		
	def fish_more(self,fishname):
		self.fishname = fishname
		print "YOu are having too much %s ,take less number of fish" %fishname
		return fishname
		
a_map = Map('corridor')
a_game = Engine(a_map)
a_game.play()