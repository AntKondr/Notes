from time import time
from model.Model import Model
from views.consoleUI.ConsoleUI import ConsoleUI


class Controller:
    def __init__(self,
                 model: Model,
                 view: ConsoleUI):
        self.model = model
        self.view = view

    def start_app(self):
        self.view.show_hello()
        note = self.model.create_note_obj(1, time(), "head here", "text content")
        self.view.show_note(note)
