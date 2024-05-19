#
# in_reader.py
#
import csv

class in_reader:
    def __init__(self,in_file):
        f = open(in_file,"r")
        reader = csv.reader(f)
        #---init save data
        self.systems=[]
        #---extract all data
        flag=True
        while(flag):
            iline = reader.__next__()
            #check if new system
            if( iline[0]=="System"):
                #yes, now add part
                iline = reader.__next__()
                part = iline[0]
                x1 = float(iline[1])
                y1 = float(iline[2])
                x2 = float(iline[3])
                y2 = float(iline[4])
                self.systems.append( (part,x1,y1,x2,y2,[]) )
                #loop through forces, momentums
                while(flag):
                    iline = reader.__next__()
                    if( iline[0]=="-1"):
                        flag=False
                    else:
                        para = iline[0]
                        val = iline[1]
                        x = float(iline[2])
                        y = float(iline[3])
                        deg = float(iline[4])
                        self.systems[-1][5].append((para,val,x,y,deg))
                #endloop2
                flag=True #reset for upper level..
            #end of file
            else:
                flag=False
        #endloop1
    
    def debug_printout(self):
        icnt=1
        for sys in self.systems:
            print("System,"+str(icnt))
            icnt += 1
            part = sys[0]
            x1 = float(sys[1])
            y1 = float(sys[2])
            x2 = float(sys[3])
            y2 = float(sys[4])
            print(str(part)+","+str(x1)+","+str(y1)+","+str(x2)+","+str(y2))
            for i in sys[5]:
                para = i[0]
                val = i[1]
                x = float(i[2])
                y = float(i[3])
                deg = float(i[4])
                print(str(para)+","+str(val)+","+str(x)+","+str(y)+","+str(deg))

#################################################
# TEST
#######
if __name__ == "__main__":
    print("\nTEST 1")
    file1 = "./test_in_reader_1.txt"
    test1 = in_reader(file1)
    test1.debug_printout()
    #---
    print("\nTEST 2")
    file2 = "./test_in_reader_2.txt"
    test2 = in_reader(file2)
    test2.debug_printout()
    #---
    print("\nDONE testing...")
