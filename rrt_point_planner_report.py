
import numpy as np
import matplotlib.pyplot as plt


#get the data
step_size_change = [4,5,6,7,8,9,10,11,12,13]

'''
4
length = [1562,1186, 1070,1066,1146,1078,1090,1110,1574,1638]
iter = [2604,5774,1194,4615,1456,8464,864,13378,15900,7285]
8
length = [1606,1310,1142,1166,1798,1158,1718,1150,1094,1614]
inter = [2598,13244,5762,2688,20335,12703,2474,2614,5590,2190]
12
length = [1610,1982,1214,1970,1346,1250,1706,1166,1094,1188]
inter = [2608,1738,2717,3745,1994,3214,4638,7700,175,418]
16
length = [1758,1248,1198,1118,1598,1054,1310,1150,1038,1438]
inter = [2726,391,2350,183,841,296,1523,310,232,1091]
20
length= [1134,1454,1114,1020,1114,1354,1294,1614,2034,1274]
inter=[977,586,566,815,1071,343,545,2083,3053,709]
24
length =[1166,1022,1214,1982,1694,1862,1094,1070,1718,1190]
inter = [103,62,858,766,426,1735,128,127,510,549]
28
length=[1134,1414,1694,1162,1162,1246,1078,1694,1190,1106]
inter=[602,462,698,213,749,182,145,738,565,172
32
length=[1038,1710,1550,1518,1006,1102,1134,1550,1774,1230]
inter=[329,591,873,295,318,52,170,246,681,1268]
36
length=[1598,1094,1598,1130,1094,1094,1166,1224,1058,1598]
inter=[261,81,405,335,423,292,451,218,62,429]
40
length=[1214,1254,1200,1094,1054,1320,2014,1494,1094,1374]
inter=[399,638,139,56,113,87,1074,342,121,230]


'''
step_4_iter = np.array([2598,13244,5762,2688,20335,12703,2474,2614,5590,2190])
step_8_iter = np.array([2604,5774,1194,4615,1456,8464,864,13378,15900,7285])
step_12_iter = np.array([2608,1738,2717,3745,1994,3214,4638,7700,175,418])
step_16_iter = np.array([139,909,1469,615,2850,5279,303,1081,371,2050])
step_20_iter = np.array([977,586,566,815,1071,343,545,2083,3053,709])
step_24_iter = np.array([103,62,858,766,426,1735,128,127,510,549])
step_28_iter = np.array([602,462,698,213,749,182,145,738,565,172])
step_32_iter = np.array([329,591,873,295,318,52,170,246,681,1268])
step_36_iter = np.array([261,81,405,335,423,292,451,218,62,429])
step_40_iter = np.array([399,638,139,56,113,87,1074,342,121,230])

step_4_len = np.array([1562,1186, 1070,1066,1146,1078,1090,1110,1574,1638])
step_8_len = np.array([1606,1310,1142,1166,1798,1158,1718,1150,1094,1614])
step_12_len = np.array([1610,1982,1214,1970,1346,1250,1706,1166,1094,1188])
step_16_len = np.array([1758,1248,1198,1118,1598,1054,1310,1150,1038,1438])
step_20_len = np.array([1134,1454,1114,1020,1114,1354,1294,1614,2034,1274])
step_24_len = np.array([1166,1022,1214,1982,1694,1862,1094,1070,1718,1190])
step_28_len = np.array([1134,1414,1694,1162,1162,1246,1078,1694,1190,1106])
step_32_len = np.array([1038,1710,1550,1518,1006,1102,1134,1550,1774,1230])
step_36_len = np.array([1598,1094,1598,1130,1094,1094,1166,1224,1058,1598])
step_40_len = np.array([1214,1254,1200,1094,1054,1320,2014,1494,1094,1374])

# Calculate the average
iter_4_mean = np.mean(step_4_iter)
iter_8_mean = np.mean(step_8_iter)
iter_12_mean = np.mean(step_12_iter)
iter_16_mean = np.mean(step_16_iter)
iter_20_mean = np.mean(step_20_iter)
iter_24_mean = np.mean(step_24_iter)
iter_28_mean = np.mean(step_28_iter)
iter_32_mean = np.mean(step_32_iter)
iter_36_mean = np.mean(step_36_iter)
iter_40_mean = np.mean(step_40_iter)

len_4_mean = np.mean(step_4_len)
len_8_mean = np.mean(step_8_len)
len_12_mean = np.mean(step_12_len)
len_16_mean = np.mean(step_16_len)
len_20_mean = np.mean(step_20_len)
len_24_mean = np.mean(step_24_len)
len_28_mean = np.mean(step_28_len)
len_32_mean = np.mean(step_32_len)
len_36_mean = np.mean(step_36_len)
len_40_mean = np.mean(step_40_len)

# Calculate standard deviation
step_4_iter_std = np.std(step_4_iter)
step_8_iter_std = np.std(step_8_iter)
step_12_iter_std = np.std(step_12_iter)
step_16_iter_std = np.std(step_16_iter)
step_20_iter_std = np.std(step_20_iter)
step_24_iter_std = np.std(step_24_iter)
step_28_iter_std = np.std(step_28_iter)
step_32_iter_std = np.std(step_32_iter)
step_36_iter_std = np.std(step_36_iter)
step_40_iter_std = np.std(step_40_iter)

step_4_len_std = np.std(step_4_len)
step_8_len_std = np.std(step_8_len)
step_12_len_std = np.std(step_12_len)
step_16_len_std = np.std(step_16_len)
step_20_len_std = np.std(step_20_len)
step_24_len_std = np.std(step_24_len)
step_28_len_std = np.std(step_28_len)
step_32_len_std = np.std(step_32_len)
step_36_len_std = np.std(step_36_len)
step_40_len_std = np.std(step_40_len)

#Create Arrays for the plot
step_sizes = ['4','8','12','16','20','24','28','32','36','40']
x_pos = np.arange(len(step_sizes))

CTEs_iter = [iter_4_mean,iter_8_mean,iter_12_mean,iter_16_mean,iter_20_mean,iter_24_mean,iter_28_mean,
             iter_32_mean,iter_36_mean,iter_40_mean]

CTEs_len = [len_4_mean,len_8_mean,len_12_mean,len_16_mean,len_20_mean,len_24_mean,len_28_mean,
            len_32_mean,len_36_mean,len_40_mean]

error_iter = [step_4_iter_std, step_8_iter_std, step_12_iter_std,step_16_iter_std,step_20_iter_std,
              step_24_iter_std,step_28_iter_std,step_32_iter_std,step_36_iter_std,step_40_iter_std]

error_len = [step_4_len_std, step_8_len_std, step_12_len_std,step_16_len_std,step_20_len_std,
             step_24_len_std,step_28_len_std,step_32_len_std,step_36_len_std,step_40_len_std]

# Build the plot
fig, ax = plt.subplots()
#ax.bar(x_pos, CTEs_iter, yerr=error_iter, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.bar(x_pos, CTEs_len, yerr=error_len, align='center', alpha=0.5, ecolor='black', capsize=10)
#ax.set_ylabel('Average # Iterations ($\degree C^{-1}$)')
ax.set_ylabel('Average Path Length ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(step_sizes)
#ax.set_title('Number of Iterations VS Step Size')
ax.set_title('Path Length VS Step Size')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
#plt.savefig('iter_vs_step.png')
plt.savefig('len_vs_step.png')
plt.show()

