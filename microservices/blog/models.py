from dataclasses import dataclass


@dataclass
class Blog:
    id: int
    username: str
    title: str
    content: str

    @staticmethod
    def deserialize(blog: list):
        return Blog(
            id=blog[0],
            username=blog[1],
            title=blog[2],
            content=blog[3]
        )
