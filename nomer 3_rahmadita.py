# class Statistic:
#     def __init__(self, sample):
#         self.sample = sample

sample = [1,2,3,7]
n = len(sample)
# MEAN
def mean (sample):
    return sum(sample) / len (sample)

print(f'mean adalah: {mean(sample)}')

#MEDIAN
def median (sample):
    n = len(sample)
    sample.sort()

    if n % 2 == 0:
        median1 = sample[n//2]
        median2 = sample[n//2 - 1] 
        median = (median1 + median2)/2        
    else: 
        median = sample[n//2]
    print("Median adalah: " + str(median))



#MODUS
def mode(sample):
    most = max(map(sample.count, sample)) if sample else None
    mset = set(filter(lambda x: sample.count(x) == most, sample))
    return mset if set(sample) - mset else "Tidak ada modus!" 
print(f'modus adalah: {mode(sample)}')

# STD DEVIASI
import math

mean = sum(sample) / len(sample)   # mean
var  = sum(pow(x-mean,2) for x in sample) / len(sample)  # variance
std  = math.sqrt(var)  # standard deviation

print(f'Standard deviasi adalah: {std}')