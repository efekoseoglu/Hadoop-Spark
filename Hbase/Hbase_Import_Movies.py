from starbase import Connection

c = Connection("127.0.0.1","8000")
ratings = c.table("ratings")

if (ratings.exists()):
    print("Dropping existing ratings table \n")
    ratings.drop()

ratings.create("rating")

print("Parsing the mk-100k ratings data... \n")
ratingFile = open("C:\\Users\\efe\\Desktop\\ml-100k\\u.data", "r")

batch = ratings.batch()

# Everytime with the updating u.data, ends up with a unique userID alongside rating family, inside rating family for each every unique movieID there will be a rating
for line in ratingFile:
    (userID,movieID,rating,timestamp) = line.split()
    batch.update(userID, {"rating": {movieID: rating}})

ratingFile.close()

print("Committing rating data to HBase via REST service \n")
batch.commit(finalize=True)

print("Get back ratings for some users...\n")
print("Ratings for used ID 1: \n")
print(ratings.fetch("1"))
print("Ratings for user ID 33: \n")
print(ratings.fetch("33"))

ratings.drop()
