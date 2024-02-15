import math

class Feature:
  def __init__(self, data_row, is_target):
    self.__name = data_row[0]
    self.__is_target = is_target
    self.__attr_row = data_row[1:]
    self.__domain = self.__getDomain(data_row)
    self.__domain_freq = self.__getFreq(data_row)
    self.__domain_freq_by_class = None

  def getName(self) -> str:
    return self.__name
  
  def getDomain(self) -> list:
    return self.__domain

  def getDomainFreq(self) -> list:
    return self.__domain_freq
  
  def getAttrRow(self) -> list:
    return self.__attr_row
  
  def setDomainFreqByClass(self, target_domain, target_row) -> None:
    domain_freq_by_class = []
    for i in range(0, len(self.__domain)):
      temp = []
      for j in range(0, len(target_domain)):
        temp.append(0)
      domain_freq_by_class.append(temp)

    for i in range(0, len(self.__domain)):
      for j in range(0, len(self.__attr_row)):
        if self.__domain[i] == self.__attr_row[j]:
          for k in range(0, len(target_domain)):
            if target_row[j] == target_domain[k]:
              domain_freq_by_class[i][k] += 1

    self.__domain_freq_by_class = domain_freq_by_class

  def __getDomain(self, data_row) -> list:
    domain = []
    for i in range(1, len(data_row)):
      if data_row[i] not in domain:
        domain.append(data_row[i])
    return domain
  
  def __getFreq(self, data_row) -> list:
    freq = []
    for i in range(0, len(self.__domain)):
      freq.append(0)

    for i in range(0, len(self.__domain)):
      for j in range(1, len(data_row)):
        if data_row[j] == self.__domain[i]:
          freq[i] += 1
    
    return freq
  
  def info(self, target_class = []):
    print(f'Feature name: {self.__name}', end=' ')
    if self.__is_target:
      print(f'(Target)')
    else:
      print()
    # print(f'Feature row:', end=' ')
    # print(self.__attr_row)
    print(f'Domain:', end=' ')
    print(self.__domain)
    print(f'Domain frequency:', end=' ')
    print(self.__domain_freq)

    print()

    if not self.__is_target:
      for i in range(len(self.__domain)):
        self.domainInfo(i, target_class)

  def domainInfo(self, i, target_class) -> None:
    print(f'\tDomain name: {self.__domain[i]}')
    print(f'\tTarget class:', end=' ')
    print(target_class)
    print(f'\tValue Frequency:', end=' ')
    print(self.__domain_freq_by_class[i])

    print()

  def __domainEntropy(self, idx) -> float:
    entropy = 0

    for i in range(0, len(self.__domain_freq_by_class[0])):
      p = self.__domain_freq_by_class[idx][i]/self.__domain_freq[idx]
      # print(f'p = {p}')
      if p > 0:
        entropy += -p * math.log2(p)
    
    return entropy

  def gain(self, entropyS, n_rows) -> int:
    value = 0
    for i in range(0, len(self.__domain)):
      value += (self.__domain_freq[i]/n_rows) * self.__domainEntropy(i)

    return entropyS - value