#we need to check if a lsit contains duplicate elements or not
#assumptions the lsit may contain repeated elements one after the other or it may not be in one by one
def contains_duplicate(nums):
    #we sort the numbersa beacause the duplicates come togethor
    arr=sorted(nums)
    n=len(arr)
    for i in range(n):
        for j in range(i):
            #we check the number with the next number
            if arr[i]==arr[j]:
                return True
    return False

n=list(map(int,input("enter the list of numbers: ").split()))
print (contains_duplicate(n))