import sys

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []
    for you in range(T):
        z=list(io.readline().strip().split())
        v=int(io.readline().strip())
        lt=[]        
        for gig in range(4):
            x =io.readline().strip()
            lt.append(x)
        tc.append([v,lt,z])  
    # Return all the test cases parsed
    return tc

# Function to solve a single test case
def solve_testcase(t):
    po=''
    dx=4
    num=t[0]
    tip=[]
    for op in t[1]:
        df=set()
        for o in range(len(op)-num+1):
            df.add(op[o:o+num])
        tip.append(df)
    x1,x2,x3,x4=tip[0],tip[1],tip[2],tip[3]
    for po in x1.intersection(x2,x3,x4):
        break    
    lo=[]
    for ag in t[1]:
        lo.append(ag.find(po))
    s=''
    for co in lo:
        s+=' '+str(co)
            
    return s

# Solve 
def solve(inp, output):
    for i, t in enumerate(parse_testcases(inp)):
        y="Case #"+str(i+1)+":" +str(solve_testcase(t))+'\n'
        output.write(y)
    output.close()

if __name__ == "__main__":
    fin = open('input.txt','r')
    fout = open('output.txt','w')
    solve(fin, fout)
