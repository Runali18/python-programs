bus=[["a","a","a"],
    ["a" ,"a","a"],
    ["a" ,"a","a"],
    ["a" ,"a","a"]]
    
for i in range(4):
    print(bus[i])

print("*******please select your set*******:")
row=int(input("Enter your row Eumber:"))
seat=int(input("Enter your seat Number:"))
print("_________________________________")

if bus[row-1][seat-1]=="a":
    bus[row-1][seat-1] ="r"
    print("your seat is resurved:")

else:
    print("seat is already resurved:")
    
for i in range(4):
        print(bus[i]) 


