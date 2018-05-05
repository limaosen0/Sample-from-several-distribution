import numpy as np
import scipy.stats as stats
import utils


def gaussian(sample_num, miu, sigma):

	mean, var, skew, kurt = stats.norm.stats(moments='mvsk')
	x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), 100)
	pdf = stats.norm.pdf(x)
	sample = stats.norm.rvs(size=sample_num) * sigma + miu
	utils.plot_curve_and_hist(x, pdf, sample, 'Gaussian pdf')
	
	return mean, var, skew, kurt, sample


def beta(sample_num, a, b):

	mean, var, skew, kurt = stats.beta.stats(a, b, moments='mvsk')
	x = np.linspace(stats.beta.ppf(0.01, a, b), stats.beta.ppf(0.99, a, b), 100)
	pdf = stats.beta.pdf(x, a, b)
	sample = stats.beta.rvs(a, b, size=sample_num)
	utils.plot_curve_and_hist(x, pdf, sample, 'Beta pdf')

	return mean, var, skew, kurt, sample


def gamma(sample_num, a):

	mean, var, skew, kurt = stats.gamma.stats(a, moments='mvsk')
	x = np.linspace(stats.gamma.ppf(0.01, a), stats.gamma.ppf(0.99, a), 100)
	pdf = stats.gamma.pdf(x, a)
	sample = stats.gamma.rvs(a, size=sample_num)
	utils.plot_curve_and_hist(x, pdf, sample, 'Gamma pdf')

	return mean, var, skew, kurt, sample


def laplace(sample_num):

	mean, var, skew, kurt = stats.laplace.stats(moments='mvsk')
	x = np.linspace(stats.laplace.ppf(0.01), stats.laplace.ppf(0.99), 100)
	pdf = stats.laplace.pdf(x)
	sample = stats.laplace.rvs(size=sample_num)
	utils.plot_curve_and_hist(x, pdf, sample, 'Laplace pdf')

	return mean, var, skew, kurt, sample