class FIFO:
    def __init__(self):
        self.arr = []
        self.n = 0
        
    def user_input(self):
        try:
            self.n = int(input("Enter the number of processes: "))
            
            
            print("Enter A.T. and B.T.")
            for i in range(self.n):
                brr = [0]*8
                brr[0] = 'P'+str(i+1)
                
                brr[1], brr[2] = list(map(int, input(f"{brr[0]}: ").split()))
                
                brr[7] = i
                self.arr.append(brr)
                
        except Exception as e:
            print(f"! Error: {e}")
            self.user_input()
    
    def fifo(self):
        self.arr = sorted(self.arr, key=lambda x: x[1])
        ct = 0
        
        for brr in self.arr:
            if ct < brr[1]:
                ct = brr[1]
            brr[3] = ct+brr[2]
            ct = brr[3]
            brr[4] = brr[3]-brr[1]
            brr[5] = brr[4]-brr[2]
            brr[6] = brr[5]
            
        
        self.arr = sorted(self.arr, key=lambda x: x[7])
    
    def print_process(self):
        for x in ['p', 'at', 'bt', 'ct', 'tt', 'wt', 'rt']:
            print(f"{x:>4}", end='')
        print()
        
        for _ in range (7):
            print(" ---", end='')
        print()
        
        for brr in self.arr:
            for crr in brr[:-1]:
                print(f"{crr:>4}", end='')
            print()
        
            
            
def main():
    fifo = FIFO()
    fifo.user_input()
    fifo.fifo()
    fifo.print_process()


if __name__ == '__main__':
    main()