

state = 'main'

d = {'Philip Jordan': [500, 200], 'Tom Parker': [750, 800, 750], 'Lisa Smith': [500, 500], 'Wayne Tucker': [400, 500], 'Jane Winkle': [800, 800, 780]}



def menu():
	action = raw_input("Send a Thank You or Create a Report?")
	if action == 'q':
		return 'quit'
	elif action == 'Send a Thank You':
		return 'send a thank you'
	elif action == 'Create a Report':
		return 'create a report'

def thank_you():

	input_name = raw_input(u'Enter a first and last name')
	if input_name == 'list':
		print d
		input_name = raw_input(u'Enter a first and last name')
	elif input_name not in d:
		d[input_name] = []


	input_amount = raw_input(u'Enter a donation amount')
	if input_amount.isdigit():
		d[input_name].append((input_amount))
		print d
	else:
		input_amount = raw_input(u'Enter a donation amount')
		d[input_name].append((input_amount))
		print d
		return input_amount

					
	print u"""Dear %s, 	

		Thank you for your generous donation of $%s. Your contribution will help make the impossible, possible.

		Sincerely,

		OrganizationX""" % (input_name, input_amount)

thank_you()

def report():

	print d

report()

while True:
	if state == 'main':
		state = menu()
	if state == 'send a thank you':
		state = thank_you()
	if state == 'create a report':
		state = report()
	if state == 'quit':
		break





		


	
			

		






			
		








	


