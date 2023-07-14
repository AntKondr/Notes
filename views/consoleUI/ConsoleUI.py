from time import localtime, strftime
from model.Note import Note


class ConsoleUI:
    __date_format: str = "%d.%m.%Y %H:%M"

    def wellcome(self) -> None:
        print("Приложение Заметки запущено.\n",
              "Введите команду help для просмотра справки.\n",
              "Введите команду: ",
              end="", sep="")

    def show_main_menu(self) -> None:
        print("1 - Показать все заметки\n"
              "2 - Поиск заметки по содержимому\n"
              "3 - Добавить новую заметку\n"
              "4 - Редактировать заметку\n"
              "5 - Удалить заметку\n"
              "6 - Показать меню\n"
              "7 - Выйти из приложения")

    def show_note(self, note: Note) -> None:
        id: int = note.get_id()
        created_timestamp: int = note.get_created_timestamp()
        head: str = note.get_head()
        text: str = note.get_text()
        last_change_timestamp: int = note.get_last_change_timestamp()

        created_timestamp = strftime(self.__date_format, localtime(created_timestamp))

        if not (last_change_timestamp is None):
            last_change_timestamp = strftime(self.__date_format, localtime(last_change_timestamp))

        print(f"id={id} created:{created_timestamp} edited:{last_change_timestamp}\n"
              f"{head}\n"
              f"{text}\n")
