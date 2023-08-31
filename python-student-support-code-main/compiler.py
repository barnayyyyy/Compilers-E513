import ast
from ast import *
from utils import *
from x86_ast import *
import os
from typing import List, Tuple, Set, Dict

Binding = Tuple[Name, expr]
Temporaries = List[Binding]

class Compiler:

    ############################################################################
    # Remove Complex Operands
    ############################################################################

    # Exercise 2.1
    def rco_exp(self, e: expr, need_atomic: bool) -> Tuple[expr, Temporaries]:
            # YOUR CODE HERE
            match (e):
                case Constant(n=n) if need_atomic == False:
                    return Constant(n), []  # Constants are already atomic
                case UnaryOp(op=USub(), operand=Constant(n=n)) if need_atomic == False:
                    return Constant(-n), []  # UnaryOp with constant operand is atomic
                case BinOp(left=left, op=Add(), right=right) if isinstance(left, Constant) and isinstance(right, Constant) and need_atomic == False:
                    return Constant(left.n + right.n), []  # BinOp with constant operands is atomic
                case BinOp(left=left, op=Sub(), right=right) if isinstance(left, Constant) and isinstance(right, Constant) and need_atomic == False:
                    return Constant(left.n - right.n), []  # BinOp with constant operands is atomic
                case BinOp(left=left, op=op, right=right) if need_atomic == True:
                    # Create temporary variables for complex operands
                    temp_left, temp_bindings_left = self.rco_exp(left, need_atomic=False)
                    temp_right, temp_bindings_right = self.rco_exp(right, need_atomic=False)
                    
                    # Create a new temporary name
                    temp_name = Name('tmp')
                    
                    # Combine the temporary bindings and add the new temporary binding
                    all_temp_bindings = temp_bindings_left + temp_bindings_right + [(temp_name, BinOp(temp_left, op, temp_right))]
                    return temp_name, all_temp_bindings

                case Name(var=var) if need_atomic == False:
                    return e, []  # Names are already atomic

                case _:
                    # For unsupported cases, create a new temporary variable and return it
                    temp_name = Name('tmp')
                    return temp_name, [(temp_name, e)]

    def rco_stmt(self, s: stmt) -> List[stmt]:
        # YOUR CODE HERE
        match (s):
            case Expr(value=e):
                # For Expr statements, simplify the expression inside it
                simplified_expr = self.rco_exp(e, need_atomic=False)
                return [Expr(simplified_expr)]
            case Assign(targets=targets, value=e):
                # For Assign statements, simplify the right-hand side expression
                simplified_rhs = self.rco_exp(e, need_atomic=False)
                return [Assign(targets=targets, value=simplified_rhs)]
            case _:
                # For other types of statements, return them as-is
                return [s]

    # def remove_complex_operands(self, p: Module) -> Module:
    #     # YOUR CODE HERE
    #     raise Exception('remove_complex_operands not implemented')
        
    ############################################################################
    # Select Instructions
    ############################################################################

    def select_arg(self, e: expr) -> arg:
        # YOUR CODE HERE
        pass        

    def select_stmt(self, s: stmt) -> List[instr]:
        # YOUR CODE HERE
        pass        

    # def select_instructions(self, p: Module) -> X86Program:
    #     # YOUR CODE HERE
    #     pass        

    ############################################################################
    # Assign Homes
    ############################################################################

    def assign_homes_arg(self, a: arg, home: Dict[Variable, arg]) -> arg:
        # YOUR CODE HERE
        pass        

    def assign_homes_instr(self, i: instr,
                           home: Dict[Variable, arg]) -> instr:
        # YOUR CODE HERE
        pass        

    def assign_homes_instrs(self, ss: List[instr],
                            home: Dict[Variable, arg]) -> List[instr]:
        # YOUR CODE HERE
        pass        

    # def assign_homes(self, p: X86Program) -> X86Program:
    #     # YOUR CODE HERE
    #     pass        

    ############################################################################
    # Patch Instructions
    ############################################################################

    def patch_instr(self, i: instr) -> List[instr]:
        # YOUR CODE HERE
        pass        

    def patch_instrs(self, ss: List[instr]) -> List[instr]:
        # YOUR CODE HERE
        pass        

    # def patch_instructions(self, p: X86Program) -> X86Program:
    #     # YOUR CODE HERE
    #     pass        

    ############################################################################
    # Prelude & Conclusion
    ############################################################################

    # def prelude_and_conclusion(self, p: X86Program) -> X86Program:
    #     # YOUR CODE HERE
    #     pass        