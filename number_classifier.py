def even_or_odd(number):
	if number % 2 == 0:
		return "even"
	else:
		return "odd"

def multiple_of(number):
	if number % 5 == 0:
		return "Y"
	else:
		return "N"

def result_squared(number):
	squared = number*number
	return	squared

def main():
	print ('Please enter a number...')
	number = int(input())
	print ('Your number is: ', even_or_odd(number))
	print ('Multiple of 5: ', multiple_of(number))
	print ('If you squared: ', result_squared(number))


if __name__ == '__main__':
	main()

