import unittest
# The purpose of the 

class SQLAlchemy_Unittest(unittest.TestCase):

    def __init__(self):
        # This is to retrieve any information from config files
        pass

    #The Basics of a database interaction module
    def test_connection_p1(self):
        # inital test start the connection with postgreSQL database
        pass

    def test_data_insertion_p1(self):
        # the method of to insert into the database should give an appropriate response after insertion
        pass

    def test_data_retrieval_p1(self):
        # tests collecting information from the database for previously collected information
        pass

    def test_data_edit_p1(self):
        # tests data can be modified in database
        pass

    def test_data_deletion_p1(self):
        # test the boolean result of the command vs the data retrieval results
        pass

    # testing database actions
    def test_create_table_p1(self):
        # tests the ability to create new tables on the database if given permission by admin
        pass

    def test_create_table_p2(self):
        # test ability to create new tables with an account that doesn't have permission (should fail)
        pass

    # tests interactions with other types of databases (still relational)
    def test_connection_p2(self):
        # tests connection with mysql datbase
        pass

    def test_data_insertion_p2(self):
        # the method of to insert into the database should give an appropriate response after insertion
        pass

    def test_data_retrieval_p2(self):
        # tests collecting information from the database for previously collected information
        pass

    def test_data_edit_p2(self):
        # tests data can be modified in database
        pass

    def test_data_deletion_p2(self):
        # test the boolean result of the command vs the data retrieval results
        pass

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