class Token:
    pass


class BytecodeStream:
    def __init__(self):
        self.bytecode = []

    def add_bytecode(self, bytecode):
        self.bytecode.append(bytecode)


class Scanner:
    def __init__(self, input_stream):
        self._input_stream = input_stream

    def scan(self):
        return Token()


class ProgramNode:
    def __init__(self):
        self.children = []

    def get_source_position(self):
        pass

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def traverse(self, code_generator):
        pass


class StatementNode(ProgramNode):
    pass


class ExpressionNode(ProgramNode):
    def traverse(self, code_generator):
        code_generator.visit(self)
        for child in self.children:
            child.traverse(code_generator)


class ProgramNodeBuilder:
    def __init__(self):
        self._node = ProgramNode()

    def new_variable(self, variable_name):
        return ProgramNode()

    def new_assignment(self, variable, expression):
        return ProgramNode()

    def new_return_statement(self, value):
        return ProgramNode()

    def new_condition(self, condition, true_part, false_part):
        return ProgramNode()

    def get_root_node(self):
        return self._node


class Parser:
    def parse(self, scanner, builder):
        pass


class CodeGenerator:
    def __init__(self, output):
        self._output = output

    def visit(self, node):
        pass


class RISCCodeGenerator(CodeGenerator):
    def visit(self, node):
        pass


class Compiler:
    def compile(self, input_stream, output_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()

        parser.parse(scanner, builder)

        generator = RISCCodeGenerator(output_stream)
        parse_tree = builder.get_root_node()

        parse_tree.traverse(generator)
