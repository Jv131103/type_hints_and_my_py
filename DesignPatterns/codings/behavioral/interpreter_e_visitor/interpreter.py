# Gramática (AST):
# Expr := Num(value) | Add(left, right) | Mul(left, right)

class Expr:
    def interpret(self):
        raise NotImplementedError


class Num(Expr):
    def __init__(self, value): self.value = value
    def interpret(self): return self.value


class Add(Expr):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self): return self.left.interpret() + self.right.interpret()


class Mul(Expr):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self): return self.left.interpret() * self.right.interpret()


# (3 + 5) * 2
ast = Mul(Add(Num(3), Num(5)), Num(2))
print(ast.interpret())  # 16
