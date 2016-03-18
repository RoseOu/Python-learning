class bird(object):
	name ='Rig'
	age = '18'
	def eat(self):
		print 'eat'
		
	def sing(self):
		print 'sing'
	
b = bird()
print b.name,b.age
b.eat()
b.sing()

class lark(bird):
	name = 'jing'
	age = '18'
	def eat(self):
		print 'eat'
		
l = lark()
print l.name,l.age
l.eat()

