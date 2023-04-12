class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):

            #Creating a temporary array and assuming zeroes to the end and beginning of it
            temp = [0] + res[-1] + [0]

            #The empty row for creating the new row
            row = []
            
            #Building the next row with a length of pervious row + 1
            for j in range(len(res[-1])+1):

                #Keeping track of 2 pointers j and j+1
                row.append(temp[j]+temp[j+1])
            
            res.append(row)
            
        return res
