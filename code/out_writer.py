#
# out_writer.py
#
from solve_forces import force_combine

class out_writer:
    def __init__(self,out_file):
        self.file = open(out_file, "w")

    def write_force(self,system,force_list):
        icnt=0
        for ivforce in force_list:
            icnt += 1
            if(icnt==system):
                self.file.write("Fx,"+str(ivforce.Fx)+"\n")
                self.file.write("Fy,"+str(ivforce.Fy)+"\n")
                break

    def write_all_contents_system(self,system):
        pass
