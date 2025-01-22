def process(arr: list, head):
        ans = 0
        for i in range(len(arr)):
            if not i: ans += abs(head-arr[i])
            else: ans += abs(arr[i]-arr[i-1]);
        
        print(ans)
    

process(list(map(int, input("List: ").split())), int(input("Head: ")))