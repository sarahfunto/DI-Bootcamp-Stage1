mylist = ["apple", "banana", "cherry", 12, 1.09]
print (mylist)
print (mylist [-1])

mylist[1] = "pineapple"  # PendingDeprecationWarning

print (mylist)

newlist = ["apple" , "banana" , "cherry", [1, 4, 7]]

print (newlist)

inside_list = newlist[3]
print ("insidelist")
print (inside_list)
print (newlist[3])  
print("------------")
print ("newlist[3][1]")
print (newlist[3][1])
print ("inside_list[1]")
print ("inside_list[2]")
print(inside_list[2])



grid = [ [1, 2, 3],                 
        [4, 5, 6],  
        [7, 8, 9] 
        ]
print(grid[0][0])

mylist.append("orange")
print(mylist)

mylist.remove("apple")
print(mylist)   

duplicate = [ "first", "second", "first", "third"]
duplicate.remove("first")
print(duplicate)    

first = [1, 2, 3, 4 ]
second = [5, 6, 7, 8]

first.extend(second)

print(first)    
print (first + second)
print ("hello" + "3" + "world")

print (first * 3)

print (len(first)) 
print (sum(first))
print (max(first))
print (min(first))

print (max ([1,2, 3] + [4, 5, 6]+ [7, 8, 9]))

tup = (1, 2, 3, "happy birthday")
print (tup)
#tup [0] = 42
print("tup[2]")
print (tup[2])
print ("--------")
a, b, c, d, e = tup
print (a)
print (b)
print (c) 
print (d)
print (e)

#a, b = tup
a, *b = tup
print(a)
print(b)

#sets
s= set ([1, 2, 3, 4, 4, 4, 5, 5])
print (s)   
s.add(10)
print (s)
s.add (2)
print (s)

#loop
li =  [12, 15, 264, 234, 12, 577# TypeError: 'tuple' object does not support item assignment