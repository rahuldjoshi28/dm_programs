import random
import copy

def binning_by_means(bins):
	for b in bins:
		avg = sum(b)/len(b)
		for it in range(len(b)):	
			b[it] = avg
	return bins

def binning_by_bounds(bins):
	for i, b in enumerate(bins):
		min_b = min(b)
		max_b = max(b)
		for it, k in enumerate(b):
			if( abs(min_b - k) > abs(max_b - k) ):
				b[it] = max_b
			else:
				b[it] = min_b
	return bins

def print_bin(bins):
	for i, b in enumerate(bins):
		print("Bin ", i, " : ", b)

if __name__ == '__main__':
	print("Enter number of elemetns: ")
	n = int(input())

	li = [random.random() * 20 for _ in range(1, n + 1)]

	print("Enter number of bins: ")
	k = int( input() )

	li.sort()

	bins = []

	p = int(n / k)

	for i in range(k):
		if(i == k - 1):
			bins.append(li[i * p:])
		else:
			bins.append(li[i * p: i * p + p])

	mean_bins = binning_by_means(copy.deepcopy(bins))

	bound_bins = binning_by_bounds(copy.deepcopy(bins))

	print("")
	print("Original bins:")
	print_bin(bins)

	print("")

	print("Bins by mean")
	print_bin(mean_bins)

	print("")

	print("Bins by bounds:")
	print_bin(bound_bins)
