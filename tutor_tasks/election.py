election = dict()
for i in range(int(input())):
    k, v = input().split()
    election[k] = election.get(k, 0) + int(v)
for k in election.keys():
    print(k, election[k])

