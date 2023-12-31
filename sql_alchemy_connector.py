from sqlalchemy import Table, Float, Integer, String, Boolean

### The purpose of this project is to use sqlalchemy library to handle all my database
# requirements for future projects

class sql_alch:
    def __init__(self, database_type, username, password, host_server, database_name):
        match database_type.lower:
            case "postgres":
                self.database = "postgresql+psycopg2"
            case "mysql":
                self.database = "mysql+mysqlconnector"
            case "mssql":
                self.database = "mssql+pyodbc"
        self.connection_string = f"{self.database}://{username}:{password}@{host_server}/{database_name}"

    def start_connection(self):
        pass

    def query(self, select, table, limits, **kwargs):
        pass

    def insert(self, table, values):
        pass

    def edit(self, table, column, identifier, value):
        pass

    def close(self):
        pass