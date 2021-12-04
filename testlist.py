list = {'Y': ['C', 'M'], 'C': ['Y', 'M'], 'M': ['C', 'Y', 'H'], 'F': ['A'], 'A': ['F', 'D'], 'D': ['A', 'H'], 'H': ['M', 'D']}

def findH(list):
  if not list:
    return None
  for item in list:
    if item == "H":
      return True
    elif item != "Fp":
      findH(item)
    else:
        return

print(findH(list))
# print(list['Y'])