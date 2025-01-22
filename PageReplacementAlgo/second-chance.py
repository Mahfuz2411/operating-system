class SCPageReplacement:
    def __init__(self, frame, references):
        self.number_of_frame = frame
        self.references = references
        self.frames = [[0]*3]*frame
        self.number_of_hit = 0
        self.number_of_miss = 0
        
    
    def _helperToFindVictim(self):
        self.frames = sorted(self.frames, key=lambda x: x[2])
    
    def replacePage(self):
        for x in self.references:
            pass

        


arr = [...]*3
arr[0] = [3,1 ,3]
arr[1] = [2,2 ,1]
arr[2] = [1,3 ,2]

arr = sorted(arr, key=lambda x: x[2])
print(arr)