import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("../data-files/numpyVsOpenCLPerformance.csv")


data.plot(x='arraySize' , y=['NumpyTime','OpenCLTime'],kind='line')

plt.show()