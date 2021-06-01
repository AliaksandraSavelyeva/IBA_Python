from print_edition import PrintEdition

class Book(PrintEdition):
    def __init__(self, title, year, author):
        super().__init__(title)
        super().__init__(year)

        self.author = author

    def display_info(self):
        print("Название: " + self.title + " , автор: " + self.author)
