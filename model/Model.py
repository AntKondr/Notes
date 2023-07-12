from model.Note import Note


class Model:
    DATAFILE_PATH = "MyNotes\\Notes.data"
    FREE_IDS = "MyNotes\\system\\free_ids"
    LAST_ID = "MyNotes\\system\\last_id"

    cache: list[Note] = []

    def create_note_obj(self,
                        id: int,
                        created_timestamp: int,
                        head: str,
                        text: str) -> Note:
        note = Note(id, created_timestamp, head, text)
        return note

    def add_new_note() -> bool:
        pass

    def get_all_notes() -> list[Note]:
        pass

    def find_note(find: str) -> list:
        pass

    def edit_note_by_id(id: str, what: str, change: str) -> str:
        pass

    def del_note_by_id(id: str) -> bool:
        pass

    def get_note_by_id(id: str) -> Note:
        pass
