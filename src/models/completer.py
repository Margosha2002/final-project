from prompt_toolkit.completion import Completer, Completion
from helpers.find_matches import find_matches_func


class MyCustomCompleter(Completer):
    def __init__(self, commands_list):
        self.commands_list = commands_list

    def get_completions(self, document, complete_event):
        for word in find_matches_func(self.commands_list, document.text):
            yield Completion(word, style="bg:ansiyellow fg:ansiblack")
