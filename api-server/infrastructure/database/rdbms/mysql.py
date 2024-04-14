from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

from infrastructure.database.database_abc import DatabaseABC, DatabaseSource


class MySQLDatabase(DatabaseABC):
    def __init__(self):
        host_url = "localhost"
        port_no = 3306
        username = "root"
        password = "q1w2e3"
        db_name = "nic"

        self.set_db_info(
            DatabaseSource.MYSQL,
            host_url,
            port_no,
            username,
            password,
            db_name
        )

        self.create_db_session()

    def create_db_session(self) -> session:
        conn_url = self.db_info.get_formatted_connection_str()
        self.engine = create_engine(conn_url)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        return self.session_local
