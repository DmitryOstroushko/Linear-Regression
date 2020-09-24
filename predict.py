#!/usr/bin/env python3
import argparse
from csv_funcs import *
from model import *

def options_parse() -> argparse.Namespace:
	"""
	Function to define arguments list for command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--verbose', '-v',
						dest='verbose',
						action='store_true',
						default=False,
						help='If set, verbosity mode is set')
	parser.add_argument('--mileage', '-m',
						action="store",
						dest="mileage",
						type=int,
						help='To set mileage to predict price')
	parser.add_argument('--draw', '-d',
						action="store_true",
						dest="draw",
						default=False,
						help='If set, drawing mode is set')
	return parser.parse_args()

def do_main_function() -> None:
	"""
	Main function of ft_liner_regression project: predict function
	"""
	try:
		options = options_parse()
	except:
		#error_message("Wrong type/value of command line arguments")
		sys.exit(1)
	if options.verbose:
		normal_message(options)

	if options.mileage is None:
		while True:
			print('\033[35mPlease enter a mileage:\033[0m')
			try:
				choice = input('\033[35m\033[0m')
			except EOFError:
				error_message('EOF on input. Exit..')
				sys.exit(0)
			except (KeyboardInterrupt, SystemExit):
				raise
			except:
				error_message('Unknown error on input. Exit...')
				sys.exit(-1)
			if choice.isdigit():
				options.mileage = int(choice)
				break
			else:
				error_message('{}: Not a valid value. It should be a positive integer.'.format(choice))
				sys.exit(-1)

	if options.mileage < 0:
		error_message('Negative value of mileage. It should be a positive.')
		sys.exit(-1)

	thetas = load_theta_from_csv()
	if options.verbose:
		normal_message('Thetas array is {}'.format(thetas))

	_, _, mileage_limits, mileage_range, price_limits = load_data_from_csv()
	if options.verbose:
		normal_message('Data parameters are:')
		normal_message('	limits of mileage is {}'.format(mileage_limits))
		normal_message('	range of mileage is  {}'.format(mileage_range))
		normal_message('	limits of price is   {}'.format(price_limits))

	y_pred = estimated_price([options.mileage], thetas, mileage_limits, mileage_range, price_limits)

	normal_message('Prediction is: {}'.format(y_pred))

if __name__ == '__main__':
	do_main_function()
