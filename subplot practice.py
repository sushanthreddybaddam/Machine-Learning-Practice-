# importing numpy and the pyplot package of matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Data for sales made by the company across three regions over the years 2012 to 2015
years = np.array(['2012', '2013', '2014', '2015'])
sales_Africa = np.array([127187.27, 144480.70, 229068.79, 283036.44])
sales_Asia_Pacific = np.array([713658.22, 863983.97, 1092231.65, 1372784.40])
sales_Europe = np.array([540750.63, 717611.40, 848670.24, 1180303.95])

# Plotting the trend of sales in African region over the 4 years

plt.plot(years,sales_Africa)
# Check the array names before plotting to avoid error
plt.show()


# Plotting the trend of sales in all three regions over the 4 years using subplots
fig,ax=plt.subplots()
africa,=ax.plot(years,sales_Africa)
africa.set_label("Africa")
aspac,=ax.plot(years,sales_Asia_Pacific)
aspac.set_label("Asia Pacific")
europe,=ax.plot(years,sales_Europe)
europe.set_label("Europe")
plt.legend()
plt.show()


# Plotting three charts with a shared y-axis
fig,ax=plt.subplots(ncols=3 ,sharey=True)
africa,=ax[0].plot(years,sales_Africa)
africa.set_label("Africa")
aspac,=ax[1].plot(years,sales_Asia_Pacific)
aspac.set_label("Asia Pacific")
europe,=ax[2].plot(years,sales_Europe)
europe.set_label("Europe")
plt.legend()
plt.show()