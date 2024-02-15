import math

import classes.Feature as Feature

class Dataset:
  def __init__(self, data):
    self.__target = self.__getTarget(data)
    self.__n_class = len(self.__target.getDomain())

    self.__features = self.__getFeatures(data)
    self.__n_rows = sum(self.__target.getDomainFreq())

    self.__entropyS = self.__entropy(self.__n_rows, self.__target.getDomainFreq())

  def getFeatures(self) -> list:
    return self.__features
  
  def getTarget(self) -> list:
    return self.__target
  
  def getNRows(self) -> list:
    return self.__n_rows
  
  def getEntropy(self) -> int:
    return self.__entropyS

  def __getFeatures(self, data) -> list:
    features = []
    for i in range(0, len(data)):
      if i != len(data) - 1:
        newFeature = Feature.Feature(data[i], False)
        newFeature.setDomainFreqByClass(self.__target.getDomain(), data[-1][1:])
        features.append(newFeature)
    return features
  
  def __getTarget(self, data) -> Feature.Feature:
    return Feature.Feature(data[-1], True)
  
  def __entropy(self, n_rows, target_domains_freq) -> float:
    entropy = 0

    for i in range(0, len(target_domains_freq)):
      p = target_domains_freq[i]/n_rows
      if (p != 1):
        entropy += -p * math.log2(p)
    
    return entropy
  
  def info(self) -> None:
    print(f"Number of non target attributes: {len(self.__features)}")
    print(f'Target attribute: {self.__target.getName()}')
    print(f'Number of rows: {self.__n_rows}')
    print(f'Number of classes: {self.__n_class}')
    print()
  
  def findBestAttribute(self) -> Feature.Feature:
    best = max()
    return 
