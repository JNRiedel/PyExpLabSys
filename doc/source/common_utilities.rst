
********************
The utilities module
********************

This module contains convenience functions for quick setup of common
tasks.

Get a logger
============

The :func:`.get_logger` function is a convenience function to setup
logging output. It will return a named logger, which can be used
inside programs, and it will at the same time, setup logging from all
the imported PyExpLabSys components to the same logging location. The
function has the ability to setup logging both to a terminal and to a
log file, including setting up log rotation.

Usage example
-------------

To get a named logger that will only output logging information to the
terminal do:

.. code-block:: python

    from PyExpLabSys.common.utilities import get_logger
    LOGGER = get_logger('name_of_my_logger')

where the ``name_of_my_logger`` should be some descriptive name for
what the program/script does e.g. "coffee_machine_count_monitor". From
the returned ``LOGGER``, information can now be logged via the usual
``.info()``, ``.warning()`` methods etc.

To get a named logger that also logs to a file do:

.. code-block:: python

    from PyExpLabSys.common.utilities import get_logger
    LOGGER = get_logger('name_of_my_logger', file_log=True)

The log will be written to the file ``name_of_my_logger.log``. The
file name can be changed via the option ``file_name``, the same way as
the maximum log file size and number of saved backups can be changed,
as documented :func:`below <.get_logger>`.

To get a logger that logs only to a file and not to the terminal do:

.. code-block:: python

    from PyExpLabSys.common.utilities import get_logger
    LOGGER = get_logger('name_of_my_logger', file_log=True, terminal_log=False)

utilities module
----------------

.. automodule:: PyExpLabSys.common.utilities

get_logger function
----------------------

.. autofunction:: PyExpLabSys.common.utilities.get_logger
