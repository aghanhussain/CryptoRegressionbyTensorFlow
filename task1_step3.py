from task1_Step1 import price
import datetime
import matplotlib.pyplot as plt

x=[0]
y=[0]
fig = plt.gcf()
fig.show()
fig.canvas.draw()
plt.ylim([0, 20000])
i=0
while(True):
    data = price('BTC')
    i+=1
    x.append(i)
    y.append(data['USD'])
    plt.title("BTC Vs USD. Last updated at: "+str(datetime.datetime))
    plt.plot(x,y)


    fig.canvas.draw()
    plt.pause(1000)


