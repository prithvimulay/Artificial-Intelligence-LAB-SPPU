profit =[]
n=int(input("Enter the no.of elements: ")) 
for i in range (n):
    m=int(input("Enter the Profit: ")) 
    profit.append(m)

jobs = []
for i in range (n): 
    b = str(input("Enter the Jobs: "))
    jobs.append(b)

deadline = []
for i in range (n): 
    c=int(input("Enter the Deadline: ")) 
    deadline.append(c)

profitNJobs = list(zip(profit,jobs, deadline))

profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)

slot=[]
for _ in range(len(jobs)):
    slot.append(0)
 
profit = 0
ans = []

for i in range(len(jobs)): 
    ans.append('null')

for i in range(len(jobs)):
    job = profitNJobs[i]
    #check if slot is occupied
    for j in range(job[2], 0, -1):

        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break

print("Jobs scheduled buddy:",ans[1:])
print("PROFIT",profit)
