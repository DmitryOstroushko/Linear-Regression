import argparse
import typing

def normalize_data(val: list) -> list:
	"""
	To train the model, we need to normalize the data
	"""
	maximum = max(val)
	minimum = min(val)
	if maximum - minimum:
		return [(num - minimum) / (maximum - minimum) for num in val]
	return [(num - minimum) for num in val]

def predict(X: list, theta: list) -> list:
	"""
	To predict and return a value
	"""
	return [theta[0] + x * theta[1] for x in X]

def cost(X: list, y: list, theta: list, options: argparse.Namespace) -> float:
	"""
	To determine the cost with given theta values
	"""
	y_pred = predict(X, theta)
	if options.square:
		return 1 / (2 * len(X)) * sum([(target - target_pred)**2 for target in y for target_pred in y_pred])
	else:
		return sum([(target - target_pred) for target in y for target_pred in y_pred])

def fit(X: list, y: list, thetas: list, options: argparse.Namespace) -> typing.Tuple[list, list, list]:
	"""
	To train the model
	"""
	count = 0
	theta0, theta1 = thetas[0], thetas[1]
	length = len(X)
	theta_history: list = []
	J_history: list = []
	while count < options.iter:
		accum_theta0, accum_theta1 = 0, 0
		for idx, _ in enumerate(X):
			t = theta0 + theta1 * X[idx] - y[idx]
			accum_theta0 += t
			accum_theta1 += (t * X[idx])
		theta0 -= options.alpha * (accum_theta0 / length)
		theta1 -= options.alpha * (accum_theta1 / length)
		J_cost = cost(X, y, [theta0, theta1], options)
		if options.auto_break and len(J_history) > 0 and J_history[-1] < J_cost:
			if options.verbose:
				print('A number of iterations is {}'.format(count))
				print('The best thetas array is {}'.format(thetas))
				print('Final thetas array is {}'.format([theta0, theta1]))
				print('The best cost func value is {}, final cost func value is {}'.format(J_history[-1], J_cost))
			return thetas, theta_history, J_history
		thetas[0], thetas[1] = theta0, theta1
		theta_history.append([theta0, theta1])
		J_history.append(cost(X, y, [theta0, theta1], options))
		count += 1
	return thetas, theta_history, J_history

def raw_estimated_price(x: float, theta: list) -> float:
	return theta[0] + theta[1] * x

def estimated_price(X: list, theta: list, mile_lim: list, mile_delta: float, price_lim: list) -> list:
	price_scaled = []
	for x in X:
		price = raw_estimated_price((x - mile_lim[0]) / mile_delta, theta)
		if not price:
			price_scaled.append(0.0)
		else:
			price_scaled.append(price * (price_lim[1] - price_lim[0]) + price_lim[0])

	return price_scaled
