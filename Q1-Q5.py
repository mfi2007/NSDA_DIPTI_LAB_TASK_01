# Step 1: Take 2 lists, list1 and list2, from the user, each with 8 items
list1 = []
list2 = []

print("Enter 8 items for List1:")
for i in range(8):
    item = int(input())
    list1.append(item)

print("Enter 8 items for List2:")
for i in range(8):
    item = int(input())
    list2.append(item)


# Step 2: Connect the two lists in newList[]
newlist = []

for item in list1:
    newlist.append(item)

for item in list2:
    newlist.append(item)


# Step 3: Remove the last 2 items from newlist
if len(newlist) >= 2:
    newlist = newlist[:-2]
else:
    print("Warning: The combined list is not long enough to remove 2 items.")
    

# Step 4: Separate the newlist[] into Evenlist[] and Oddlist[]
Evenlist = []
Oddlist = []

for item in newlist:
    if item % 2 == 0:
        Evenlist.append(item)
    else:
        Oddlist.append(item)


# Step 5: Find the minimum numbers from newlist[], Evenlist[], and Oddlist[]
min_newlist = newlist[0]  
min_Evenlist = Evenlist[0] if Evenlist else None  
min_Oddlist = Oddlist[0] if Oddlist else None  

for item in newlist:
    if item < min_newlist:
        min_newlist = item

for item in Evenlist:
    if item < min_Evenlist:
        min_Evenlist = item

for item in Oddlist:
    if item < min_Oddlist:
        min_Oddlist = item


# Display the results
print("New List:", newlist)
print("Even List:", Evenlist)
print("Odd List:", Oddlist)
print("Minimum number in newlist:", min_newlist)
print("Minimum number in Evenlist:", min_Evenlist)
print("Minimum number in Oddlist:", min_Oddlist)