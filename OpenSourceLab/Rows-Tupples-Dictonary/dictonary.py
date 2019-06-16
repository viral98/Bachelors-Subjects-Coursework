
dict = {'Name': 'Viral', 'Age': 19}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


print ("Length : %d" % len (dict))


print ("Equivalent String : %s" % str (dict))


dict2 = dict.copy()
print ("New Dictionary : ",dict2)


print ("Value of keys: %s" %  dict.keys())
print ("Values : ",  list(dict.values()))
print (dict)


print("After updating..")
dict['Name'] = "Milond"
dict['Age'] = 99
print ("Value of keys: %s" %  dict.keys())
print ("Values : ",  list(dict.values()))
print (dict)


print ("Value : %s" %  dict.get('Age'))
print ("Value : %s" %  dict.get('Education'))
