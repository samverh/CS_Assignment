import pandas as pd
import matplotlib.pyplot as plt

# load data
data_file = "istherecorrelation.csv"
data = pd.read_csv(data_file, delimiter=";")

# create correlation plot
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(data["WO [x1000]"], data["NL Beer consumption [x1000 hectoliter]"])
plt.title("Beer consumption of WO students in the Netherlands (from 2006 to 2018)")
plt.xlabel("WO students (x1000)")
plt.ylabel("Beer consumption (x1000 hectoliter)")
plt.show()

# save file
fig.savefig('plot.png', dpi = 300)
