# Movie Recommendation System

# Dataset: Movie -> Genre
movies = {
    # ==========================
    # Hollywood Movies
    # ==========================
    "avatar": "Avatar (2009) - A science fiction adventure directed by James Cameron.",
    "avatar 2": "Avatar: The Way of Water (2022) - The sequel to Avatar.",
    "avengers": "The Avengers (2012) - Marvel superheroes unite to save Earth.",
    "avengers endgame": "Avengers: Endgame (2019) - One of Marvel's biggest blockbuster movies.",
    "iron man": "Iron Man (2008) - The first movie in the Marvel Cinematic Universe.",
    "spiderman": "Spider-Man: No Way Home (2021) - A multiverse superhero adventure.",
    "batman": "The Batman (2022) - A detective-style superhero film.",
    "joker": "Joker (2019) - An Oscar-winning psychological drama.",
    "oppenheimer": "Oppenheimer (2023) - A biographical film directed by Christopher Nolan.",
    "interstellar": "Interstellar (2014) - A science fiction masterpiece by Christopher Nolan.",
    "inception": "Inception (2010) - A mind-bending science fiction thriller.",
    "titanic": "Titanic (1997) - A romantic disaster film directed by James Cameron.",
    "the dark knight": "The Dark Knight (2008) - One of the greatest superhero films ever made.",
    "john wick": "John Wick (2014) - A stylish action movie starring Keanu Reeves.",
    "mission impossible": "Mission: Impossible - Action spy film series starring Tom Cruise.",
    "fast and furious": "Fast & Furious - Popular action racing franchise.",
    "jurassic park": "Jurassic Park (1993) - A dinosaur adventure directed by Steven Spielberg.",
    "harry potter": "Harry Potter - Fantasy adventure series based on J.K. Rowling's novels.",
    "lord of the rings": "The Lord of the Rings - Epic fantasy trilogy.",
    "pirates of the caribbean": "Pirates of the Caribbean - Adventure fantasy series starring Johnny Depp.",

    # ==========================
    # Bollywood Movies
    # ==========================
    "3 idiots": "3 Idiots (2009) - One of India's greatest comedy-drama films.",
    "dangal": "Dangal (2016) - A sports drama inspired by a true story.",
    "pk": "PK (2014) - A comedy-drama starring Aamir Khan.",
    "lagaan": "Lagaan (2001) - Oscar-nominated Indian sports drama.",
    "sholay": "Sholay (1975) - One of the greatest Indian films ever made.",
    "bahubali": "Baahubali: The Beginning (2015) - Epic Indian fantasy action film.",
    "bahubali 2": "Baahubali 2: The Conclusion (2017) - One of India's highest-grossing films.",
    "rrr": "RRR (2022) - Oscar-winning Indian action drama.",
    "kgf": "KGF: Chapter 1 (2018) - Kannada action blockbuster.",
    "kgf 2": "KGF: Chapter 2 (2022) - Sequel to KGF.",
    "pushpa": "Pushpa: The Rise (2021) - Telugu action drama.",
    "pushpa 2": "Pushpa 2: The Rule (2024) - Sequel to Pushpa.",
    "drishyam": "Drishyam (2015) - A suspense thriller.",
    "drishyam 2": "Drishyam 2 (2022) - Sequel to Drishyam.",
    "war": "War (2019) - Bollywood action thriller.",
    "pathaan": "Pathaan (2023) - Spy action film starring Shah Rukh Khan.",
    "jawan": "Jawan (2023) - Action thriller starring Shah Rukh Khan.",
    "animal": "Animal (2023) - Action drama starring Ranbir Kapoor.",
    "stree": "Stree (2018) - Horror comedy film.",
    "chhichhore": "Chhichhore (2019) - Inspirational comedy-drama.",

    # ==========================
    # Anime Movies
    # ==========================
    "your name": "Your Name (2016) - One of the greatest anime romance films.",
    "spirited away": "Spirited Away (2001) - Oscar-winning Studio Ghibli film.",
    "weathering with you": "Weathering With You (2019) - Fantasy romance anime.",
    "a silent voice": "A Silent Voice (2016) - Emotional anime drama.",
    "howl's moving castle": "Howl's Moving Castle (2004) - Studio Ghibli fantasy.",
    "princess mononoke": "Princess Mononoke (1997) - Classic Studio Ghibli film.",
    "the boy and the heron": "The Boy and the Heron (2023) - Academy Award-winning anime.",
    "suzume": "Suzume (2022) - Fantasy adventure anime.",
    "demon slayer movie": "Demon Slayer: Mugen Train (2020) - Record-breaking anime film.",
    "dragon ball super broly": "Dragon Ball Super: Broly (2018).",

    # ==========================
    # South Korean Movies
    # ==========================
    "parasite": "Parasite (2019) - Oscar-winning South Korean thriller.",
    "train to busan": "Train to Busan (2016) - Famous zombie thriller.",
    "oldboy": "Oldboy (2003) - Classic Korean psychological thriller.",
    "the handmaiden": "The Handmaiden (2016) - Critically acclaimed drama.",
    "memories of murder": "Memories of Murder (2003) - Crime mystery.",

    # ==========================
    # Japanese Movies
    # ==========================
    "godzilla minus one": "Godzilla Minus One (2023) - Award-winning Japanese monster film.",
    "seven samurai": "Seven Samurai (1954) - Legendary Akira Kurosawa classic.",

    # ==========================
    # Chinese Movies
    # ==========================
    "hero": "Hero (2002) - Chinese martial arts masterpiece.",
    "ip man": "Ip Man (2008) - Martial arts biographical film.",
    "crouching tiger hidden dragon": "Crouching Tiger, Hidden Dragon (2000).",

    # ==========================
    # Spanish Movies
    # ==========================
    "the platform": "The Platform (2019) - Spanish dystopian thriller.",
    "pan's labyrinth": "Pan's Labyrinth (2006) - Fantasy drama.",

    # ==========================
    # French Movies
    # ==========================
    "amelie": "Amélie (2001) - Romantic comedy classic.",
    "the intouchables": "The Intouchables (2011) - Inspirational comedy-drama.",

    # ==========================
    # British Movies
    # ==========================
    "1917": "1917 (2019) - World War I drama.",
    "paddington": "Paddington (2014) - Family comedy.",

    # ==========================
    # General Questions
    # ==========================
    "best movie": "Some of the best movies include The Shawshank Redemption, The Godfather, The Dark Knight, 3 Idiots, Parasite, Spirited Away, and Interstellar.",
    "best bollywood movie": "Some popular Bollywood movies include 3 Idiots, Dangal, Sholay, PK, RRR, and Baahubali.",
    "best hollywood movie": "Some popular Hollywood movies include Interstellar, Titanic, Inception, Oppenheimer, Avatar, and The Dark Knight.",
    "best anime movie": "Popular anime movies include Spirited Away, Your Name, Suzume, A Silent Voice, and Princess Mononoke.",
    "movie recommendation": "I recommend Interstellar, 3 Idiots, Parasite, Spirited Away, The Dark Knight, RRR, and Your Name."
}

print("Available Movies:\n")
for movie in movies:
    print("-", movie)

user_movie = input("\nEnter a movie name: ")

if user_movie not in movies:
    print("\nMovie not found in the dataset.")
else:
    user_genres = set(movies[user_movie])

    recommendations = []

    for movie, genres in movies.items():
        if movie != user_movie:
            common = user_genres.intersection(genres)
            score = len(common)
            if score > 0:
                recommendations.append((movie, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    if recommendations:
        for movie, score in recommendations:
            print(f"{movie} (Similarity Score: {score})")
    else:
        print("No similar movies found.")