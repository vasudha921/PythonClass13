import pandas as pd
import statistics
import csv

df = pd.read_csv("properties.csv")
heightlist = df["Height(Inches)"].to_list()
heightmean = statistics.mean(heightlist)
heightmedian = statistics.median(heightlist)
heightmode = statistics.mode(heightlist)
heightstddeviation = statistics.stdev(heightlist)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(heightmean, heightmedian, heightmode))

height_1st_stddev_start, height_1st_stddev_end = heightmean-heightstddeviation, heightmean+heightstddeviation
height_2nd_stddev_start, height_2nd_stddev_end = heightmean - (2 * heightstddeviation), heightmean + (2 * heightstddeviation)
height_3rd_stddev_start, height_3rd_stddev_end = heightmean - (3 * heightstddeviation), heightmean + (3 * heightstddeviation)

height_list_of_data_within_1_std_deviation = [result for result in heightlist if result > height_1st_stddev_start and result < height_1st_stddev_end]
height_list_of_data_within_2_std_deviation = [result for result in heightlist if result > height_2nd_stddev_start and result < height_2nd_stddev_end]
height_list_of_data_within_3_std_deviation = [result for result in heightlist if result > height_3rd_stddev_start and result < height_3rd_stddev_end]


print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(heightlist)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(heightlist)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(heightlist)))