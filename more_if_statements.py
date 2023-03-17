movies_watched = {"The Matrix", "aftersun", "persona", "Her"}
user_movie = input("enter something you have watched recently: ")

if user_movie in movies_watched:
    print(f"you've watched {user_movie} before!")
else:
    movies_watched.add(user_movie)
    print("new movie added to your repertoire!")
    print(movies_watched)