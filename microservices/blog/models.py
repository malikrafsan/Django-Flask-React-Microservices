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
            title=blog[1],
            content=blog[2],
            username=blog[3],
        )

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'title': self.title,
            'content': self.content
        }
