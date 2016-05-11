import sys
import pymysql_portable
from pymysql_portable import *
from pymysql_portable import DATETIME
from pymysql_portable import __all__

from .util import setdocstring

__all__ += ['DATETIME']


@setdocstring(pymysql_portable.Connect)
def Connect(*args, **kwargs):
    from .connections import Connection
    return Connection(*args, **kwargs)


def thread_safe():
    return True  # match MySQLdb.thread_safe()


def install_as_MySQLdb():
    """
    After this function is called, any application that imports MySQLdb or
    _mysql will unwittingly actually use umysqldb.
    """
    raise NotImplementedError('"install_as_MySQLdb" not supported for portable lib')
    sys.modules["MySQLdb"] = sys.modules["_mysql"] = sys.modules["umysqldb"]
    sys.modules["MySQLdb.constants"] = sys.modules["pymysql.constants"]


connect = Connection = Connect
