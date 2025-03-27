import csv
filename=input()
movies={}

with open (filename,'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        showtime,title,rating=row[0],row[1],row[2]
        if title not in movies:
            movies[title]={"rating":rating,"showtimes":[]}
        movies[title]["showtimes"].append(showtime)

for title,data in movies.items():
    formatted_title=title[:44].ljust(44)
    formatted_rating=data["rating"].rjust(5)
    formatted_shows=" ".join(data["showtimes"])
    print(f'{formatted_title} | {formatted_rating} | {formatted_shows}')
