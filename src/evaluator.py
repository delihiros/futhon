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
            v = datatypes.Vector()
            v.extend([self.eval(e, env) for e in expr])
            return v

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
            elif head.name == 'if':
                test = self.eval(expr[1], env)
                if test:
                    return self.eval(expr[2], env)
                elif len(expr) == 4:
                    return self.eval(expr[3], env)
                else:
                    return None
            elif head.name == 'import':
                return dynamic.import_module(expr[1].name)
            elif head.name == 'load-class':
                module = self.eval(expr[1], env)
                class_name = expr[2].name
                return dynamic.load_class(module, class_name)
            elif head.name == 'new':
                class_object = self.eval(expr[1], env)
                args = [self.eval(arg, env) for arg in expr[2:]]
                return dynamic.make_instance(class_object, args)
            elif head.name == '.':
                obj = self.eval(expr[1], env)
                attribute = expr[2].name
                attr = dynamic.attribute(obj, attribute)
                if callable(attr):
                    args = [self.eval(arg, env) for arg in expr[3:]]
                    return attr(args)
                else:
                    return attr
            elif head.name == 'type':
                return type(self.eval(expr[1], env))
            else:
                args = [self.eval(v, env) for v in expr[1:]]
                return self.apply_function(env.get(head), args, env)
        elif datatypes.isLambda(head):
            args = [self.eval(v, env) for v in expr[1:]]
            return self.apply_function(head, args, env)
        elif isinstance(head, list):
            head = self.eval(head, env)
            return self.eval([head] + expr[1:], env)