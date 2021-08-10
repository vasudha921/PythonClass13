import pandas as pd
import statistics
import csv

df = pd.read_csv("properties.csv")
weightlist = df["Weight(Pounds)"].to_list()
weightmean = statistics.mean(weightlist)
weightmedian = statistics.median(weightlist)
weightmode = statistics.mode(weightlist)
weightstddeviation = statistics.stdev(weightlist)

print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weightmean, weightmedian, weightmode))

weight_1st_stddev_start, weight_1st_stddev_end = weightmean-weightstddeviation, weightmean+weightstddeviation
weight_2nd_stddev_start, weight_2nd_stddev_end = weightmean - (2 * weightstddeviation), weightmean + (2 * weightstddeviation)
weight_3rd_stddev_start, weight_3rd_stddev_end = weightmean - (3 * weightstddeviation), weightmean + (3 * weightstddeviation)

weight_list_of_data_within_1_std_deviation = [result for result in weightlist if result > weight_1st_stddev_start and result < weight_1st_stddev_end]
weight_list_of_data_within_2_std_deviation = [result for result in weightlist if result > weight_2nd_stddev_start and result < weight_2nd_stddev_end]
weight_list_of_data_within_3_std_deviation = [result for result in weightlist if result > weight_3rd_stddev_start and result < weight_3rd_stddev_end]


print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weightlist)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weightlist)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weightlist)))