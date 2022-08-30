import pandas as pd
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv('StudentsPerformance.csv')
mathScore = df['math score'].tolist()

mean = st.mean(mathScore)
median = st.median(mathScore)
mode = st.median(mathScore)
print("The mean of the given data is ",mean)
print("The median of the given data is ",median)
print("The mode of the given data is ",mode)

sD = st.stdev(mathScore)
print("The Standard Deviation of the given data is ",sD)

Mfst,mfEnd = mean-sD, mean+sD
Msst, msEnd = mean-(2*sD),mean+(2*sD) 
Mtst, mtEnd = mean-(3*sD), mean+(3*sD)


Mldwfstd = [re for re  in mathScore if re > Mfst and re < mfEnd]

Mldwsstd = [re for re  in mathScore if re > Msst and re < msEnd]

Mldwtstd = [re for re  in mathScore if re > Mtst and re < mtEnd]
print("{}% of data for height lies within 1 standard deviation".format(len(Mldwfstd)*100.0/len(mathScore)))
print("{}% of data for height lies within 2 standard deviation".format(len(Mldwsstd)*100.0/len(mathScore)))
print("{}% of data for height lies within 3 standard deviation".format(len(Mldwtstd)*100.0/len(mathScore)))

fig = ff.create_distplot([mathScore], ['Math Score'], show_hist=False)
fig.show()