import time
nums = [10,14,19,26,27,31,33,35,42,44]
target = 19
print(f"Target : {target}")
high = len(nums) - 1
print(f"high : {high}")

low = 0
print(f"low : {low}")

status = "True"

#mid_new = take_mid(low, high)
#print(f"{mid_new}")
mid_new = 0

while status == "True":
    def take_mid(low, high):
        mid_new  = (high - low)//2
        return mid_new
    if target > nums[mid_new]:
        print(f"low inside while {low}")
        low = mid_new + 1
        mid_new = take_mid(low, high)
        time.sleep(5)
    
    elif target < nums[mid_new]:
        print(f"low inside else{low}")
        high = mid_new - 1
        mid_new = take_mid(low, high)
        print("coming here")
        time.sleep(5)
    else:
        status = "False"
    
    
    


        
        
