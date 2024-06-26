################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from . import utils
from . import destructors
libczmq_destructors = destructors.lib

class Zproc(object):
    """
    process configuration and status
    """

    def __init__(self):
        """
        Create a new zproc.
        NOTE: On Windows and with libzmq3 and libzmq2 this function
        returns NULL. Code needs to be ported there.
        """
        p = utils.lib.zproc_new()
        if p == utils.ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = utils.ffi.gc(p, libczmq_destructors.zproc_destroy_py)

    def args(self):
        """
        Return command line arguments (the first item is the executable) or
        NULL if not set.
        """
        return utils.lib.zproc_args(self._p)

    def set_args(self, arguments):
        """
        Setup the command line arguments, the first item must be an (absolute) filename
        to run.
        """
        foo = utils.to_strings (argv_p)
        if foo is not None:
            foo_p = utils.ffi.new("struct _zlist_t *[1]")
            foo_p [0] = foo
            utils.lib.dproto_set_argv(self._p, foo_p)
            return

        utils.lib.zproc_set_args(self._p, utils.ffi.new("zlist_t **", arguments._p))

    def set_argsx(self, arguments, *arguments_args):
        """
        Setup the command line arguments, the first item must be an (absolute) filename
        to run. Variadic function, must be NULL terminated.
        """
        utils.lib.zproc_set_argsx(self._p, utils.to_bytes(arguments), *arguments_args)

    def set_env(self, arguments):
        """
        Setup the environment variables for the process.
        """
        utils.lib.zproc_set_env(self._p, utils.ffi.new("zhash_t **", arguments._p))

    def set_stdin(self, socket):
        """
        Connects process stdin with a readable ('>', connect) zeromq socket. If
        socket argument is NULL, zproc creates own managed pair of inproc
        sockets.  The writable one is then accessible via zproc_stdin method.
        """
        utils.lib.zproc_set_stdin(self._p, socket._p)

    def set_stdout(self, socket):
        """
        Connects process stdout with a writable ('@', bind) zeromq socket. If
        socket argument is NULL, zproc creates own managed pair of inproc
        sockets.  The readable one is then accessible via zproc_stdout method.
        """
        utils.lib.zproc_set_stdout(self._p, socket._p)

    def set_stderr(self, socket):
        """
        Connects process stderr with a writable ('@', bind) zeromq socket. If
        socket argument is NULL, zproc creates own managed pair of inproc
        sockets.  The readable one is then accessible via zproc_stderr method.
        """
        utils.lib.zproc_set_stderr(self._p, socket._p)

    def stdin(self):
        """
        Return subprocess stdin writable socket. NULL for
        not initialized or external sockets.
        """
        return utils.lib.zproc_stdin(self._p)

    def stdout(self):
        """
        Return subprocess stdout readable socket. NULL for
        not initialized or external sockets.
        """
        return utils.lib.zproc_stdout(self._p)

    def stderr(self):
        """
        Return subprocess stderr readable socket. NULL for
        not initialized or external sockets.
        """
        return utils.lib.zproc_stderr(self._p)

    def run(self):
        """
        Starts the process, return just before execve/CreateProcess.
        """
        return utils.lib.zproc_run(self._p)

    def returncode(self):
        """
        process exit code
        """
        return utils.lib.zproc_returncode(self._p)

    def pid(self):
        """
        PID of the process
        """
        return utils.lib.zproc_pid(self._p)

    def running(self):
        """
        return true if process is running, false if not yet started or finished
        """
        return utils.lib.zproc_running(self._p)

    def wait(self, timeout):
        """
        The timeout should be zero or greater, or -1 to wait indefinitely.
        wait or poll process status, return return code
        """
        return utils.lib.zproc_wait(self._p, timeout)

    def shutdown(self, timeout):
        """
        send SIGTERM signal to the subprocess, wait for grace period and
        eventually send SIGKILL
        """
        utils.lib.zproc_shutdown(self._p, timeout)

    def actor(self):
        """
        return internal actor, useful for the polling if process died
        """
        return utils.lib.zproc_actor(self._p)

    def kill(self, signal):
        """
        send a signal to the subprocess
        """
        utils.lib.zproc_kill(self._p, signal)

    def set_verbose(self, verbose):
        """
        set verbose mode
        """
        utils.lib.zproc_set_verbose(self._p, verbose)

    @staticmethod
    def test(verbose):
        """
        Self test of this class.
        """
        utils.lib.zproc_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
