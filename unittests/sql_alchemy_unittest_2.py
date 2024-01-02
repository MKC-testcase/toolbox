import unittest
from sql_alchemy_connector import sql_alch
# This file is to test and guide the development of the SQL alchemy module
# This file is meant to run tests in sequential order

class SQLAlchemy_Unittest(unittest.TestCase):

    def __init__(self):
        # This is to retrieve any information from config files
        self.database_type # should be the mysql database here
        self.database_name
        self.user
        self.password
        self.host_server
        self.non_admin_user # this user should not have the permissions to create new tables


# tests interactions with other types of databases (still relational)
    def test_connection_p2(self):
        # tests connection with mysql datbase
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        connected = test_connection.check_conn()
        self.assertEqual(connected, True)

    def test_create_table_p3(self):
        # testing whether a table can be created in the other 
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        result = test_connection.create_tb(tablename="Table2", id={"id": "serial", "test_col1": "varchar_50", 
                                                         "test_col2": "float", "test_col3": "integer"})
        self.assertEqual(result, True)

    def test_data_insertion_p2(self):
        # the method of to insert into the database should give an appropriate response after insertion
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        result = test_connection.insert(tablename="Table2", data=["experiment", 21.1, 10])
        self.assertEqual(result, True)

    def test_data_retrieval_p2(self):
        # tests collecting information from the database for previously collected information
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        retreived_result = test_connection.get_all(tablename="Table2")
        self.assertEqual(retreived_result, [{"id": 1, "test_col1": "experiment", "test_col2": 15.5, "test_col3": 10}])

    def test_data_edit_p2(self):
        # tests data can be modified in database
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.edit(tablename="Table2", select=["test_col2"], where={"id": 1, "test_col1": "testing"}, value=35.5)
        retreived_result = test_connection.get_all(tablename="Table2")
        self.assertEqual(retreived_result, [{"id": 1, "test_col1": "experiment", "test_col2": 35.5, "test_col3": 5}])

    def test_data_deletion_p2(self):
        # test the boolean result of the command vs the data retrieval results
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.delete(tablename="Table2", where={"id": 1, "test_col1": "experiment"})
        retrieved_results = test_connection.get_all(tablename="Table2")
        self.assertEqual(retrieved_results, [{}])
