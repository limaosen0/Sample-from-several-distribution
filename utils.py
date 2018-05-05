import matplotlib.pyplot as plt


def plot_curve_and_hist(x, y, value, label):

	fig, ax = plt.subplots(1,1)
	ax.plot(x, y, 'r-', lw=5, alpha=0.6, label=label)
	ax.hist(value, normed=True, histtype='stepfilled', alpha=0.2)
	ax.legend(loc='best', frameon=False)
	plt.show()