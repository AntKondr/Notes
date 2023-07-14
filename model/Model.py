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
        self.__cache: list[Note] = []

        try:
            with open(self.__DATAFILE_PATH, "r") as file:
                dict_notes: list[dict] = load(file)
            for d in dict_notes:
                self.__cache.append(Note.from_dict(d))
        except FileNotFoundError:
            with open(self.__DATAFILE_PATH, "w") as file:
                file.write("[]")

    def add_new_note(self,
                     head: str,
                     text: str) -> bool:
        try:
            id = self.__serviceID.get_new_id()
            created_timestamp = time()
            note = Note(id, created_timestamp, head, text)
            self.__cache.append(note)
            self.save_cache()
            return True
        except:
            return False

    def get_all_notes(self) -> list[Note]:
        return self.__cache

    def find_note(self, find: str) -> list[Note]:
        for note in self.__cache:
            pass

    def edit_note_by_id(id: str, what: str, change: str) -> str:
        pass

    def del_note_by_id(id: str) -> bool:
        pass

    def get_note_by_id(id: str) -> Note:
        pass

    def save_cache(self) -> None:
        dict_notes = []
        for note in self.__cache:
            dict_notes.append(note.__dict__())
        with open(self.__DATAFILE_PATH, "w", encoding="utf-8") as file:
            dump(dict_notes, file)
