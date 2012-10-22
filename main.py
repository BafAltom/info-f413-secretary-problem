import math
import random

NUMBER_OF_TESTS = 1000
SIZE_OF_SAMPLE = 100

def generate_candidates(n):
	l = []
	for i in range(n):
		randPos = random.randint(0,len(l))
		l.insert(randPos, i)
	return l

def interview(candidates, m):
	n = len(candidates)
	assert (n > m)
	assert (n > 1)
	best_candidate = candidates[0]
	# find best candidate in the first m candidates
	for i in range(m):
		if (candidates[i] > best_candidate):
			best_candidate= candidates[i]
	# find a new better candidate
	for i in range(m, n):
		if (candidates[i] > best_candidate):
			return candidates[i]
	return None

def compute_best_m(n):
	return int(round(n/math.e))

if __name__ == "__main__":
	fileM = open("output_m.csv", "w")
	fileV = open("output_value.csv", "w")
	list_of_m = []
	for i in range(0, SIZE_OF_SAMPLE, 1):
		list_of_m.append(i)
	#list_of_m.append(compute_best_m(SIZE_OF_SAMPLE))
	current_best_success = 0
	current_best_m = 0
	theor_best_m = compute_best_m(SIZE_OF_SAMPLE)
	theor_best_success = 0
	for m in list_of_m:
		print m, "/", len(list_of_m)
		successCount = 0
		testCount = 0
		for i in range(NUMBER_OF_TESTS):
			candidates = generate_candidates(SIZE_OF_SAMPLE)
			bestCandidate = max(candidates)
			hiredGuy = interview(candidates, m)
			if (hiredGuy == bestCandidate):
				successCount += 1
			testCount += 1
		successRate = float(successCount)/testCount
		if (successRate > current_best_success):
			current_best_success = successRate
			current_best_m = m
		if (m == theor_best_m):
			theor_best_success = successRate
		fileM.write(str(m) + ",\n")
		fileV.write(str(successRate) + ",\n")
	print "theoretical value :", theor_best_m, "success:", theor_best_success, "> 1/e = ", round(1/math.e, 2)
	print "actual best m :", current_best_m, "success:", current_best_success
	
