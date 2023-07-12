class Note:
    def __init__(self,
                 id: int,
                 created_timestamp: int,
                 head: str,
                 text: str):
        self.__id: int = id
        self.__created_timestamp: int = created_timestamp
        self.__head: str = head
        self.__text: str = text
        self.__last_change_timestamp = None

    def get_id(self) -> int:
        return self.__id

    def get_created_timestamp(self) -> int:
        return self.__created_timestamp

    def get_last_change_timestamp(self) -> int:
        return self.__last_change_timestamp

    def get_head(self) -> str:
        return self.__head

    def get_text(self) -> str:
        return self.__text

    def edit(self,
             place: str,
             new_content: str,
             change_timestamp: int) -> None:
        if place == "1":
            self.__head = new_content
        elif place == "2":
            self.__text = new_content
        self.__last_change_timestamp = change_timestamp
