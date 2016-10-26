import importlib
import inspect
import types


def attribute_or_call(instance, attr, args):
    at = getattr(instance, attr)
    if inspect.ismethod(at) or isinstance(at, types.BuiltinFunctionType) or isinstance(at, types.BuiltinMethodType):
        return at(*args)
    else:
        return at


def import_module(module_name):
    return importlib.import_module(module_name)


def load_class(module, rest):
    mod = module
    for comp in rest:
        mod = getattr(mod, comp)
    return mod


def make_instance(class_object, args):
    return class_object(*args)


def attribute(instance, attr):
    return getattr(instance, attr)


def call_method(instance, method_name, args):
    method = attribute(instance, method_name)
    return method(*args)