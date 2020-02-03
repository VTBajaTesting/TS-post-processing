import pandas
from matplotlib import pyplot as plt
def do_the_thing(path):
    data = pandas.read_csv(path)
    time = data.time.values
    lp1 = data.LP1.values
    lp2 = data.LP2.values
    lp3 = data.LP3.values
    lp4 = data.LP4.values
    igyroX = data.gyroX.values
    igyroY = data.gyroY.values
    igyroZ = data.gyroZ.values
    iaccelX = data.accelX.values
    iaccelY = data.accelY.values
    iaccelZ = data.accelZ.values
    temp = data.temp.values
    lp_m = -415.83
    lp_b = 4094.8
    lp1 = (lp1 - lp_b)/lp_m
    lp2 = (lp2 - lp_b) / lp_m
    lp3 = (lp3 - lp_b) / lp_m
    lp4 = (lp4 - lp_b) / lp_m
    plt.plot(time, lp1, label = 'LP1')
    plt.plot(time, lp2, label = 'LP2')
    plt.plot(time, lp3, label = 'LP3')
    plt.plot(time, lp4, label = 'LP4')
    plt.xlabel('Time(ms)')
    plt.ylabel('LP value(in)')
    plt.legend()
    plt.show()

do_the_thing('TS1atTime0.csv')