normal_set = {"a", "b","c"}
normal_set.add("d")
print("Normal Set")
print(normal_set)


frozen_set = frozenset(["e", "f", "g", "c"])
print("Frozen Set")
print(frozen_set)


##Operations on sets
print("Adding h to normal set")
normal_set.add("h")
print(normal_set)


print("Performing union between normal set and frozen set")
print (normal_set.union(frozen_set))


print("Performing intersection between normal set and frozen set")
print (normal_set.intersection(frozen_set))
print (frozen_set.intersection(normal_set))


print("Performing difference between normal set and frozen set")
print (normal_set.difference(frozen_set))
print (frozen_set.difference(normal_set))


print("Performing symmetric difference between normal set and frozen set")
print (normal_set.symmetric_difference(frozen_set))
print (frozen_set.symmetric_difference(normal_set))
if normal_set.isdisjoint(frozen_set):
    print("The sets have nothing in common\n")