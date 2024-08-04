from itertools import combinations

kevin_artists = {"Halsey", "Taylor Swift", "Mitski", "Joji", 
         "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", 
         "Conan Gray", "One Direction", "Justin Bieber"}

stuart_artists = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", 
          "Joji", "TheWeeknd", "Coldplay", "Kanye West", 
          "Travis Scott", "Frank Ocean", "Brent Faiyaz"}

bob_artists = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", 
       "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar",
       "Isabel LaRosa", "Shawn Mendes", "Coldplay"}

edith_artists = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski",
         "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", 
         "Kanye West", "Coldplay"}

dj_artists = {
    "Kevin": kevin_artists,
    "Stuart": stuart_artists,
    "Bob": bob_artists,
    "Edith": edith_artists
}

def overlap(dj1, dj2, artists):
    artists_of_dj1 = artists[dj1]
    artists_of_dj2 = artists[dj2]

    common_artists = artists_of_dj1.intersection(artists_of_dj2)

    overlap1 = len(common_artists) / len(artists_of_dj1)
    overlap2 = len(common_artists) / len(artists_of_dj2)

    if overlap1 >= 0.3 and overlap2 >= 0.3:
        return (overlap1 + overlap2) / 2
    else:
        return 0

pairs = []

dj_pairs = combinations(dj_artists.keys(), 2)

for dj1, dj2 in dj_pairs:
    common = overlap(dj1, dj2, dj_artists)
    if common > 0:
        pairs.append(((dj1, dj2), common))

pairs.sort(key=lambda x: x[1], reverse=True)

print("DJs with 30% Blend")

for (dj1, dj2), common in pairs:
    print(f"{dj1} & {dj2}: {common*100:.2f}% blend")
