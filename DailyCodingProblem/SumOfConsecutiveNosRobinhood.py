#Given a number n, return the number of lists of consecutive positive integers that sum up to n.

#For example, for n = 9, you should return 3 since the lists are: [2, 3, 4], [4, 5], and [9]. Can you do it in linear time?

n = 9
start = 1
end = 1
sum = 1
Nsums = 0
while start <= n//2:
    print(sum, start, end)
    if end > n:
        break
    if sum < n:
        end +=1
        sum = sum + end
    elif sum > n:
        #sum += end
        sum -= start
        start += 1
    elif sum == n:
        Nsums += 1
        print("Success - sum:{}, start:{}, end:{}".format(sum,start,end))
        sum -= start
        start += 1
Nsums += 1 # For self - to include the condition 9
print(Nsums)