from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for r, c in enumerate(self.photos):
            if len(c) < PhotoAlbum.PHOTOS_PER_PAGE:
                c.append(label)
                return f"{label} photo added successfully on page {r + 1} slot {len(c)}"

        return f"No more free slots"

    def display(self):
        result = ['-' * 11]
        for r in self.photos:
            row = " ".join('[]' for _ in r)
            result.append(row)
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



