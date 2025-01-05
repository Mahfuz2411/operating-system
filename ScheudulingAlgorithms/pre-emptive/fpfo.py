class SJTF:
    def __init__(self):
        self.arr = []
        self.n = 0
    
    def user_input(self):
        try:
            self.n = int(input("Enter the number of processes: "))
            
            
            print("Enter A.T. and B.T. and Priority")
            for i in range(self.n):
                brr = [0]*9
                brr[0] = 'P'+str(i+1)
                
                brr[1], brr[2], brr[3] = list(map(int, input(f"{brr[0]}: ").split()))[:3]
                
                brr[7] = -1
                brr[8] = i
                self.arr.append(brr)
                
        except Exception as e:
            print(f"! Error: {e}")
            self.user_input()
            
    def custom_sort(self, i, ct):
        for j in range(i, len(self.arr)):
            for k in range(j+1, len(self.arr)):
                if self.arr[k][1]<=ct and self.arr[k][3] < self.arr[j][3]:
                    self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
            
    def sjtf(self):
        self.arr = sorted(self.arr, key=lambda x: x[1])
        ct = 0
        i = 0
        
        cry = {}
        
        for brr in self.arr:
            cry[brr[0]] = brr[2]
        
        while 1:
            self.custom_sort(i, ct)
            brr = self.arr[i]
            if ct < brr[1]:
                ct = brr[1]
            if brr[7]==-1 and ct>=brr[1]: brr[7] = ct - brr[1]
            brr[2] -= 1
            ct += 1
            if brr[2] == 0:
                brr[4] = ct
                brr[5] = brr[4]-brr[1]
                brr[6] = brr[5]-cry[brr[0]]
                
                i += 1
            
            
            if i >= len(self.arr):
                break
        
        for brr in self.arr:
            brr[2] = cry[brr[0]]
        
        self.arr = sorted(self.arr, key=lambda x: x[8])    
    
    
    def print_process(self):
        for x in ['p', 'at', 'bt','pr', 'ct', 'tt', 'wt', 'rt']:
            print(f"{x:>4}", end='')
        print()
        
        for _ in range (8):
            print(" ---", end='')
        print()
        
        for brr in self.arr:
            for crr in brr[:-1]:
                print(f"{crr:>4}", end='')
            print()


def main():
    ob = SJTF()
    ob.user_input()
    ob.sjtf()
    ob.print_process()


if __name__ == "__main__":
    main()