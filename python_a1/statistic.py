"""
4. Define a list of numbers. Print out fundamental statistical values for these numbers:
• Mean
• Median
• Mode
• Standard deviation
Note: Do not use any math libraries to do this assignment

"""

class statistic:
    def __init__(self, arr):
        self.N=len(arr)
        self.arr=arr
    def mean(self) -> float:
        return sum(self.arr)/self.N
    
    def meadian(self) -> float:
        N=self.N
        temp=self.arr.copy()
        temp.sort()
        if(N%2==0):
            return (temp[N//2]+temp[(N//2)-1])/2
        else:
            return temp[(N-1)//2]
    
    def mode(self) -> int:
        freq=dict()
        max_freq_ele=0
        max_freq=0
        for num in self.arr:
            if num not in freq:
                freq[num]=0
            freq[num]+=1
            if(freq[num] > max_freq):
                max_freq=freq[num]
                max_freq_ele=num
        
        return max_freq_ele
    
    def standard_deviation(self):
        mean=self.mean()
        total=0
        for num in self.arr:
            total+=(num-mean)**2
        
        return (total/self.N)**0.5 

arr=list(map(int, input("array: ").split(" ")))
print(arr)
st=statistic(arr)
print(st.mean())
print(st.meadian())
print(st.mode())
print(st.standard_deviation())

