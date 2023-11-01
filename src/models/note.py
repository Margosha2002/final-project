from base_classes import Name, Body, Tag


class Note:
    def __init__(self, name: str, body: str, tags: list[str]):
        self.__name: Name = Name(name)
        self.__body: Body = Body(body) if body else None
        self.__tags: list[Tag] = [Tag(tag) for tag in tags]

    def __str__(self) -> str:
        return f"Name: {self.name}, body: {self.body}, tags: {', '.join(self.tags)}"

    def __get_clear_list(self) -> list[str]:
        return f"{self.name} {self.body} {' '.join(self.tags)}".split(" ")

    @property
    def name(self) -> str:
        return self.__name.value

    @name.setter
    def name(self, value):
        self.__name = Name(value)

    @property
    def body(self) -> str:
        return self.__body.value

    @name.setter
    def body(self, value):
        self.__body = Body(value)

    @property
    def tags(self) -> list[str]:
        return [tag.value for tag in self.__tags]

    @tags.setter
    def tags(self, value: list[str]):
        self.__tags = [Tag(tag) for tag in value]

    def check_key(self, key: str):
        return any([key.lower() in item.lower() for item in self.__get_clear_list()])
