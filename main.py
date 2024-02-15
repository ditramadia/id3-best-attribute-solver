# Import library
import sys
import math

# Import data
import data.data as data

# Import classes
import classes.Dataset as Dataset

if __name__ == "__main__":
  
  # Prepare dataset
  dataset = Dataset.Dataset(data.data)
  dataset.info()
  for feature in dataset.getFeatures():
    feature.info(dataset.getTarget().getDomain())
  dataset.getTarget().info()

  # Get entropy
  entropyS = dataset.getEntropy()
  print(f'Entropy(S): {entropyS}')
  print()

  # Get information gain of every attributes
  ig = []
  for i in range(len(dataset.getFeatures())):
    curr_ig = dataset.getFeatures()[i].gain(entropyS, dataset.getNRows())
    ig.append(curr_ig)
    print(f'Gain(S, {dataset.getFeatures()[i].getName()}) = {curr_ig}')
  print()

  # Get best attribute
  best_attr = ig.index(max(ig))
  print(f"Best attribute: {dataset.getFeatures()[best_attr].getName()} with IG of {max(ig)}")

  # Terminate
  sys.exit(0)