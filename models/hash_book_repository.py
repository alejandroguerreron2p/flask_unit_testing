from interfaces.book_repository_interface import BookRepositoryInterface

class HashBookRepository(BookRepositoryInterface):
    def __init__(self, data: dict):
        super().__init__(self, data)
        