import argparse
import csv


##taking i the files and city from the cmd
parser = argparse.ArgumentParser(description='Big Data Analysis of a specified city.')
parser.add_argument('user_file', type=str, help='Enter the File name yelp_business.csv')
parser.add_argument('city', type=str, help='Enter the City name like Toronto')
args = parser.parse_args()

##setting up variable to get the numbers
numOfBus = 0
avgStars = 0.0
avgNumOfReviews = 0.0
numOfRestaurants = 0
avgStarsRestaurants = 0.0
avgNumOfReviewsBus = 0

with open(args.user_file, 'r', encoding='utf8') as file_csv:
    f_reader = csv.reader(file_csv)

    next(f_reader)

    for line in f_reader:
        if args.city in line[4]:
            numOfBus += 1
            avgStars += float(line[9])
            avgNumOfReviews += int(line[10])
            if 'Restaurant' in line[12] or 'restaurant' in line[12]: ##checking if the category is restraunt or not
                numOfRestaurants += 1                 ##updating variables
                avgStarsRestaurants += float(line[9]) ## in these
                avgNumOfReviewsBus += int(line[10])   ## 3 blocks

##printing all the values 
print("For city: " + args.city)

print("numOfBus: " + str(numOfBus))

stars = float(avgStars / float(numOfBus))
stars_avg = round(stars, 1)
print("avgStars: " + str(stars_avg))

print("numOfRestaurants: " + str(numOfRestaurants))

r_stars = float(avgStarsRestaurants / float(numOfRestaurants))
r_stars_avg = round(r_stars, 1)
print("avgStarsRestaurants: " + str(r_stars_avg))

review_avg = float(avgNumOfReviews/numOfBus)
review_avg_short = round(review_avg, 2)
print("avgNumOfReviews: " + str(review_avg_short))

r_review_avg = float(avgNumOfReviewsBus/numOfRestaurants)
r_review_avg_short = round(r_review_avg, 2)
print("avgNumOfReviewsBus: " + str(r_review_avg_short))
