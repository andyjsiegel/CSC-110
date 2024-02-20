# Programming Problem 21
def differences(set_1, set_2):
    for item in set_1.intersection(set_2): 
        set_1.discard(item)
        set_2.discard(item)
    
    return len(set_1) + len(set_2)


print( differences({1, 2, 3}, {2, 3, 4, 5}) ) # 3
print( differences({'john', 'mark', 'paul'}, {'john', 'mark'}) ) # 1