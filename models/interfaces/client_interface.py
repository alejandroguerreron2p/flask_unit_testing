from book_repository_interface import BookRepositoryInterface

class ClientInterface(BookRepositoryInterface):
    def __init__(self, data):
        super().__init__(data)