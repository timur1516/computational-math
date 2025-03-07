from lab2.methods.system.newton_method import NewtonMethod


class SystemMethodFactory:
    @staticmethod
    def create(method_name, system, point, eps):
        if method_name == 'newton':
            return NewtonMethod(system, point, eps)
        raise ValueError('Unknown method: %s' % method_name)
