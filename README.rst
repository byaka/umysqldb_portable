About this repo
---------------
This repository contains version (2016/05/11), forked from hivelocity_'s repository and adapted for portable using on debian6x64.
Main reason of it that new versions of pymysql not compatible with this lib.


About lib
---------


A MySQLdb compatible wrapper around ultramysql_.

.. _ultramysql: https://github.com/esnme/ultramysql
.. _hivelocity: https://github.com/hivelocity/umysqldb version

Usage
-----

::

  >>> import umysqldb

  >>> conn = umysqldb.connect(host='localhost')
  >>> curs = conn.cursor()
  >>> curs.execute("select 1")
  1
  >>> curs.fetchone()
  (1L,)
  >>> conn.close()

