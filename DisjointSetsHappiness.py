n, m = map(int, input().split())
a = list(map(int, input().split()))
like = list(map(int, input().split()))
dislike = list(map(int, input().split()))

happiness = 0
for num in a:
    if(like.__contains__(num)):
        happiness += 1
    elif(dislike.__contains__(num)):
        happiness -= 1

print(happiness)