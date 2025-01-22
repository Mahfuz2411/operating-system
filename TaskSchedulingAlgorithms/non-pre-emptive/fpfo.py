# first priority first out
class FPFO:
    def __init__(self):
        self.arr = []
        self.n = 0
    
    def user_input(self):
        try:
            self.n = int(input("Enter the number of processes: "))
            
            
            print("Enter A.T. and B.T.")
            for i in range(self.n):
                brr = [0]*9
                brr[0] = 'P'+str(i+1)
                
                brr[1], brr[2], brr[3] = list(map(int, input(f"{brr[0]}: ").split()))[:3]
                
                brr[8] = i
                self.arr.append(brr)
                
        except Exception as e:
            print(f"! Error: {e}")
            self.user_input()
            
    def _custom_sort(self, i, ct):
        for j in range(i, len(self.arr)):
            for k in range(j+1, len(self.arr)):
                if self.arr[k][1]<=ct and self.arr[k][3] < self.arr[j][3]:
                    self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
            
    def fpfo(self):
        self.arr = sorted(self.arr, key=lambda x: x[1])
        ct = 0
        
        for i in range(len(self.arr)):
            self._custom_sort(i, ct)
            brr = self.arr[i]
            if ct < brr[1]:
                ct = brr[1]
            brr[4] = ct+brr[2]
            ct = brr[4]
            brr[5] = brr[4]-brr[1]
            brr[6] = brr[5]-brr[2]
            brr[7] = brr[6]
            
        
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
    ob = FPFO()
    ob.user_input()
    ob.fpfo()
    ob.print_process()


if __name__ == "__main__":
    main()