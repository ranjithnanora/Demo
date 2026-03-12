"""
3. Define a list of numbers in the python script file. Write a script to print out all numbers below 10 in the list.
• Test out using 10 different lists
"""

class printBelow10:
    def print_numbers(self, arr: list) -> list:
        result=[]
        for num in arr:
            if num<10:
                result.append(num)
        #print(arr," -> ",result)
        return result
    
    def test_class(self, arr: list, outputs: list) -> None:
        for i in range(len(arr)):
            solution=self.print_numbers(arr[i])
            if solution == outputs[i]:
                print(f"success {i+1}")
            else:
                print(f"Failed {i+1}")


arr = [[12, 4, 15, 8], [7, 10, 2], 
        [20, 30, 40], [15, 11, 19],          
        [1, 2, 3], [4, 5, 6],                
        [9, 10, 11, 12], [8, 9, 10],         
        [5, 15, 25], [2, 12, 22],            
        [10, 20, 30, 5], [9, 11],            
           
]
outputs = [
    [4, 8],[7, 2],
    [],[],
    [1, 2, 3],[4, 5, 6],
    [9],[8, 9],
    [5],[2],
    [5],[9],
]

ob=printBelow10()
ob.test_class(arr, outputs)