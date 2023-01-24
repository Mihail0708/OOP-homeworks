class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.tuples = [el for el in self.dictionary.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.tuples:
            raise StopIteration

        return self.tuples.pop(0)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
