def main():
    res = int(input("Resourse number = "))
    instance = list(map(int, input("Instances = ").strip().split()))[:res]
    allocated = [0]*res
    safe_sequence = []
    data = []
    
    # print(res, instance)
    
    process = int(input("Process number = "))
    
    for i in range(process):
        arr = [0]*(res*3+2)
        arr[0] = 'p'+str(i)
        temp = list(map(int, input(f'{arr[0]}= ').split()))[:res*2]
        arr[1:1+len(temp)] = temp
        ext = 1+len(temp)
        
        
        
        for j in range(res):
            arr[ext+j] = arr[j+1] - arr[res + j + 1]
            allocated[j] += arr[res + j + 1]
        # print(allocated)
        arr[-1] = 'w'
        # print(arr)
        data.append(arr)
    
    for i in range(res):
        allocated[i] = instance[i] - allocated[i]
        
    # print("Allocated = ", allocated)
    
    
    run = True
    sv = 0
    while(run):
        for arr in data:
            # print(arr)
            f = True
            for i in range(res):
                # print(allocated[i], arr[res*2+i+1])
                if(arr[-1]=='w' and allocated[i]<arr[res*2+i+1]):
                    # print('hi')
                    f = False
                    break
            if f == True and arr[-1]!='ok':
                # print('ok============================\n')
                arr[-1] = 'ok'
                safe_sequence.append(arr[0])
                for i in range(res):
                    allocated[i]+=arr[res+i+1]                    
                break
        
        if len(safe_sequence)<=sv or len(safe_sequence) == process:
            run = False
        else: sv+=1
    
    print(safe_sequence)
    
        
        

if __name__=="__main__":
    main()
    
# py bankers.py