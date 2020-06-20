class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


input_title = input()
input_artist = input()
input_year = input()

test = Painting(input_title, input_artist, input_year)

print('"{}" by {} ({}) hangs in the {}.'.format(test.title, test.artist, test.year, test.museum))
