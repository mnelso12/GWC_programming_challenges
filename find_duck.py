birds = ['duck', 'duck', 'duck', 'duck', 'goose', 'duck', 'duck']

def find_index_of_goose():
	counter = 0
	for element in birds:
		if element == 'goose':
			print(counter)
		counter += 1

find_index_of_goose()

def count_ducks(animal):
	counter = 0
	for element in birds:
		if element == animal:
			counter += 1
	print('number of ' + animal + " " + str(counter))

count_ducks('duck')
count_ducks('goose')
