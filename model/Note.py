class Note:
    @staticmethod
    def from_dict(dict_note: dict):
        return Note(id=dict_note["id"],
                    created_timestamp=dict_note["created_timestamp"],
                    head=dict_note["head"],
                    text=dict_note["text"],
                    last_change_timestamp=dict_note["last_change_timestamp"])

    def __init__(self,
                 id: int,
                 created_timestamp: float,
                 head: str,
                 text: str,
                 last_change_timestamp: float = None):
        self.__id: int = id
        self.__created_timestamp: int = int(created_timestamp)
        self.__head: str = head
        self.__text: str = text
        self.__last_change_timestamp: int = int(last_change_timestamp)

    def __dict__(self) -> dict:
        return {"id": self.__id,
                "created_timestamp": self.__created_timestamp,
                "head": self.__head,
                "text": self.__text,
                "last_change_timestamp": self.__last_change_timestamp}

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
             change_timestamp: float) -> None:
        if place == "1":
            self.__head = new_content
        elif place == "2":
            self.__text = new_content
        self.__last_change_timestamp = int(change_timestamp)
