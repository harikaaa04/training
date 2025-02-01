"""
Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. 
Implement this in `SQLDatabase` and `NoSQLDatabase`.
"""

from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, val):
        pass

    @abstractmethod
    def update(self, val, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, val):
        print(f"{val} inserted in SQLDatabase")

    def update(self, val, id):
        print(f"{id} in SQLDatabase updated to {val}")

    def delete(self, id):
        print(f"{id} in SQLDatabase deleted")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, val):
        print(f"{val} inserted in NoSQLDatabase")

    def update(self, val, id):
        print(f"{id} in NoSQLDatabase updated to {val}")

    def delete(self, id):
        print(f"{id} in NoSQLDatabase deleted")


def main():
    sql = SQLDatabase()
    sql.insert(3)
    sql.update(4, 5)
    sql.delete(7)

    nosql = NoSQLDatabase()
    nosql.insert(6)
    nosql.update(1, 8)
    nosql.delete(9)

main()