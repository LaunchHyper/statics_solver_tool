#
# solve_forces.py
#
import math
#---
from in_reader import in_reader

class force:
    #class general methods / values
    TOLERANCE = 0.00001

    def add(F1,F2):
        x = (F1.x + F2.x)/2.0
        y = (F1.y + F2.y)/2.0
        try:
            #only for numerical Fx,Fy
            Fx = F1.Fx + F2.Fx
            Fy = F1.Fy + F2.Fy
            deg = math.tan(Fy/Fx)
            val = math.sqrt( math.pow(Fx,2)+math.pow(Fy,2) )
        except:
            #check variable Fx
            if(F1.Fx!=0 and F2.Fx!=0): Fx = str(F1.Fx)+"+"+str(F2.Fx)
            elif(F1.Fx!=0): Fx = str(F1.Fx)
            elif(F2.Fx!=0): Fx = str(F2.Fx)
            else: Fx = 0
            #check variable Fy
            if(F1.Fy!=0 and F2.Fy!=0): Fy = str(F1.Fy)+"+"+str(F2.Fy)
            elif(F1.Fy!=0): Fy = str(F1.Fy)
            elif(F2.Fy!=0): Fy = str(F2.Fy)
            else: Fy = 0
            #TODO: below..
            deg = 0
            val = 0
        #---
        F3 = force(x=x,y=y)
        F3.Fx = Fx
        F3.Fy = Fy
        return F3

    #class instance methods
    def __init__(self,val=0,x=0,y=0,deg=0):
        self.x = x
        self.y = y
        self.val = val
        self.deg = deg
        #---
        deg_val_c = math.cos(math.pi/180.0*self.deg)
        if(math.fabs(deg_val_c) <= force.TOLERANCE): 
            deg_val_c=0
        #endif
        deg_val_s = math.sin(math.pi/180.0*self.deg)
        if(math.fabs(deg_val_s) <= force.TOLERANCE): 
            deg_val_s=0
        #endif
        try:
            self.Fx = self.val * deg_val_c
            self.Fy = self.val * deg_val_s
        except:
            if(deg_val_c!=0): 
                self.Fx = str(self.val)
                if(deg_val_c!=1): self.Fx = str(deg_val_c) + self.Fx
            else:
                self.Fx = 0
            #endif
            if(deg_val_s!=0): 
                self.Fy = str(self.val)
                if(deg_val_s!=1): self.Fy = str(deg_val_s) + self.Fy
            else:
                self.Fy = 0
            #endif

class force_combine:
    def __init__(self,in_file):
        self.in_forces = []
        self.out_forces = []
        try:
            extract = in_reader(in_file)
            self.icnt=0
            for sys in extract.systems:
                self.icnt += 1
                part = sys[0]
                x1 = float(sys[1])
                y1 = float(sys[2])
                x2 = float(sys[3])
                y2 = float(sys[4])
                for i in sys[5]:
                    para = i[0]
                    if(para=="force"):
                        val = i[1]
                        x = float(i[2])
                        y = float(i[3])
                        deg = float(i[4])
                        self.in_forces.append( (self.icnt,force(val,x,y,deg)) )
                    #end force check
            #endloop
        except:
            print("File not correct: "+str(in_file))

    def combine_forces(self):
        self.ivforce_list=[]
        for icnt in range(self.icnt):
            self.ivforce_list.append(force())
        for iforce in self.in_forces:
            icnt = iforce[0]    #what system
            i1force = iforce[1] #specific force in system
            i2force = self.ivforce_list[icnt-1]
            #---
            result = force.add(i1force,i2force)
            self.ivforce_list[icnt-1] = result
    
    def debug_printout(self):
        icnt=0
        for ivforce in self.ivforce_list:
            icnt += 1
            print("System,"+str(icnt))
            print("Fx,"+str(ivforce.Fx))
            print("Fy,"+str(ivforce.Fy))

#################################################
# TEST
#######
if __name__ == "__main__":
    print("\nTEST 1")
    file1 = "./test_in_reader_1.txt"
    test1 = force_combine(file1)
    test1.combine_forces()
    test1.debug_printout()
    #---
    print("\nTEST 2")
    file2 = "./test_in_reader_2.txt"
    test2 = force_combine(file2)
    test2.combine_forces()
    test2.debug_printout()
    #---
    print("\nDONE testing...")
