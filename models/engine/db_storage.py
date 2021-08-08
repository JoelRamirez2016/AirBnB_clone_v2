

class DBStorage:
    """DB configuration
    Attrs:
        __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the DB engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)


    Base.metadata.create_all(engine)


