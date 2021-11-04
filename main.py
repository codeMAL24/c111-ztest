import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random as r

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = s.mean(data)
std = s.stdev(data)

print(f"This is the mean of the marks: {mean}")
print(f"This is the std of the marks: {std}")

# fig = ff.create_distplot([data],["MATHS SCORE"],show_hist = False)
# fig.show()

def rsom(counter):
    dataSet = []
    for i in range(0,counter):
        ri = r.randint(0,len(data)-1)
        value = data[ri]
        dataSet.append(value)
    Smean = s.mean(dataSet)
    return Smean 

meanList = []
for i in range(0,1000):
    sm = rsom(100)
    meanList.append(sm)

mean = s.mean(meanList)
std = s.stdev(meanList)

print(f"This is the mean of the sample distribution: {mean}")
print(f"This is the std of the sample distribution: {std}")

fig = ff.create_distplot([meanList],["Student MATH marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
# fig.show()

#---------------------------------------------------------------------------------------------

std1s,std1e = mean - std, mean + std
std2s,std2e = mean - (2*std), mean + (2*std)
std3s,std3e = mean - (3*std), mean + (3*std)


# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()



meanS1 = s.mean(data)

fig = ff.create_distplot([meanList],["Student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS1,meanS1],y = [0,0.17],mode = "lines",name = "mean of 1st intervention(ipad)"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
#fig.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()


meanS2 = s.mean(data)

fig = ff.create_distplot([meanList],["Student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS2,meanS2],y = [0,0.17],mode = "lines",name = "mean of 2nd intervention(xtra classes))"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
fig.add_trace(go.Scatter(x = [std2e,std2e],y = [0,0.17],mode = "lines",name = "2nd std end"))
#fig.show()

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()


meanS3 = s.mean(data)

fig = ff.create_distplot([meanList],["Student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS3,meanS3],y = [0,0.17],mode = "lines",name = "mean of 3rd intervention(funSheet)"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
fig.add_trace(go.Scatter(x = [std2e,std2e],y = [0,0.17],mode = "lines",name = "2nd std end"))
fig.add_trace(go.Scatter(x = [std3e,std3e],y = [0,0.17],mode = "lines",name = "3rd std end"))

#fig.show()


#finding the z score using the formula
zscore1 = (meanS1 - mean)/std
print(f"The zscore of the 1st intervention is {zscore1}")

zscore2 = (meanS2 - mean)/std
print(f"The zscore of the 2nd intervention is {zscore2}")

zscore3 = (meanS3 - mean)/std
print(f"The zscore of the 3rd intervention is {zscore3}")

#The zscore of the 3rd intervention(funsheets) was more than 2 therefore it had the most impact 

