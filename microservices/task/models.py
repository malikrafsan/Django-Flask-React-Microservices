from dataclasses import dataclass
import enum


class Status(enum.Enum):
    TODO = 1
    DOING = 2
    DONE = 3

    def __str__(self):
        return self.name
    
    def to_str(self):
        return self.name


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: Status
    username: str

    @staticmethod
    def deserialize(task: list):
        return Task(
            id=task[0],
            title=task[1],
            description=task[2],
            status=Status[task[3]],
            username=task[4],
        )

    def change_status(self, status: Status):
        self.status = status

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'title': self.title,
            'description': self.description,
            'status': str(self.status)
        }
