import datetime
list = []
set = set()
dictionary = {}

Start = datetime.datetime.now()
for iCount in range(0,50000) :
    list.append("Customer" + str(iCount))
End = datetime.datetime.now()
print("List add: " + str((End-Start).microseconds))

Start = datetime.datetime.now()
for iCount in range(0,50000) :
    set.add("Customer" + str(iCount))
End = datetime.datetime.now()
print("Set add: " + str((End - Start).microseconds))

Start = datetime.datetime.now()
for iCount in range(0, 50000) :
    dictionary[iCount] = "Customer" + str(iCount)
End = datetime.datetime.now()
print("Dictionary add: " + str((End - Start).microseconds))

print("\n")

Start = datetime.datetime.now()
if "Customer25000" in list : 
    print("Found")
End = datetime.datetime.now()
print("List Find: " + str((End-Start).microseconds))

print("\n")

Start = datetime.datetime.now()
for sName in set:
    if sName == "Customer25000" :
        print("Found")
End = datetime.datetime.now()
print("Set find: " + str((End - Start).microseconds))

print("\n")

Start = datetime.datetime.now()
if 25000 in dictionary:
        print("Found")
End = datetime.datetime.now()
print("Dictioanary find: " + str((End - Start).microseconds))

print("\n")

Start = datetime.datetime.now()
for iCount in range(0, len(list)):
        list.pop(0)
End = datetime.datetime.now()
print("List delete: " + str((End - Start).microseconds))

print("\n")

Start = datetime.datetime.now()
for iCount in range(0, len(set)):
        set.pop()
End = datetime.datetime.now()
print("Set delete: " + str((End - Start).microseconds))

print("\n")

Start = datetime.datetime.now()
for iCount in range(0, len(dictionary)):
        dictionary.pop(iCount)
End = datetime.datetime.now()
print("Dictionary delete: " + str((End - Start).microseconds)) 