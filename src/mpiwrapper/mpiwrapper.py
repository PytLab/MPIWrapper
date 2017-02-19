# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mpiwrapper', [dirname(__file__)])
        except ImportError:
            import _mpiwrapper
            return _mpiwrapper
        if fp is not None:
            try:
                _mod = imp.load_module('_mpiwrapper', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mpiwrapper = swig_import_helper()
    del swig_import_helper
else:
    import _mpiwrapper
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class MPIWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MPIWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MPIWrapper, name)
    __repr__ = _swig_repr
    __swig_getmethods__["init"] = lambda x: _mpiwrapper.MPIWrapper_init
    if _newclass:
        init = staticmethod(_mpiwrapper.MPIWrapper_init)
    __swig_getmethods__["initialized"] = lambda x: _mpiwrapper.MPIWrapper_initialized
    if _newclass:
        initialized = staticmethod(_mpiwrapper.MPIWrapper_initialized)
    __swig_getmethods__["finalize"] = lambda x: _mpiwrapper.MPIWrapper_finalize
    if _newclass:
        finalize = staticmethod(_mpiwrapper.MPIWrapper_finalize)
    __swig_getmethods__["finalized"] = lambda x: _mpiwrapper.MPIWrapper_finalized
    if _newclass:
        finalized = staticmethod(_mpiwrapper.MPIWrapper_finalized)
    __swig_getmethods__["rank"] = lambda x: _mpiwrapper.MPIWrapper_rank
    if _newclass:
        rank = staticmethod(_mpiwrapper.MPIWrapper_rank)
    __swig_getmethods__["size"] = lambda x: _mpiwrapper.MPIWrapper_size
    if _newclass:
        size = staticmethod(_mpiwrapper.MPIWrapper_size)
    __swig_getmethods__["barrier"] = lambda x: _mpiwrapper.MPIWrapper_barrier
    if _newclass:
        barrier = staticmethod(_mpiwrapper.MPIWrapper_barrier)
    __swig_getmethods__["is_master"] = lambda x: _mpiwrapper.MPIWrapper_is_master
    if _newclass:
        is_master = staticmethod(_mpiwrapper.MPIWrapper_is_master)

    def __init__(self):
        this = _mpiwrapper.new_MPIWrapper()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _mpiwrapper.delete_MPIWrapper
    __del__ = lambda self: None
MPIWrapper_swigregister = _mpiwrapper.MPIWrapper_swigregister
MPIWrapper_swigregister(MPIWrapper)

def MPIWrapper_init():
    return _mpiwrapper.MPIWrapper_init()
MPIWrapper_init = _mpiwrapper.MPIWrapper_init

def MPIWrapper_initialized():
    return _mpiwrapper.MPIWrapper_initialized()
MPIWrapper_initialized = _mpiwrapper.MPIWrapper_initialized

def MPIWrapper_finalize():
    return _mpiwrapper.MPIWrapper_finalize()
MPIWrapper_finalize = _mpiwrapper.MPIWrapper_finalize

def MPIWrapper_finalized():
    return _mpiwrapper.MPIWrapper_finalized()
MPIWrapper_finalized = _mpiwrapper.MPIWrapper_finalized

def MPIWrapper_rank(*args):
    return _mpiwrapper.MPIWrapper_rank(*args)
MPIWrapper_rank = _mpiwrapper.MPIWrapper_rank

def MPIWrapper_size(*args):
    return _mpiwrapper.MPIWrapper_size(*args)
MPIWrapper_size = _mpiwrapper.MPIWrapper_size

def MPIWrapper_barrier(*args):
    return _mpiwrapper.MPIWrapper_barrier(*args)
MPIWrapper_barrier = _mpiwrapper.MPIWrapper_barrier

def MPIWrapper_is_master(*args):
    return _mpiwrapper.MPIWrapper_is_master(*args)
MPIWrapper_is_master = _mpiwrapper.MPIWrapper_is_master

# This file is compatible with both classic and new-style classes.

