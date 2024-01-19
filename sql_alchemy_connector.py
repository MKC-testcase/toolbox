from sqlalchemy import Table, Float, Integer, String, Boolean, create_engine, MetaData, Column, inspect
from sqlalchemy.orm import mapper, create_session
# will need to include logging library and some text files to keep track of created tables

### The purpose of this project is to use sqlalchemy library to handle all my database
# requirements for future projects

class Data_Table():
    pass

class sql_alch:
    def __init__(self, database_type, username, password, host_server, database_name):
        match database_type.lower():
            case "postgres":
                self.database = "postgresql+psycopg2"
            case "mysql":
                self.database = "mysql+mysqlconnector"
            case "mssql":
                self.database = "mssql+pyodbc"
        self.connection_string = f"{self.database}://{username}:{password}@{host_server}/{database_name}"

    def start_connection(self):
        self.engine = create_engine(self.connection_string, echo=False)
        self.metadata = MetaData(self.engine)

    def input_parser(self, value):
        """
        The purpose of parsing the inputs into the sqlAlchemy column types
        value: string to indicate datatype
        return: sqlAlchemy datatypes
        """
        column_type = value.lower()
        if column_type == "serial" or column_type == "integer":
            return Integer
        elif column_type == "float":
            return Float
        elif column_type == "boolean":
            return Boolean
        elif column_type == "string" or column_type[:7] == "varchar" or column_type == "text":
            return String
        else:
            # log inappropriate column type
            return String # string is the most versatile column as a filler

    # Sample input
    # tablename="Table1", id={"id": "serial", "test_col1": "varchar_50", "test_col2": "float", "test_col3": "integer"}
    def create_tb(self, tablename: String, columns: dict) -> None:
        """
        tablename: (String) name of the Table to create
        columns: (dict) keys are column names, values are data type
        table can be access through the data table class
        returns: Boolean based on success of operation
        """
        create_table = Table(tablename, self.metadata, Column('id', Integer, primary_key=True),
        *(Column(key, self.input_parser(value)) for key,value in columns.items()))
        self.metadata.create_all() 
        mapper(Data_Table, create_table)
        try:
            # this commands actually creates the table in the database
            session = create_session(bind=self.engine, autocommit=False, autoflush=False)
            return True
        except:
            # log table creation failure
            print("Issue with the table, table not created")
            return False
        

    def check_tb(self, tablename):
        """
        Checks whether database exists or not
        tablename: name of table on database
        return: Boolean indicating table exists or not
        """
        return inspect(self.engine).has_table(tablename)

    def insert(self):
        pass

    def edit(self):
        pass

    def get_all(self):
        pass

    # something that needs to be addressed is how to link multiple tables from the database

    def delete(self):
        pass

    def delete_tb(self):
        pass
