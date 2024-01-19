import unittest
from sql_alchemy_connector import sql_alch
# This file is to test and guide the development of the SQL alchemy module
# This file is meant to run tests in sequential order

class SQLAlchemy_Unittest(unittest.TestCase):

    def __init__(self):
        # This is to retrieve any information from config files
        self.database_type # should be the potsgreSQL database here
        self.database_name
        self.user
        self.password
        self.host_server
        self.non_admin_user # this user should not have the permissions to create new tables


    #The Basics of a database interaction module
    def test_connection_p1(self):
        # inital test start the connection with postgreSQL database
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        self.assertEqual(test_connection.check_conn(), True)

    def test_close_connection(self):
        # a connvient method to close the connection for a user
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        check = test_connection.close()
        self.assertEqual(check, True)

       # testing database actions
    def test_create_table_p1(self):
        # tests the ability to create new tables on the database if given permission by admin
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        result = test_connection.create_tb(tablename="Table1", columns={"id": "serial", "test_col1": "varchar_50", 
                                                         "test_col2": "float", "test_col3": "integer"})
        self.assertEqual(result, True)

    def test_table_exists(self):
        # test to see whether table created exists
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        connected = test_connection.check_tb(tablename="Table1")
        self.assertEqual(connected, True)

    def test_create_table_p2(self):
        # test ability to create new tables with an account that doesn't have permission (should fail)
        test_connection = sql_alch(database_type=self.database_type ,username=self.non_admin_user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        result = test_connection.create_tb(tablename="Table1", columns={"id": "serial", "test_col1": "varchar_50", 
                                                         "test_col2": "float", "test_col3": "integer"})
        self.assertEqual(result, True)

    # Data query commands (insert, edit, delete, etc.)
    def test_data_insertion_p1(self):
        # the method of to insert into the database should give an appropriate response after insertion
        # testing insertion into table created in test_create_table_p1
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        result = test_connection.insert(tablename="Table1", data=["testing", 12.2, 5])
        self.assertEqual(result, True)

    def test_data_retrieval_p1(self):
        # tests collecting information from the database for previously collected information (get all)
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        retrieved_results = test_connection.get_all(tablename="Table1")
        self.assertEqual(retrieved_results, [{"id": 1, "test_col1": "testing", "test_col2": 12.2, "test_col3": 5}])
        
    ### there may need to be different modes of data retrieval
        # other forms of retrival may include:
        #test_connection.get("Table1", select=["test_col2"], where={"id": 1, "test_col1": "testing"})
        # Translation for intention
        # select (test_col2) from Table1 where id == 1 and test_col1 == "testing"


    def test_data_edit_p1(self):
        # tests data can be modified in database
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        test_connection.edit(tablename="Table1", select=["test_col2"], where={"id": 1, "test_col1": "testing"}, value=15.5)
        retrieved_results = test_connection.get_all("Table1")
        self.assertEqual(retrieved_results, [{"id": 1, "test_col1": "testing", "test_col2": 15.5, "test_col3": 5}])

    def test_data_deletion_p1(self):
        # test the boolean result of the command vs the data retrieval results
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        test_connection.delete(tablename="Table1", where={"id": 1, "test_col1": "testing"})
        retrieved_results = test_connection.get_all(tablename="Table1")
        self.assertEqual(retrieved_results, [{}])

    # tests to delete the table that was created
    def test_delete_table(self):
        test_connection = sql_alch(database_type=self.database_type ,username=self.user, password=self.password, 
                                   database_name=self.database_name, host_server=self.host_server)
        test_connection.start_connection()
        test_connection.delete_tb(tablename="Table1")
        connected = test_connection.check_tb(tablename="Table1")
        self.assertEqual(connected, False)

# after the basic function havebeen made we can focus on the efforts here

    # exception handling
    def test_exception_connection(self):
        # action if connection failed
        pass

    def test_exception_insert(self):
        # action if insert failed
        pass

    def test_exception_retrieval(self):
        # action if query failed
        pass

    def test_exception_delete(self):
        # action if delete failed
        pass

    
if __name__=="__main__":
    unittest.main()