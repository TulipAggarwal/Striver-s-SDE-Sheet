class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        result = []
        intervals.sort()
        for interval in intervals:
            
            #In the if statement we check if the result list is empty i.e adding the first element or by checking if next interval's beginning time is greater than the previous interval's end time
            if result == [] or result [-1][1] < interval [0]:
                #result[last thing we add to it][the end time of that element]
                result.append(interval)
            
            #If the above above condition is not true then we can say that we have an interlap in the intervals
            else:
        
            #In the following code line we take the previously added interval to our result and then make the end time of that interval as the max of the end time of first or second interval 
                result[-1][1] = max(result[-1][1], interval[1])
        return result
