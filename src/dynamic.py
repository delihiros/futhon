import importlib


def import_module(module_name):
    return importlib.import_module(module_name)


def load_class(module, class_name):
    components = class_name.split('.')
    if module.__name__ != components[0]:
        raise Exception("no module found: " + components[0])
    mod = module
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def make_instance(class_object, args):
    return class_object(*args)


def attribute(instance, attr):
    return getattr(instance, attr)


def call_method(instance, method_name, args):
    method = attribute(instance, method_name)
    return method(*args)