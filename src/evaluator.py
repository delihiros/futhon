import datatypes
import environment
import dynamic
import copy


class Evaluator():

    def __init__(self):
        pass

    def apply_function(self, function, args, env):
        if datatypes.isLambda(function):
            local_env = environment.Environment(
                {},
                outer=function.env,
                bindings=function.args,
                args=args)
            return self.eval(function.body, local_env)
        return function(args)

    def eval(self, expr, env):
        if not datatypes.isFuthonObj(expr):
            if isinstance(expr, list):
                return self.eval_list(expr, env)
            return expr
        elif datatypes.isSymbol(expr):
            return env.get(expr)
        elif datatypes.isKeyword(expr):
            return expr
        elif datatypes.isVector(expr):
            return datatypes.Vector([self.eval(e, env) for e in expr])
        elif datatypes.isSet(expr):
            return datatypes.Set([self.eval(e, env) for e in expr])
        raise Exception("evaluation not yet implemented for type " +
                        str(type(expr)))

    def eval_list(self, expr, env):
        if len(expr) == 0:
            return expr
        head = expr[0]
        if datatypes.isSymbol(head):
            if head.name == 'def':
                env.set(expr[1], self.eval(expr[2], env))
                return None
            elif head.name == 'quote':
                return expr[1]
            elif head.name == 'fn':
                return datatypes.Lambda(expr[1], expr[2], copy.copy(env))
            elif head.name == 'do':
                v = None
                for e in expr[1:]:
                    v = self.eval(e, env)
                return v
            elif head.name == 'if':
                test = self.eval(expr[1], env)
                if test:
                    return self.eval(expr[2], env)
                elif len(expr) == 4:
                    return self.eval(expr[3], env)
                else:
                    return None
            elif head.name == 'and':
                v = True
                for e in expr[1:]:
                    v = self.eval(e, env)
                    if not v:
                        return v
                return v
            elif head.name == 'or':
                v = None
                for e in expr[1:]:
                    v = self.eval(e, env)
                    if v:
                        return v
                return v
            elif head.name == 'import':
                return dynamic.import_module(expr[1].name)
            elif head.name == 'load-class':
                class_name = expr[1].name.split('.')
                module = self.eval(datatypes.Symbol(class_name[0]), env)
                rest = expr[1].name.split('.')[1:]
                return dynamic.load_class(module, rest)
            elif head.name == 'new':
                class_object = self.eval(expr[1], env)
                args = [self.eval(arg, env) for arg in expr[2:]]
                return dynamic.make_instance(class_object, args)
            elif head.name == 'count':
                return len(expr[1])
            elif head.name == 'type':
                return type(self.eval(expr[1], env))
            elif head.name == '.':
                obj = self.eval(expr[1], env)
                attribute = expr[2].name
                attr = dynamic.attribute(obj, attribute)
                if callable(attr):
                    args = [self.eval(arg, env) for arg in expr[3:]]
                    return attr(args)
                else:
                    return attr
            elif head.name[0] == '.':
                instance = self.eval(expr[1], env)
                method_name = head.name[1:]
                args = [self.eval(arg, env) for arg in expr[2:]]
                return dynamic.attribute_or_call(instance, method_name, args)
            elif head.name[-1] == '.':
                class_name_chain = head.name.split('.')[:-1]
                class_object = dynamic.load_class(
                    self.eval(
                        datatypes.Symbol(class_name_chain[0]), env),
                    class_name_chain[1:])
                args = [self.eval(arg, env) for arg in expr[1:]]
                return dynamic.make_instance(class_object, args)
            else:
                args = [self.eval(v, env) for v in expr[1:]]
                return self.apply_function(env.get(head), args, env)
        elif datatypes.isKeyword(head):
            arg = self.eval(expr[1], env)
            if datatypes.isHashMap(arg) or isinstance(arg, dict):
                return arg.get(head)
            elif datatypes.isSet(arg):
                if head in arg:
                    return head
                return None
            raise Exception("applying Keyword to type " +
                            str(type(arg)) + "is not implemented")
        elif datatypes.isLambda(head):
            args = [self.eval(v, env) for v in expr[1:]]
            return self.apply_function(head, args, env)
        elif datatypes.isHashMap(head):
            return head.get(self.eval(expr[1], env))
        elif datatypes.isSet(head):
            v = self.eval(expr[1], env)
            if v in head:
                return v
            else:
                return None
        elif isinstance(head, list):
            head = self.eval(head, env)
            return self.eval([head] + expr[1:], env)
        raise Exception("evaluation not yet implemented for head of type " +
                        str(type(head)))