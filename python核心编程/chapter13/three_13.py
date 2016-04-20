# coding: utf-8

class MoneyFmt(object):
    #constructor
	def __init__(self, value = 0.0):
		self.value = float(value)
    
	#allow updates    
	def update(self, value = None):
		if value != None:
			self.value = float(value)
			print 'New value: ', self.value
		else:
			pass
    
    # display as a float
	def __repr__(self):
		return 'self.value'
    
	# formatted display
	def __str__(self):
		val = ''
		roundi = round(self.value, 2)
		absi = abs(roundi)
		if (absi * 10) % 1 == 0:
			value = format(absi, ',') + '0'
		else:
			value = format(absi, ',')
        
		if roundi >= 0:
			val = '$' + value
		else:
			val = '-' + '$' + value
        
		return val
    
	# boolean test
	def __nonzero__(self):
		if float(self.value) > 0:
			return True
		else:
			return False
		return int(self.value)
