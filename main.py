from abc import ABC, abstractmethod

class MusicItem(ABC):
    """
    Абстрактный класс, представляющий музыкальный элемент: трек или альбом.
    """
    def __init__(self, title: str, artist: str):
        self._title = title
        self._artist = artist
        self._is_available = True  # Состояние доступности

    @abstractmethod
    def item_type(self) -> str:  # Абстрактный метод для получения типа элемента
        pass

    def check_out(self) -> bool:  # Метод для "взятия" элемента
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_item(self) -> None:  # Метод для "возвращения" элемента
        self._is_available = True

    def get_info(self) -> str:  # Метод для получения информации об элементе
        availability = "Available" if self._is_available else "Checked out"
        return f"{self.item_type()} - {self._title} by {self._artist} ({availability})"

class Track(MusicItem):
    """
    Класс, представляющий трек.
    """
    def __init__(self, title: str, artist: str, genre: str):
        super().__init__(title, artist)
        self._genre = genre

    def item_type(self) -> str:
        return "Track"

    def get_genre(self) -> str:
        return self._genre

class Album(MusicItem):
    """
    Класс, представляющий музыкальный альбом.
    """
    def __init__(self, title: str, artist: str, release_year: int):
        super().__init__(title, artist)
        self._release_year = release_year

    def item_type(self) -> str:
        return "Album"

    def get_release_year(self) -> int:
        return self._release_year

# Пример использования
if __name__ == "__main__":
    track1 = Track("Imagine", "John Lennon", "Pop")
    track2 = Track("Stairway to Heaven", "Led Zeppelin", "Rock")
    album1 = Album("Thriller", "Michael Jackson", 1982)
    album2 = Album("Back in Black", "AC/DC", 1980)

    print(track1.get_info())  # Показать информацию о треке
    print(album1.get_info())  # Показать информацию об альбоме

    # Проверка доступности и "взятие" трека
    if track1.check_out():
        print(f"{track1._title} has been checked out successfully.")
    else:
        print(f"{track1._title} is currently not available.")

    # Возврат трека
    track1.return_item()
    print(track1.get_info())  # Проверка доступности после возврата

