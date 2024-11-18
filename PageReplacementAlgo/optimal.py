import math as mt

class Optimal:
    def __init__(self, frame: int, ref: list[int]) -> None:
        self.arr         : list[int]          = []
        self.brr         : list[int]          = []
        self.ref         : list[int]          = ref
        # self.mp          : dict[int, bool]    = {}
        self.idx         : int                = 0
        self.frame       : int                = frame
        self.hitCount    : int                = 0
    
    def push(self, n: int) -> str:
        self.idx += 1
        if n in self.arr:
            print("[", self.arr, ' H ]')
            self.hitCount += 1
            return [n, 'H']


        replace_idx = -1
        if len(self.arr)>=self.frame:
            # temp : dict[int, int] = {}
            # cnt : int = 1
            temp: list[int] = []
            # for d in self.arr:
            #     temp[d] = 0
            for i in range(self.idx, len(self.ref)):
                # print("23 ====> ", self.ref[i])
                if self.ref[i] in self.arr and self.ref[i] not in temp: 
                    temp.append(self.ref[i])
                    # cnt += 1
                    # temp[self.ref[i]] = (temp[self.ref[i]]+1) if (self.ref[i] in temp) else 1
            for d in self.arr:
                if d not in temp:
                    temp.append(d)
                
                # if cnt  == self.frame:
                #     break
            
            
            
            # print("====>", temp)
            # min : list[int] = [-1]*2
            # for d in temp:
            #     if min[1] == -1 or min[1]>=temp[d]:
            #         print('=====> ', n, min[1], temp[d])
            #         min[0] = d
            #         min[1] = temp[d]
            #     elif min[1]>=temp[d]:
            #         min[0] = d
            #         min[1] = temp[d]
            
            
            
            # print(n, min[0])
            # ext: int = self.arr.pop(0)
            # self.mp[ext] = 0
            # self.arr.remove(min[0])
            replace_idx = self.arr.index(temp.pop())
            self.arr[replace_idx] = n
            # print("Replace idx: ", replace_idx)
        
        else:
            # self.arr[replace_idx] = n
            self.arr.append(n)
            # self.mp[n] = self.idx - 1
            # print(self.arr)
        print("[", self.arr,' M ]')
        return [n, 'M']
    
    def runOptimal(self) -> None:
        for d in self.ref:
        	self.brr.append(self.push(d))






def main() -> None:
    arr: list[int] = list(map(int, input().split()))
    ob = Optimal(3, arr)
    ob.runOptimal()
    
    
    # brr: list[str] = []
    # brr =[]
    # for d in arr:
    #     brr.append(ob.push(d))
    
    print("================================")
    print(ob.brr)
    # print(brr)
    
    _gcd : int = mt.gcd(ob.hitCount, len(arr)-ob.hitCount)
    
    print()
    print("Total hits: ", ob.hitCount)
    print("Total misses: ", len(arr) - ob.hitCount)
    print("Hit & Miss Ratio (H:M) = ",  int(ob.hitCount/_gcd), ":", int((len(arr)-ob.hitCount)/_gcd))
    print("Hit Percentage = ",  "{:.2f}".format((ob.hitCount*100)/len(arr)), "%")
    


if __name__ == "__main__":
    main()
    
    # 2 3 2 1 5 2 4 5 3 2 5 2