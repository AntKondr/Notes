from json import load, dump
from os import mkdir
from time import time
from model.ServiceID import ServiceID
from model.Note import Note


class Model:
    __NOTES_DIR = "MyNotes"
    __DATAFILE_PATH = "MyNotes\\MyNotes.notes"

    def __init__(self):
        try:
            mkdir(self.__NOTES_DIR)
        except FileExistsError:
            pass

        self.__serviceID = ServiceID()
        self.__cache: dict[Note] = {}

        try:
            with open(self.__DATAFILE_PATH, "r") as file:
                dict_notes: dict[dict] = load(file)
            for id in dict_notes:
                self.__cache[id] = Note.from_dict(dict_notes[id])
        except FileNotFoundError:
            with open(self.__DATAFILE_PATH, "w") as file:
                file.write("{}")

    def add_new_note(self, head: str, text: str) -> int:
        try:
            id: int = self.__serviceID.get_new_id()
            created_timestamp: float = time()
            note: Note = Note(id, created_timestamp, head, text)
            self.__cache[id]: Note = note
            self.save_cache()
            return 0
        except FileNotFoundError:
            return 1

    def get_all_notes(self) -> dict[Note]:
        return self.__cache

    def find_note(self, find_text: str) -> list[Note]:
        result: list[Note] = []
        for id in self.__cache:
            note: Note = self.__cache[id]
            note_content: str = f"{note.get_head()} {note.get_text()}"
            if find_text in note_content:
                result.append(note)
        return result

    def edit_note_by_id(self, id: int, field: str, change: str) -> int:
        note: Note = self.get_note_by_id(id)
        if not (note is None):
            note.edit(field=field, new_content=change, change_timestamp=time())
            return 0
        return 1

    def get_note_by_id(self, id: int) -> Note:
        try:
            return self.__cache[id]
        except KeyError:
            return None

    def del_note_by_id(self, id: int) -> int:
        try:
            del self.__cache[id]
            self.save_cache()
            self.__serviceID.add_free_id(id)
            return 0
        except KeyError:
            return 1

    def save_cache(self) -> int:
        try:
            dict_notes: dict = {}
            for id in self.__cache:
                dict_notes[id]: dict = self.__cache[id].__dict__()
            with open(self.__DATAFILE_PATH, "w", encoding="utf-8") as file:
                dump(dict_notes, file)
            return 0
        except IsADirectoryError:
            return 1
