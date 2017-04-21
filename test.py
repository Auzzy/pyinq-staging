from pyinq.tags import test
        
@test(expected=TypeError)
def false_positive():
	# kwargs = dict(("num1", "2"), ("num2",8))
	kwargs = {"num1":"2", "num2":8}
	add_values(kwargs.values())

def add_values(values):
	sum = 0
	for value in values:
		sum += int(value)
	return sum
