import statistics

nums = [1, 5, 33, 12, 46, 33, 2]

# calculate mean
mean = statistics.mean(nums)
result = "mean: {}".format(mean)
print(result)

# calculate median
median = statistics.median(nums)
result = "median: {}".format(median)
print(result)

# calculate mode
mode = statistics.mode(nums)
result = "mode: {}".format(mode)
print(result)

# calculate populative standard deviation
pstdev = statistics.pstdev(nums)
result = "populative standard deviasion: {}".format(pstdev)
print(result)

# calculate populative variance
pvar = statistics.pvariance(nums)
result = "populative variance: {}".format(pvar)
print(result)
