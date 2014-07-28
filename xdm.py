#!/usr/bin/env python2

import sys
import numpy as np
from matplotlib import pyplot as plt

class AnalogData:
  def __init__(self, maxLen):
    self.ay = np.array([0.0])
    self.maxLen = maxLen

  def addToBuf(self, buf, val):
    if buf.size < self.maxLen:
      buf = np.hstack((buf, val))
    else:
      buf = buf[1:]
      buf = np.hstack((buf, val))

  def add(self, data):
    self.addToBuf(self.ay, data)
    if self.ay.size < self.maxLen:
      self.ay = np.hstack((self.ay, data))
    else:
      self.ay = self.ay[1:]
      self.ay = np.hstack((self.ay, data))

class AnalogPlot: 
  def __init__(self, analogData):
    plt.ion() 
    self.aline, = plt.plot(range(analogData.ay.size), analogData.ay)
    plt.axis([0, analogData.maxLen, 0, 100])

  def update(self, analogData):
    self.aline.set_xdata(range(analogData.ay.size))
    self.aline.set_ydata(analogData.ay)
    plt.draw()

def main():
  created_vars = False
  while True:
    line = sys.stdin.readline()
    if not line:
      break
    data = [float(val) for val in line.split()]
    if not created_vars:
      analogPlots = []
      analogDatas = []
      for i in range(len(data)):
        plt.figure(i)
        analogDatas.append(AnalogData(100))
        analogPlots.append(AnalogPlot(analogDatas[i]))
      created_vars = True
    for i in range(len(data)):
      plt.figure(i)
      analogDatas[i].add(data[i])
      analogPlots[i].update(analogDatas[i])

if __name__ == '__main__':
  main()
