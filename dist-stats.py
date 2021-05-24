import argparse
import csv
import matplotlib.pyplot as plt

## creating arparse to take files from commandline
parser = argparse.ArgumentParser(description='Big Data Analysis of a specified city.')
parser.add_argument('user_file', type=str, help='Enter the File name yelp_business.csv')
parser.add_argument('city', type=str, help='Enter the City name like Toronto')
args = parser.parse_args()

##creating dictonaries for holding data
holder = {'Filipino': [0, 0, 0], 'American (Traditional)': [0, 0, 0], 'Cuban': [0, 0, 0], 'Caribbean': [0, 0, 0],
          'Hawaiian': [0, 0, 0], 'African': [0, 0, 0], 'Spanish': [0, 0, 0], 'Indian': [0, 0, 0], 'Korean': [0, 0, 0],
          'French': [0, 0, 0], 'Vietnamese': [0, 0, 0], 'Greek': [0, 0, 0], 'Chinese': [0, 0, 0],
          'Thai': [0, 0, 0], 'Mediterranean': [0, 0, 0], 'American (New)': [0, 0, 0],
          'Mexican': [0, 0, 0], 'Italian': [0, 0, 0], 'Japanese': [0, 0, 0]}

holder_2 = {'Filipino': [0, 0, 0], 'American (Traditional)': [0, 0, 0], 'Cuban': [0, 0, 0], 'Caribbean': [0, 0, 0],
            'Hawaiian': [0, 0, 0], 'African': [0, 0, 0], 'Spanish': [0, 0, 0], 'Indian': [0, 0, 0], 'Korean': [0, 0, 0],
            'French': [0, 0, 0], 'Vietnamese': [0, 0, 0], 'Greek': [0, 0, 0], 'Chinese': [0, 0, 0],
            'Thai': [0, 0, 0], 'Mediterranean': [0, 0, 0], 'American (New)': [0, 0, 0],
            'Mexican': [0, 0, 0], 'Italian': [0, 0, 0], 'Japanese': [0, 0, 0]}

with open(args.user_file, 'r', encoding='utf8') as file_csv:
    f_reader = csv.reader(file_csv)

    next(f_reader)

    for line in f_reader:
        if args.city in line[4] and (
                'Restaurant' in line[12] or 'restaurant' in line[12] ##checking if the category has restaurant in it
        ):
            cuisine = line[12].split(';')
            for c in cuisine:
                for k, v in holder.items():
                    c.strip()
                    if c == k: ##checking if cuisine exists in keys
                        v[0] += 1 ##incrmenting the frequency of that cusine
                    if c in holder_2:
                        hold1 = holder_2.get(c)     ## updating
                        hold1[0] += int(line[10])   ## data
                        hold1[1] += float(line[9])  ## in these
                        hold1[2] += 1               ## 4 blocks 
                        holder_2.update({c: hold1}) ##updating 

numb_food = {k: v for k, v in sorted(holder.items(), key=lambda v1: v1[1], reverse=True)} ##sorting dictonaries
numb_food_2 = {k: v for k, v in sorted(holder_2.items(), key=lambda v1: v1[1], reverse=True)} ##sorting dictionaries

name = []
freq = []

for k, v in numb_food.items():
    name.append(k)
    freq.append(v[0])

print("\n category:#restaurants ----------------------------------------------------------------------------")

for k, v in numb_food.items():
    print(k + " : " + str(v[0]))

print("\n category:#reviews:avg_stars ----------------------------------------------------------------------------")

for k, v in numb_food_2.items():
    print(k + " : " + str(v[0]) + " : " + str(round((v[1] / v[2]), 1)))

print("\n restaurantCategoryDist :#restaurants "
      "----------------------------------------------------------------------------")

##ploting the graph
fig = plt.figure()

ax: object = fig.add_axes([0, 0, 1, 1])
ax.bar(name, freq)
ax.set_title('restaurantCategoryDist :#restaurants')
ax.set_xlabel('Category')
ax.set_ylabel("Number of Restaurants")
plt.show()
