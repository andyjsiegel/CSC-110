import random

def pick_winner(list):
    return list[random.randint(0, len(list)-1)]

def pick_winners(names):
  winners = []
  for i in range(len(names)-2): # note how i here just controls how many iterations
    index = random.randint(0, len(names) - 1)
    winners.append(names[index])
    names.pop(index)
  return winners

print(pick_winner(["Peter", "Griffin", "Jonesy", "Michael"]))
if __name__ == "__main__":
  random.seed(42)
  winners = pick_winners(["Peter", "Joan", "Mary", "June"])
  print(winners)

