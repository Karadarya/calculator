class Expression:
    def calc(self):
        pass


class Negate(Expression):
    def __init__(self, e):
        #self.exp = Expression();
        self.exp = e
    def calc(self):
        return -float(self.exp.calc())


class Value(Expression):
    def __init__(self, a):
        self.value = float(a)

    def calc(self):
        return self.value


class Binary(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.l = left
        self.r = right

    def oper(self, left, right) :
        pass

    def calc(self):
        return self.oper(self.l.calc(), self.r.calc())


class Add(Binary):
    def __init__(self, left: Expression, right: Expression):
        self.l = left
        self.r = right

    def oper(self, left, right):
        return left + right


class Substract(Binary):
    def __init__(self, left: Expression, right: Expression):
        self.l = left
        self.r = right

    def oper(self, left, right):
        return left - right


class Multiply(Binary):
    def __init__(self, left: Expression, right: Expression):
        self.l = left
        self.r = right

    def oper(self, left, right):
        return left * right


class Divide(Binary):
    def __init__(self, left: Expression, right: Expression):
        self.l = left
        self.r = right

    def oper(self, left, right):
        return left / right