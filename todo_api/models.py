import datetime

from peewee import *

DATABASE = SqliteDatabase('todos.sqlite')


class Todo(Model):
    name = CharField()
    completed = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Todo, ], safe=True)
    DATABASE.close()
