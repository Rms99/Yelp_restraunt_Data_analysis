import csv
import sys

## The code below increases the csv size precisely according to our need. 
## resource - https://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

## The code below opens the file
user_file = sys.argv[1]
with open(user_file, 'r', encoding='utf8') as file_csv:
    f_reader = csv.reader(file_csv, delimiter=' ')
    
    n = {} ## declaring the dictonary that hold's the nodes
    edges = 0 ## declaring edge counter

    for line in f_reader:
        edges+=1
        vertices = []
        vertices.append(line[0])
        vertices.append(line[1])
        for vs in vertices:
            if vs in n: ## if node already in n increment value by 1
                n[vs] +=1
            else:
                n[vs] = 1 ## else add the node to key with value 1

num_nodes = len(n)
avg_n = (2.0*float(edges/num_nodes)) ## finding the average node
avg_nodes = round(avg_n, 2)

print('#nodes:|' + str(num_nodes) + '| #edges:|' + str(edges) +'|') 

outfile = open('nodes.txt', 'w')

n_nodes = {k: v for k, v in sorted(n.items(), key=lambda v1: v1[1], reverse=True)} ##sorting the nodes according to num of edges

for k,v in n_nodes.items():
    outfile.write(k + ":" + str(v) +"\n") ##printing nodes into nodes.txt

print('avgNodeDegree:' + str(avg_nodes))
print('nodeDegreeDist is in a txt file called nodes.txt')