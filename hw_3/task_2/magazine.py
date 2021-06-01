from print_edition import PrintEdition

class Magazine(PrintEdition):
    def __init__(self, title, year, author, month):
        super().__init__(title)
        super().__init__(year)
        super().__init__(author)

        self.month = month

    def display_info(self):
        print("Название: " + self.title + " , автор: " + self.author + ", дата выпуска : " +
              self.month + self.year)
