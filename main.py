import re
# Online Python - IDE, Editor, Compiler, Interpreter
PID = r"PID:\s\w[A-Z0-9_-]{0,15}"
SN = r"SN:\s\w[A-Z0-9_-]{0,11}"
PID_Values = []
SN_Values = []

with open("cisco.txt", "r") as file:
    for line in file:
        pids = re.findall(PID, line, re.IGNORECASE)
        sns = re.findall(SN, line, re.IGNORECASE)
        PID_Values.extend(pids)
        SN_Values.extend(sns)
       
        
#remove leading/trailing whitespace
PID_Values = [pid.replace(" ", "") for pid in PID_Values]
SN_Values = [sn.replace(" ", "") for sn in SN_Values]


for pid, sn in zip(PID_Values, SN_Values):
        print(f"{pid} {sn}")
 
