import typing
import csv
import sys
from stream_funcs import *

def load_theta_from_csv() -> list:
	theta_list: list = []
	try:
		with open('theta.csv', 'r') as data_file:
			data_content = csv.reader(data_file, delimiter=',')
			theta_list = [float(line[0]) for line in data_content]
			if len(theta_list) > 2:
				theta_list = theta_list[:2]
			if len(theta_list) < 2:
				error_message('Thetas array is not loaded')
				normal_message('Thetas array is filled by zeros')
				return [0, 0]
	except (FileNotFoundError):
		error_message('File with thetas array is not found')
		success_message('Thetas array is filled by zeros')
		return [0, 0]
	except:
		error_message('Thetas array is not loaded during error in theta value')
		success_message('Thetas array is filled by zeros')
		return [0, 0]
	success_message('Thetas array is loaded')
	return theta_list

def load_data_from_csv() -> typing.Tuple[list, list, list, int, list]:
	X: list = []
	y: list = []
	is_first_line = True
	try:
		with open('data.csv', 'r') as data_file:
			data_content = csv.reader(data_file, delimiter=',')
			for data_line in data_content:
				if is_first_line:
					if data_line[0] != 'km' or data_line[1] != 'price':
						error_message('It is wrong format of CSV file')
						sys.exit(1)
					else:
						is_first_line = False
				if data_line[0].isdigit():
					X.append(int(data_line[0]))
					y.append(int(data_line[1]))
	except (FileNotFoundError):
		error_message('File with data is not found')
		sys.exit(1)
	except:
		error_message('It is impossible to analyze CSV file')
		sys.exit(1)
	mileage_limits: list = [min(X), max(X)]
	mileage_range: int = mileage_limits[1] - mileage_limits[0]
	if not mileage_range:
		mileage_range = 1
	price_limits: list = [min(y), max(y)]
	success_message('Data is loaded')
	return X, y, mileage_limits, mileage_range, price_limits

def save_theta_to_csv(theta: list) -> None:
	try:
		with open('theta.csv', 'w') as data_file:
			for key in theta:
				data_file.write('{}\n'.format(key))
		success_message('Thetas array is saved')
	except:
		error_message('It is impossible to save theta values')
