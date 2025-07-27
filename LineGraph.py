# importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Sales data across months
months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
sales = np.array([241268.56, 184837.36, 263100.77, 242771.86, 288401.05, 401814.06, 258705.68, 456619.94, 481157.24, 422766.63, 555279.03, 503143.69])

# plotting a line chart
plt.plot(months,sales)
# adding title to the chart
plt.title("Monthly Sales")
# labeling the axes
plt.xlabel("Months")
plt.ylabel("Sales")
# rotating the tick values of x-axis

# displating the created plot
plt.show()