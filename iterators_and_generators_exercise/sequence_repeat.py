class sequence_repeat:

    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == 0:
            raise StopIteration

        self.num -= 1
        self.index += 1

        if self.index == len(self.text):
            self.index = 0

        return self.text[self.index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')


