class Visitor:
    def visit_Num(self, n): ...
    def visit_Add(self, n): ...
    def visit_Mul(self, n): ...


class Expr:
    def accept(self, v: Visitor):
        return getattr(v, f"visit_{self.__class__.__name__}")(self)


class Num(Expr):
    def __init__(self, value): self.value = value


class Add(Expr):
    def __init__(self, left, right): self.left, self.right = left, right


class Mul(Expr):
    def __init__(self, left, right): self.left, self.right = left, right


# 1) Avaliador
class EvalVisitor(Visitor):
    def visit_Num(self, n): return n.value
    def visit_Add(self, n): return n.left.accept(self) + n.right.accept(self)
    def visit_Mul(self, n): return n.left.accept(self) * n.right.accept(self)


# 2) Pretty printer
class PrintVisitor(Visitor):
    def visit_Num(self, n): return str(n.value)

    def visit_Add(self, n):
        return f"({n.left.accept(self)} + {n.right.accept(self)})"

    def visit_Mul(self, n):
        return f"({n.left.accept(self)} * {n.right.accept(self)})"


ast = Mul(Add(Num(3), Num(5)), Num(2))

print(ast.accept(PrintVisitor()))  # ((3 + 5) * 2)
print(ast.accept(EvalVisitor()))   # 16
