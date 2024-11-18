import math as mt

class Fifo:
    def __init__(self, frame: int) -> None:
        self.arr        : list[int]         = []
        self.frame      : int               = frame
        self.hitCount   : int               = 0
    
    def push(self, n: int) -> str:
        if n in self.arr:
            print("[", self.arr, ' H ]')
            self.hitCount += 1
            return [n, 'H']

        if len(self.arr)>=self.frame:
            self.arr.pop(0)
        
        self.arr.append(n)
        # print(self.arr)
        print("[", self.arr,' M ]')
        return [n, 'M']

        


def main() -> None:
    ob = Fifo(3)
    arr: list[int] = list(map(int, input().split()))
    
    # brr: list[str] = []
    brr =[]
    for d in arr:
        brr.append(ob.push(d))
    
    print("================================")
    print(brr)
    
    __gcd : int = mt.gcd(ob.hitCount, len(arr)-ob.hitCount)
    
    print()
    print("Total hits: ", ob.hitCount)
    print("Total misses: ", len(arr) - ob.hitCount)
    print("Hit & Miss Ratio (H:M) = ",  int(ob.hitCount/__gcd), ":", int((len(arr)-ob.hitCount)/__gcd))
    print("Hit Percentage = ",  "{:.2f}".format((ob.hitCount*100)/len(arr)), "%")
    


if __name__ == "__main__":
    main()