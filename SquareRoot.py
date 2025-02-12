# Calculate the square root of a number.



def Calc_Sqrt(n):
    if n==0 or n ==1:
        return n
    
    s=0 
    e=(n/2)+1
    ans=0

    while s<=e:
        mid=s+(e-s)//2

        if mid*mid==n:
            
            return mid 
             
        elif mid*mid < n :
            ans = mid
            s=mid+1
        else:
            e=mid-1

    return ans


n=int(input("Give the number : "))
sqrt = Calc_Sqrt(n)
print(f"the square root of {n} is : {sqrt}")



# python SquareRoot.py

