# text = "Python Programming"
# print(text[6::-1])

# text = "  ##Hello World##  "
# new_text=text.strip().strip("##").split()
# print(new_text)

# tup = (1, 2, [3, 4])
# x,y,z=tup
# z[0]=9
# tup =(x,y,z)
# print(tup)

# prices = [10, 20, 30]
# for i in range(len(prices)):
#     prices[i]= prices[i]-(0.10*prices[i])
#
# print(prices)

# with open("eve2.csv", "r") as file:
#     print(file.read())


# def function_divide(num1: int=1, num2: int=1) -> float:
#     """
#     It divides two numbers
#     :param num1:
#     :param num2:
#     :return:
#     """
#     return num1 / num2
#
# print(function_divide())

# def func(*numbers, optype="mean")->int|None:
#     if optype == "mean":
#         return sum(numbers) / len(numbers)
#     elif optype == "mode":
#         mp=dict()
#         max_freq=0
#         max_freq_num=-1
#         for num in numbers:
#             mp[num]=mp.get(num,0)+1
#             if mp[num]>max_freq:
#                 max_freq_num=num
#                 max_freq=mp[num]
#
#         return max_freq_num
#     return None
#
# print(func(2,3,4,5,6, optype="mean"))
# print(func( 1,2,3,4,5,6))
# print(func(2,3,3,4,5,6,optype="mode"))

# arr1=[1,2,3,4,5,6,7]
# arr2=[2,3,4,5]
# result=[]
# result=[key*val for key,val in zip(arr1,arr2)]

# for i in range(min(len(arr1),len(arr2))):
#     result.append(arr1[i]*arr2[i])
# print(result)
# mp={2:5,3:5,4:5,5:5,6:5,7:5,8:5,9:5}
# new_dict={}
# new_dict={new_dict for key,value in mp.items()}
# print(new_dict)

# matrix1=[[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# matrix2=[[5,3,5],
#          [10,6,5],
#          [20,9,5]]
# result=[[0 for _ in range(3)] for _ in range(3)]
# for i in range(len(matrix1)):
#     for row in range(len(matrix1[0])):
#         for col in range(len(matrix2)):
#             result[i][row]+= matrix1[i][col]* matrix2[col][row]
# print(result)

#[[85, 42, 30], [190, 96, 75], [295, 150, 120]]

# matrix=[[1, 2, 3, 4, 5],
#         [16, 17, 18, 19, 6],
#         [15, 24, 25, 20, 7],
#         [14, 23, 22, 21, 8],
#         [13, 12, 11, 10, 9]]
#
# traversal=[]
# row_start=0
# col_start=0
# row_end=len(matrix)
# col_end=len(matrix[0])
# i,j=0,0
# while col_start<col_end and row_start<row_end:
#     i = row_start
#     j = col_start
#     while j<col_end-1:
#         traversal.append(matrix[i][j])
#         j+=1
#
#     while i<row_end-1:
#         i+=1
#         traversal.append(matrix[i][j])
#
#     while j>col_start:
#         j-=1
#         traversal.append(matrix[i][j])
#
#     while i>row_start+1:
#         i-=1
#         traversal.append(matrix[i][j])
#
#     row_start += 1
#     col_start += 1
#     row_end -= 1
#     col_end -= 1
#
# traversal.append(matrix[i][j])
# print(traversal)

# matrix=[[5,3,4],
#         [10,6,8],
#         [15,9,12]]
#
# # matrix transpose
# for i in range(len(matrix)):
#     for j in range(i+1,len(matrix[0])):
#         print(i,j)
#         print(matrix[i][j], "<->", matrix[j][i])
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for arr in matrix:
#     arr.reverse()
# print(matrix)

# arr=["eat","tea","tan","ate","nat","bat"]
# mp={}
# for val in arr:
#     a=list(val)
#     a.sort()
#     key=str(a)
#     if key not in mp:
#         mp[key]=[]
#     mp[key].append(val)
# for value in mp.values():
#     print(value)





