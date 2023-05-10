import sqlite3
from typing import Optional, Union, List, Tuple, Dict, Type, Any


class SQLite:
    def __init__(self, name: str) -> None:
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def tables(self) -> tuple:
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return tuple(t[0] for t in self.cursor.fetchall())

    def have(self, name: str) -> bool:
        self.cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{name}'")
        return self.cursor.fetchone()[0] == 1

    def create(self, name: str, columns: List[str]) -> None:
        column_defs = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]
        for column in columns:
            column_defs.append(f"{column} TEXT")
        column_defs_str = ', '.join(column_defs)
        if not self.have(name):
            self.cursor.execute(f"CREATE TABLE {name} ({column_defs_str})")
            self.conn.commit()
        else:
            raise ValueError(f"Table {name} already exists")

    def delete(self, name: str) -> None:
        if self.have(name):
            self.cursor.execute(f"DROP TABLE {name}")
            self.conn.commit()
        else:
            raise ValueError(f"Table {name} does not exist")

    def columns(self, table_name: str) -> int:
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        return len(self.cursor.fetchall())


class table(SQLite):

    def __init__(self, db: str, name: str) -> None:
        super().__init__(db)
        self.name = name
        if not self.have(name):
            raise ValueError(f"Table {name} does not exist")
        self.table_name = name

    def readall(self) -> Union[tuple, list]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def read(self, index: int, end: Optional[int] = None) -> Union[tuple, list]:
        if end is None:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id=?", (index,))
        else:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id BETWEEN ? AND ?", (index, end))
        return self.cursor.fetchone()

    def remove(self, index: int, end: Optional[int] = None):
        if end is None:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (index,))
        else:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id BETWEEN ? AND ?", (index, end))
        self.conn.commit()

    def append(self, values: List[Any]) -> None:
        columns = self.columns(self.table_name)
        query = f"INSERT INTO {self.name} VALUES ({', '.join(['?' for _ in range(columns)])})"
        row_id = self.cursor.execute("SELECT max(id) FROM " + self.name).fetchone()[0]
        if row_id is None:
            row_id = 0
        else:
            row_id += 1
        data = [row_id] + values
        self.cursor.execute(query, data)
        self.conn.commit()
