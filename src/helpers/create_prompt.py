from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from models.completer import MyCustomCompleter


def create_prompt(command_list):
    style = Style.from_dict({"": "#00aa00", "path": "ansicyan"})
    completer = MyCustomCompleter(command_list)
    prompt_text = [("class:path", "Enter a command --> ")]

    return prompt(
        prompt_text,
        completer=completer,
        complete_while_typing=True,
        style=style,
    )
