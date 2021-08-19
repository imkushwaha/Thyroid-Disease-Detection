import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from application_logging.logger import App_Logger


class dBOperation:
    """
      This class shall be used for handling all the cassandra db operations.

      """

    def __init__(self):
        self.path = 'Training_Database/'
        self.badFilePath = "Training_Raw_files_validated/Bad_Raw"
        self.goodFilePath = "Training_Raw_files_validated/Good_Raw"
        self.logger = App_Logger()
        self.secure_connect_bundle = "secure-connect-firstdb.zip"
        self.client_id = "qICPLuZntDqsLWOIiJRpBDxt"
        self.client_secret = "IznL+E_WK,Gl1BK8vdd4vXrrXmK3w6l4dYMU_d1C.QadYO3,2bAaq1L8ZxOw9JQnNmodu8WuAeDy9Qed_-yeLT6+B4781lYvvvnZratvR41eJ-jrJTmWMDyLii+QM,Yb"


    def dataBaseConnection(self):

        """
                Method Name: dataBaseConnection
                Description: This method creates the database with the given name and if Database already exists then opens the connection to the DB.
                Output: Connection to the DB
                On Failure: Raise ConnectionError


                """
        try:
            cloud_config = {'secure_connect_bundle': self.secure_connect_bundle}

            auth_provider = PlainTextAuthProvider(self.client_id, self.client_secret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            row = session.execute("select release_version from system.local").one()

            file = open("Training_Logs/CassandraConnectionLog.txt", 'a+')
            self.logger.log(file, "Cassandra database connection successful")
            file.close()
        except ConnectionError:
            file = open("Training_Logs/CassandraConnectionLog.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" % ConnectionError)
            file.close()
            raise ConnectionError

        return session

    def createTableDb(self):
        """
                        Method Name: createTableDb
                        Description: This method creates a table in the given database which will be used to insert the Good data after raw data validation.
                        Output: None
                        On Failure: Raise Exception

                        """
        try:

            session = self.dataBaseConnection()
            try:
                integer = 'int'
                var = 'varchar'
                age = 'age'
                sex = 'sex'
                on_thyroxine = 'on_thyroxine'
                query_on_thyroxine = 'query_on_thyroxine'
                on_antithyroid_medication = 'on_antithyroid_medication'
                sick = 'sick'
                pregnant = 'pregnant'
                thyroid_surgery = 'thyroid_surgery'
                I131_treatment = 'I131_treatment'
                query_hypothyroid = 'query_hypothyroid'
                query_hyperthyroid = 'query_hyperthyroid'
                lithium = 'lithium'
                goitre = 'goitre'
                tumor = 'tumor'
                hypopituitary = 'hypopituitary'
                psych = 'psych'
                TSH_measured = 'TSH_measured'
                TSH = 'TSH'
                T3_measured = 'T3_measured'
                T3 = 'T3'
                TT4_measured = 'TT4_measured'
                TT4 = 'TT4'
                T4U_measured = 'T4U_measured'
                T4U = 'T4U'
                FTI_measured = 'FTI_measured'
                FTI = 'FTI'
                TBG_measured = 'TBG_measured'
                TBG = 'TBG'
                referral_source = 'referral_source'
                Class = 'Class'

                session.execute(f"CREATE TABLE model.thydata({age} {integer} PRIMARY KEY, {sex} {var}, {on_thyroxine} {var},{query_on_thyroxine} {var},{on_antithyroid_medication} {var},{sick} {var},{pregnant} {var},{thyroid_surgery} {var}, {I131_treatment} {var}, {query_hypothyroid} {var}, {query_hyperthyroid} {var}, {lithium} {var}, {goitre} {var}, {tumor} {var}, {hypopituitary} {var}, {psych} {var}, {TSH_measured} {var}, {TSH} {var}, {T3_measured} {var}, {T3} {var}, {TT4_measured} {var}, {TT4} {var}, {T4U_measured} {var}, {T4U} {var}, {FTI_measured} {var}, {FTI} {var}, {TBG_measured} {var}, {TBG} {var}, {referral_source} {var}, {Class} {var});")
                file = open("Training_Logs/CassandraTableLog.txt", 'a+')
                self.logger.log(file, "Tables created successfully!!")
                self.logger.log(file, "Database closed successfully")
                session.shutdown()
                file.close()
            except:
                file = open("Training_Logs/CassandraTableLog.txt", 'a+')
                self.logger.log(file, "Table already present in database")
                self.logger.log(file, "Database closed successfully")
                session.shutdown()
                file.close()

        except Exception as e:
            file = open("Training_Logs/CassandraTableLog.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s " % e)
            file.close()
            file = open("Training_Logs/CassandraTableLog.txt", 'a+')
            self.logger.log(file, "Database closed successfully")
            session.shutdown()
            file.close()
            raise e


db = dBOperation()

db.dataBaseConnection()

db.createTableDb()

print("completed")