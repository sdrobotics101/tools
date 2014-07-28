#!/usr/bin/env python2

import sys
import numpy as np
from matplotlib import pyplot as plt

class AnalogData:
  def __init__(self, maxLen):
    self.ay = np.zeros((1,6))
    self.maxLen = maxLen

  def add(self, data):
    if self.ay.shape[0] < self.maxLen:
      self.ay = np.vstack((self.ay, data))
    else:
      self.ay = self.ay[1:]
      self.ay = np.vstack((self.ay, data))

class AnalogPlot: 
  def __init__(self, analogData):
    plt.ion()
    self.alines = []
    for i in range(analogData.ay.shape[1]):
      self.alines.append(plt.plot(range(analogData.ay.shape[0]), analogData.ay[:,i])[0])
    plt.axis([0, analogData.maxLen, 0, 600])

  def update(self, analogData):
    for i in range(analogData.ay.shape[1]):
      self.alines[i].set_xdata(range(analogData.ay.shape[0]))
      self.alines[i].set_ydata(analogData.ay[:,i])
    plt.draw()

def main():
  created_vars = False
  while True:
    line = sys.stdin.readline()
    if not line:
      break
    data = np.array([float(val) for val in line.split()])
    data += np.array([50, 150, 250, 350, 450, 550])
    #if not created_vars:
    #  analogPlots = []
    #  analogDatas = []
    #  for i in range(len(data)):
    #    plt.figure(i)
    #    analogDatas.append(AnalogData(100))
    #    analogPlots.append(AnalogPlot(analogDatas[i]))
    #  created_vars = True
    #for i in range(len(data)):
    #  plt.figure(i)
    #  analogDatas[i].add(data[i])
    #  analogPlots[i].update(analogDatas[i])
    
    if not created_vars:
      analogData = AnalogData(300)
      analogPlot = AnalogPlot(analogData)
      created_vars = True
    analogData.add(data)
    analogPlot.update(analogData)

if __name__ == '__main__':
  main()
