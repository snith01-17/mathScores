import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
mathList = df["math score"].to_list()

mean = statistics.mean(mathList)
median = statistics.median(mathList)
mode = statistics.mode(mathList)
sd = statistics.stdev(mathList)

first_sdStart, first_sdEnd = mean-sd, mean+sd
second_sdStart, second_sdEnd = mean-(2*sd), mean+(2*sd)
third_sdStart, third_sdEnd = mean-(3*sd), mean+(3*sd)

fig = ff.create_distplot([df["math score"].tolist()], ["Math Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_sdStart,first_sdStart], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[first_sdEnd,first_sdEnd], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[second_sdStart,second_sdStart], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[second_sdEnd,second_sdEnd], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[third_sdStart,third_sdStart], y=[0,0.17], mode="lines", name="Standard Deviation 3"))
fig.add_trace(go.Scatter(x=[third_sdEnd,third_sdEnd], y=[0,0.17], mode="lines", name="Standard Deviation 3"))

fig.show()

listOfDataWithinfirstStandardDeviation = [result for result in mathList if result > first_sdStart and result < first_sdEnd]
listOfDataWithinSecondStandardDeviation = [result for result in mathList if result > second_sdStart and result < second_sdEnd]
listOfDataWithinThirdStandardDeviation = [result for result in mathList if result > third_sdStart and result < third_sdEnd]


print("Mean of data is: {}".format(mean))
print("Median of data is: {}".format(median))
print("Mode of data is: {}".format(mode))
print("Standard deviation of data is: {}".format(sd))

print("{}% of data lies within first standard deviation".format(len(listOfDataWithinfirstStandardDeviation)*100.0/len(mathList)))
print("{}% of data lies within second standard deviation".format(len(listOfDataWithinSecondStandardDeviation)*100.0/len(mathList)))
print("{}% of data lies within third standard deviation".format(len(listOfDataWithinThirdStandardDeviation)*100.0/len(mathList)))