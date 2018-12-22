
import numpy as np
import matplotlib.pyplot as plt


#get the data

'''
3
[2670, 2182, 4999, 4950, 3597, 2732, 2228, 2015, 2519, 2166]
4
[1359, 3265, 1991, 1798, 1661, 3740, 4692, 1786, 2357, 3396]
5
[3064, 4982, 2491, 3731, 4574, 2490, 3114, 2092, 2058, 3815]
6
[2491, 3754, 2657, 3554, 3213, 2492, 1475, 3340, 2101, 3349]
7
[2640, 1923, 2911, 2628, 2128, 3078, 4056, 3666, 4418, 1951]
8
[4205, 6141, 2463, 3352, 2524, 2820, 5745, 1451, 4135, 4007]
9
[3590, 1618, 2237, 4268, 3050, 6252, 1709, 1878, 3397, 2435]
10
[5372, 2786, 3443, 1991, 7089, 2288, 2886, 3500, 2777, 3016]
11
[3596, 2254, 3990, 3284, 2357, 2954, 2874, 2175, 1876, 2553]
12
[3400, 2130, 1975, 2345, 2881, 2258, 2183, 6714, 2754, 2442]
13
[2267, 1879, 2541, 5478, 2046, 7145, 3972, 3189, 2009, 2966]

'''
line_3_iter = np.array([2258, 1818, 1931, 8156, 1768, 3388, 2454, 3154, 4399, 3049])
line_4_iter = np.array([4868, 1838, 5499, 3828, 4116, 1962, 2727, 3406, 1980, 3419])
line_6_iter = np.array([3778, 4776, 4650, 2918, 2759, 2680, 4960, 2490, 2702, 1979])
line_8_iter = np.array([4959, 3524, 2328, 1697, 5474, 2783, 3530, 1935, 5608, 4109])
line_10_iter = np.array([2865, 6395, 3662, 4578, 4144, 2263, 2270, 4235, 2462, 2505])
line_12_iter = np.array([4395, 3568, 4175, 4134, 2413, 3080, 3550, 4192, 5921, 2874])
line_14_iter = np.array([1966, 5862, 4124, 2110, 2089, 2359, 3875, 4660, 5638, 2940])
line_16_iter = np.array([3694, 2512, 7149, 3594, 2004, 3238, 2370, 4015, 2348, 4152])
line_18_iter = np.array([2556, 3454, 2070, 2138, 5236, 5798, 4584, 6254, 3819, 2405])
line_20_iter = np.array([3770, 2225, 3995, 2282, 3983, 3592, 5259, 5200, 4544, 4757])


# Calculate the average
iter_3_mean = np.mean(line_3_iter)
iter_4_mean = np.mean(line_4_iter)
iter_6_mean = np.mean(line_6_iter)
iter_8_mean = np.mean(line_8_iter)
iter_10_mean = np.mean(line_10_iter)
iter_12_mean = np.mean(line_12_iter)
iter_14_mean = np.mean(line_14_iter)
iter_16_mean = np.mean(line_16_iter)
iter_18_mean = np.mean(line_18_iter)
iter_20_mean = np.mean(line_20_iter)

# Calculate standard deviation
line_3_iter_std = np.std(line_3_iter)
line_4_iter_std = np.std(line_4_iter)
line_6_iter_std = np.std(line_6_iter)
line_8_iter_std = np.std(line_8_iter)
line_10_iter_std = np.std(line_10_iter)
line_12_iter_std = np.std(line_12_iter)
line_14_iter_std = np.std(line_14_iter)
line_16_iter_std = np.std(line_16_iter)
line_18_iter_std = np.std(line_18_iter)
line_20_iter_std = np.std(line_20_iter)

#Create Arrays for the plot
robot_sizes = ['3','4','6','8','10','12','14','16','18','20']
x_pos = np.arange(len(robot_sizes))

CTEs_iter = [iter_3_mean,iter_4_mean,iter_6_mean,iter_8_mean,iter_10_mean,iter_12_mean,iter_14_mean,
             iter_16_mean,iter_18_mean,iter_20_mean]

error_iter = [line_3_iter_std, line_4_iter_std, line_6_iter_std,line_8_iter_std,line_10_iter_std,
              line_12_iter_std,line_14_iter_std,line_16_iter_std,line_18_iter_std,line_20_iter_std]

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs_iter, yerr=error_iter, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Average # Iterations ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(robot_sizes)
ax.set_title('Number of Iterations VS Robot Size')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('iter_vs_robot_size.png')
plt.show()

