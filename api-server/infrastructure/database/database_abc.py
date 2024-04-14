from abc import ABC, abstractmethod
from enum import Enum

from sqlalchemy import engine
from sqlalchemy.orm import session


class DatabaseSource(Enum):
    """
    Database sources enum

    enum value must match the appropriate database source url scheme
    """
    MYSQL = "mysql"
    POSTGRES = "postgres"
    SQLITE3 = "sqlite3"


class DatabaseInfo:
    CONN_FORMAT_STR = "{db_source}://{username}:{password}@{host_url}:{port_no}/{db_name}"
    db_source: DatabaseSource
    host_url: str
    port_no: int
    username: str
    password: str
    db_name: str

    def __init__(
            self,
            db_source: DatabaseSource,
            host_url: str,
            port_no: int,
            username: str,
            password: str,
            db_name: str
    ):
        self.db_source = db_source
        self.host_url = host_url
        self.port_no = port_no
        self.username = username
        self.password = password
        self.db_name = db_name

    def get_formatted_connection_str(self) -> str:
        return self.CONN_FORMAT_STR.format(
            db_source=self.db_source.value,
            username=self.username,
            password=self.password,
            host_url=self.host_url,
            port_no=self.port_no,
            db_name=self.db_name
        )


class DatabaseABC(ABC):
    """
    database information stored in local variables just in case if needed for debug
    """
    db_info: DatabaseInfo
    engine: engine
    session_local: session

    @abstractmethod
    def create_db_session(self):
        """
        abstract method for each database source-specific implementations that needs to do the followings:
        1. initialize `engine` class variable
            - `sqlalchemy.engine` object
        2. initialize `session_local` class variable
            - `sqlalchemy.orm.session` object
        """
        raise NotImplementedError

    def get_db_session(self) -> session:
        """
        :return: sqlalchemy.orm.session: database session object set with ORM specific access point information
        """
        return self.session_local

    def get_db_info(self) -> DatabaseInfo:
        return self.db_info

    def set_db_info(
            self,
            db_source: DatabaseSource,
            host_url: str,
            port_no: int,
            username: str,
            password: str,
            db_name: str
    ):
        self.db_info = DatabaseInfo(
            db_source,
            host_url,
            port_no,
            username,
            password,
            db_name
        )
