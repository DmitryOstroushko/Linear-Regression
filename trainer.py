#!/usr/bin/env python3

import sys
import math
import argparse
import matplotlib.pyplot as plt

from stream_funcs import *
from csv_funcs import *
from model import *

def options_parse():
	"""
	Function to define arguments list for command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--verbose', '-v',
						dest='verbose',
						action='store_true',
						default=False,
						help='If set, verbosity mode is set')
	parser.add_argument('--auto_break', '-b',
						dest='auto_break',
						action='store_true',
						default=False,
						help='If set, the program will be stopped when cost functions has min value')
	parser.add_argument('--iteration', '-i',
						action="store",
						dest="iter",
						type=int,
						default=500,
						help='To set a number of iterations (default is 500)')
	parser.add_argument('--coeff', '-c',
						action="store_true",
						dest="coeff",
						default=False,
						help='If set, counting will start from known coefficients from CSV file')
	parser.add_argument('--learningRate', '-l',
						action="store",
						dest="alpha",
						type=float,
						default=0.2,
						help='To set learning coefficient (default is 0.2)')
	parser.add_argument('--draw', '-d',
						action="store_true",
						dest="draw",
						default=False,
						help='If set, drawing mode is set')
	return parser.parse_args()

def do_main_function():
	"""
	Main function of ft_liner_regression project
	"""
	try:
		options = options_parse()
	except:
		error_message("Wrong type/value of command line arguments")
		sys.exit(1)
	if options.verbose:
		normal_message(options)
	if options.alpha <= 0:
		error_message('{}: Wrong learning coefficient. It should be more than 0.'.format(options.alpha))
		sys.exit(1)
	X_original, y_original, mileage_limits, mileage_range, price_limits = load_data_from_csv()

	X = normalize_data(X_original)
	y = normalize_data(y_original)

	thetas = [0 ,0] if not options.coeff else load_theta_from_csv()
	if options.verbose:
		normal_message('Thetas array is {}'.format(thetas))
	try:
		thetas, thetas_history, J_history = fit(X, y, thetas, options)
	except:
		error_message('It is impossible to count gradient descent')
		error_message(sys.exc_info()[1].args[0])
		sys.exit(1)
	save_theta_to_csv(thetas)
	if options.verbose:
		normal_message('Thetas history is {}'.format(thetas_history))

	if options.draw:
		plt.gcf().canvas.set_window_title('Cost Function')
		plt.ylabel('Price differential')
		plt.xlabel('iteration')
		plt.grid(True)
		plt.title('Price differential = f(descent)')
		plt.plot([_ for _ in range(len(J_history))], J_history, 'r--', label='Precision')
		plt.show()

	if options.draw:
		y_pred = estimated_price(X_original, thetas, mileage_limits, mileage_range, price_limits)
		plt.gcf().canvas.set_window_title('PRICE: real vs prediction')
		plt.ylabel('Price')
		plt.xlabel('mileage')
		plt.grid(True)
		plt.title('Price = f(mileage)')
		#plt.plot([_ for _ in range(len(y_original))], y_original, 'b--', label='Real price')
		#plt.plot([_ for _ in range(len(y_pred))], y_pred, 'r--', label='Predicted price')
		plt.plot(X_original, y_original, 'b--', label='Real price')
		plt.plot(X_original, y_pred, 'r--', label='Predicted price')
		plt.legend(loc="upper right")
		plt.show()

if __name__ == '__main__':
	do_main_function()
