def travel(start, end, link=[]):
    link = link + [start]
    if start == end:
        return link
    if start not in vertices:
        return None
    for node in vertices[start]:
        if node not in link:
            new = travel(node, end, link)
            if new: 
                return new
    return None

vertices = dict()
start = input().split(" ")
for _ in range(0, int(start[1])):
    query = input().split(" ")
    if(int(query[0]) == 0):
        #for vertices == int query 1 add int query 2
        if int(query[1]) in vertices:
            vertices[int(query[1])].append(int(query[2]))
        else:
            vertices[int(query[1])] = [int(query[2])]
            #for vertices == int query 2 add int query 1
        if int(query[2]) in vertices:
            vertices[int(query[2])].append(int(query[1]))
        else:
            vertices[int(query[2])] = [int(query[1])]
    elif(int(query[0]) == 1):
            #check the dictionnary if the key exists and one of its value is in the other key using travel
        if travel(int(query[1]), int(query[2])) != None:
            print(1)
        else:
            print(0)