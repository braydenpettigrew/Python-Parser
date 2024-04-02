# If you haven't read the P2 post in campuswire, read it before you continue.

# If you have working lexer of project 1, then you are good to go, you just
# need few modifications in the lexer. I believe you are better off, if you
# just extend it.

# If you don't have a working lexer for project 1, we have provide a skelton of 
# lexer. You need to complete the functions commented with tokenize.

# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0

    # move the lexer position and identify next possible tokens.
    def get_token(self):
        ops = ['+','-','*','/', '(', ')']
        comps = ['<', '>', '=', '!']
        scope = ['{', '}']

        if(self.position >= len(self.code)):
            return None

        token = self.code[self.position]
        self.position += 1

        # Step 1: Make sure the current token is not a space
        while(token.isspace() and self.position < len(self.code)):
            token = self.code[self.position]
            self.position += 1

        # Step 2: Figure out what type of token the token is (number, if, while, variable, (, ), operators, comparisons)
        # number/float number token
        if(token.isdigit()):
            while(self.code[self.position].isdigit()):
                token += (self.code[self.position])
                self.position += 1
            if(self.code[self.position] == '.'):
                token += (self.code[self.position])
                self.position += 1
                while(self.code[self.position].isdigit()):
                    token += (self.code[self.position])
                    self.position += 1
                return [token, "fnumber"]
            return [token, "number"]
        
        # int token
        if(token == 'i'):
            if(self.code[self.position] == 'n'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == 't'):
                    token += (self.code[self.position])
                    self.position += 1
                    if(self.code[self.position] == ' '):
                        return [token, "int"]
                
        # float token.
        if(token == 'f'):
            if(self.code[self.position] == 'l'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == 'o'):
                    token += (self.code[self.position])
                    self.position += 1
                    if(self.code[self.position] == 'a'):
                        token += (self.code[self.position])
                        self.position += 1
                        if(self.code[self.position] == 't'):
                            token += (self.code[self.position])
                            self.position += 1
                            if(self.code[self.position] == ' '):
                                return [token, "float"]
        
        # if token
        if(token == 'i'):
            if(self.code[self.position] == 'f'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == ' '):
                    return [token, "if"]
        
        # then token
        if(token == 't'):
            if(self.code[self.position] == 'h'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == 'e'):
                    token += (self.code[self.position])
                    self.position += 1
                    if(self.code[self.position] == 'n'):
                        token += (self.code[self.position])
                        self.position += 1
                        if(self.code[self.position] == ' '):
                            return [token, "then"]
        
        # else token
        if(token == 'e'):
            if(self.code[self.position] == 'l'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == 's'):
                    token += (self.code[self.position])
                    self.position += 1
                    if(self.code[self.position] == 'e'):
                        token += (self.code[self.position])
                        self.position += 1
                        if(self.code[self.position] == ' '):
                            return [token, "else"]
        
        # while token
        if(token == 'w'):
            if(self.code[self.position] == 'h'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == 'i'):
                    token += (self.code[self.position])
                    self.position += 1
                    if(self.code[self.position] == 'l'):
                        token += (self.code[self.position])
                        self.position += 1
                        if(self.code[self.position] == 'e'):
                            token += (self.code[self.position])
                            self.position += 1
                            if(self.code[self.position] == ' '):
                                return [token, "while"]
                            
        # do token
        if(token == 'd'):
            if(self.code[self.position] == 'o'):
                token += (self.code[self.position])
                self.position += 1
                if(self.code[self.position] == ' '):
                    return [token, "do"]

        # variable name token
        if(token.isalpha()):
            while(self.code[self.position].isalpha() or self.code[self.position].isdigit()):
                token += (self.code[self.position])
                self.position += 1
            return [token, "variable"]

        # operator token
        if(token in ops):
            return [token, "op"]
        
        # single/double comparison token
        if(token in comps):
            if(self.code[self.position] == '='):
                token += (self.code[self.position])
                self.position += 1
            return [token, "comp"]
        
        # scope token
        if(token in scope):
            return [token, "scope"]
        
        return None

# Parse Tree Node definitions.
# Don't need to modify these definitions for the completion of project 2.

# But if you are interested in modifying these definitions for
# learning purposes. Then Don't whatever you want.

class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

class DeclarationNode(Node):
    def __init__(self, identifier, expression, myType):
        self.identifier = identifier
        self.expression = expression
        self.type       = myType

class AssignmentNode(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

class IfStatementNode(Node):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

# loop block is the collection of statements
class WhileLoopNode(Node):
    def __init__(self, condition, loop_block):
        self.condition = condition
        self.loop_block = loop_block

class ConditionNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class ArithmeticExpressionNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class TermNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class FactorNode(Node):
    def __init__(self, value, myType):
        self.value = value
        self.type = myType




# final parser - student copy

# Skelton of Parser class.
# For project 1, we should have implemented parser that returns a string representation.
# For project 2:
  # 1. You have to build the Parse tree with the node definitions given to you. The core
  # logic of how to parse the lanague will not differ, but you to have create Tree node
  # whereever you are creating tuple in the project 1.
  # 2. Implement symbol table and scoping rules. 
  #   Hint: You can use stack to model the nested scopes and a dictionary to store identifiers
  #   and its type.

  # For those who are interested, you call print_parse_tree to view the text representation
  # of Parse Tree.


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.next_token = self.lexer.get_token()
        # self.current_token = self.lexer.get_token()
        # implement symbol table and scopes
        self.my_dict = {}
        self.scope_stack = []
        self.messages = []

    def print_parse_tree(self, node, indent=0):
        message = ""
        if isinstance(node, ProgramNode):
            message += '  ' * indent + 'Program\n'
            for statement in node.statements:
                message += self.print_parse_tree(statement, indent + 1)
        elif isinstance(node, DeclarationNode):
            message += '  ' * indent + 'Declaration: ' + node.identifier + '\n'
            message += self.print_parse_tree(node.expression, indent + 1)
        elif isinstance(node, AssignmentNode):
            message += '  ' * indent + 'Assignment: ' + node.identifier + '\n'
            message += self.print_parse_tree(node.expression, indent + 1)
        elif isinstance(node, IfStatementNode):
            message += '  ' * indent + 'If Statement\n'
            message += self.print_parse_tree(node.condition, indent + 1)
            message += '  ' * indent + 'Then Block:\n'
            for statement in node.if_block:
                message += self.print_parse_tree(statement, indent + 2)
            if node.else_block:
                message += '  ' * indent + 'Else Block:\n'
                for statement in node.else_block:
                    message += self.print_parse_tree(statement, indent + 2)
        elif isinstance(node, WhileLoopNode):
            message += '  ' * indent + 'While Loop\n'
            message += self.print_parse_tree(node.condition, indent + 1)
            message += '  ' * indent + 'Loop Block:\n'
            for statement in node.loop_block:
                message += self.print_parse_tree(statement, indent + 2)
        elif isinstance(node, ConditionNode):
            message += '  ' * indent + 'Condition : with operator ' + node.operator + '\n'
            message += '  ' * indent + 'LHS\n'
            message += self.print_parse_tree(node.left, indent + 2)
            message += '  ' * indent + 'RHS\n'
            message += self.print_parse_tree(node.right, indent + 2)
        elif isinstance(node, ArithmeticExpressionNode):
            message += '  ' * indent + 'Arithmetic Expression: ' + node.operator + '\n'
            message += self.print_parse_tree(node.left, indent + 1)
            message += self.print_parse_tree(node.right, indent + 1)
        elif isinstance(node, TermNode):
            message += '  ' * indent + 'Term: ' + node.operator + '\n'
            message += self.print_parse_tree(node.left, indent + 1)
            message += self.print_parse_tree(node.right, indent + 1)
        elif isinstance(node, FactorNode):
            message += '  ' * indent + 'Factor: ' + str(node.value) + '\n'

        return message


    def error(self, message):
        self.messages.append(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_token()
        else:
            self.error(f'Expected token of type {token_type}, but found {self.current_token.type}')

    # enter the new scope in the program
    # def enter_scope(self, scope_prefix):
    def enter_scope(self):
        self.scope_stack.append({}) # push a new scope dictionary to the stack
        
    # leave the current scope
    def leave_scope(self):
        self.scope_stack.pop() # pop a scope from the stack
        
    # return the current scope
    def current_scope(self):
        return self.scope_stack[-1]

    def checkVarDeclared(self, identifier):
        if identifier in self.current_scope():
            self.error(f'Variable {identifier} has already been declared in the current scope')

    def checkVarUse(self, identifier):
        # check var declared, so we can use it.
        for scope in range(len(self.scope_stack) - 1, -1, -1):
            if identifier in self.scope_stack[scope]:
                return
        self.error(f'Variable {identifier} has not been declared in the current or any enclosing scopes')


    # return false when types mismatch, otherwise ret true
    # def checkTypeMatch(self, vType, eType, var, exp):
    def checkTypeMatch(self, vType, eType):
        if((vType == 'int' and eType == 'number') or (vType == 'float' and eType == 'fnumber')):
            return True
        self.error(f'Type Mismatch between {vType} and {eType}')

    # # return its type or None if not found
    # def getMyType(self, identifier):
      
    # move to the next token.
    def advance(self):
        self.current_token = self.next_token
        self.next_token = self.lexer.get_token()

    def parse_program(self):
        self.enter_scope() # enter the scope of the global program
        self.advance()
        statements = []
        while self.current_token != None:
            statements.append(self.parse_statement())
            self.advance()
        return ProgramNode(statements)

    def parse_statement(self):
        if(self.current_token[1] == "if"):
            return self.parse_if_statement()
        elif(self.current_token[1] == "while"):
            return self.parse_while_loop()
        elif(self.current_token[1] == "int" or self.current_token[1] == "float"):
            return self.parse_declaration()
        else:
            return self.parse_assignment()

    # call checkVarDeclared.
    def parse_declaration(self):
        type = self.current_token[0] # set the type to int or float
        self.advance() # advance to identifier
        identifier = self.current_token[0] # set the identifier to the variable name
        self.advance() # advance to '='
        self.advance() # advance to first term of the arithmetic_expression
        expression = self.parse_arithmetic_expression() # set expression to arithmetic_expression

        # check if variable was already declared
        self.checkVarDeclared(identifier)

        # append varName: type to current scopes dictionary
        self.scope_stack[-1][identifier] = type

        # check if types match
        self.checkTypeMatch(type, expression.type)
        return DeclarationNode(identifier, expression, type)

    def parse_assignment(self):
        identifier = self.current_token[0] # set the identifier to the variable name
        self.advance() # advance to '='
        self.advance() # advance to first term of the arithmetic_expression
        expression = self.parse_arithmetic_expression() # set expression to arithmetic_expression
        return AssignmentNode(identifier, expression)

    def parse_if_statement(self):
        if_block = []
        else_block = []
        self.advance() # advance past the 'if'
        condition = self.parse_condition()
        self.advance() # advance to the 'then'
        self.advance() # advance past the 'then'
        self.advance() # advance past the '{'
        self.enter_scope() # enter the scope of the if block
        while(self.current_token[0] != '}'):
            if_block.append(self.parse_statement())
            self.advance() # advance to next statement
        self.leave_scope() # leave the scope of the if block
        
        self.enter_scope() # enter the scope of the else block
        if(self.next_token and self.next_token[1] == "else"):
            self.advance() # advance past the '}' to the "else"
            self.advance() # advance past the "else"
            self.advance() # advance past the '{'
            while(self.current_token[0] != '}'):
                else_block.append(self.parse_statement())
                self.advance() # advance to next statement
        self.leave_scope() # leave the scope of the else block
        return IfStatementNode(condition, if_block, else_block)

    def parse_while_loop(self):
        loop_block = []
        self.advance() # advance past the 'while'
        condition = self.parse_condition()
        self.advance() # advance to the 'do'
        self.advance() # advance past the 'do'
        self.advance() # advance past the '{'
        self.enter_scope() # enter the scope of the while loop
        while(self.current_token[0] != '}'):
            loop_block.append(self.parse_statement())
            self.advance() # advance to next statement
        self.leave_scope() # leave the scope of the while loop
        return WhileLoopNode(condition, loop_block)
    
    # No need to check type mismatch here.
    def parse_condition(self):
        left = self.parse_arithmetic_expression() # set LHS arithmetic expression
        self.advance() # advance to comparison token
        operator = self.current_token[0] # set operator to comparison token
        self.advance() # advance to RHS arithmetic expression
        right = self.parse_arithmetic_expression() # set RHS arithmetic expression
        return ConditionNode(left, operator, right)

    def parse_arithmetic_expression(self):
        left = self.parse_term() # set left to be equal to the LHS term
        left_type = self.current_token[1]
        if(self.next_token and self.next_token[1] == "op" and (self.next_token[0] == "+" or self.next_token[0] == "-")):
            self.advance()
            operator = self.current_token[0] # set operator to be the operator
            self.advance()
            right = self.parse_term() # set right to be the RHS term
            right_type = self.current_token[1]
            if(left_type == right_type):
                return ArithmeticExpressionNode(operator, left, right, left_type)
            return ArithmeticExpressionNode(operator, left, right, None)
        else:
            # return ArithmeticExpressionNode("None", left, "None", left_type)
            return left

    # call checkVarUse
    def parse_term(self):
        left = self.parse_factor() # set left to be equal to the LHS factor
        left_type = self.current_token[1]
        if(self.next_token and self.next_token[1] == "op" and (self.next_token[0] == "*" or self.next_token[0] == "/")):
            self.advance()
            operator = self.current_token[0] # set operator to be the operator
            self.advance()
            right = self.parse_factor() # set right to be the RHS factor
            right_type = self.current_token[1]
            if(left_type == right_type):
                return TermNode(operator, left, right, left_type)
            return TermNode(operator, left, right, None)
        else:
            # return TermNode("None", left, "None", left_type)
            return left

    # call checkVarUse
    def parse_factor(self):
        if(self.current_token[1] == "number" or self.current_token[1] == "fnumber"):
            return FactorNode(self.current_token[0], self.current_token[1]) # return number or fnumber as a node
        elif(self.current_token[1] == "variable"):
            self.checkVarUse(self.current_token[0])
            return FactorNode(self.current_token[0], self.current_token[1]) # return variable as a node
        else:
            self.advance() # skip the '('
            expression = self.parse_arithmetic_expression()
            self.advance() # skip the ')'
            return expression
