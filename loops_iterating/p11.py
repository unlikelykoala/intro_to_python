# Problem 11

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

length1 = len(my_list)
index1 = 0

while True:
    if index1 < length1:
        length2 = len(my_list[index1])
        index2 = 0
        while True:
            if index2 < length2:
                if my_list[index1][index2] % 2 == 0:
                    print(my_list[index1][index2])
                index2 += 1
            else: break
        
        index1 += 1                  
    
    else: break
