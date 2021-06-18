#Basic Ad-Hoc Report from CMS Medicaid Enrollment Data

from matplotlib import pyplot as plt
import pandas as pd
#dataframes
enrollment_df = pd.read_csv('data/vtenrollment1.csv')
enrollment_df['Report Date'] = pd.to_datetime(enrollment_df['Report Date'], infer_datetime_format=True)
enrollment_df.sort_values(['Report Date'], axis=0, ascending=True, inplace=True)
vtenrollment_df = enrollment_df[(enrollment_df['State Abbreviation'] == 'VT')]
sample_enrollment = vtenrollment_df.sample(10)
sum_null=vtenrollment_df.isnull().sum()
#plot enrollment participation over time
plt.scatter(vtenrollment_df['Report Date'], vtenrollment_df['Total Medicaid and CHIP Enrollment'])
plt.xlabel('Report Date(Year)')
plt.ylabel('Total Enrollment #')
plt.title('Total Medicaid and CHIP Enrollment')
plt.show()






