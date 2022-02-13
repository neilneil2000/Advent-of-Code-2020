from dataclasses import dataclass
from typing import List, Set


@dataclass
class Instruction:
    operation: str
    value: int


class InstructionOverRunError(Exception):
    pass


class InfiniteLoopError(Exception):
    pass


class BootLoader:
    """Class Representing a Bootloader and it's code"""  #

    def __init__(self, text_instructions: List[str]) -> None:
        self.instructions = []  # List[Instruction]
        self.accumulator = 0
        self.executed_instructions = set()
        self.instruction_pointer = 0
        self.corrupted_instruction = None
        self.confirmed_correct = set()
        for text_instruction in text_instructions:
            self.parse_instruction(text_instruction)

    def parse_instruction(self, text_instruction: str) -> None:
        operation, value = text_instruction.split(" ")
        self.instructions.append(Instruction(operation, int(value)))

    def run_til_end(self):
        while True:
            try:
                self.execute_instruction(True)
            except InfiniteLoopError:
                self.confirmed_correct.add(self.corrupted_instruction)
                self.reset_cpu()
            except InstructionOverRunError:
                break

    def run_til_loop(self):
        while True:
            try:
                self.execute_instruction()
            except InfiniteLoopError:
                break

    def execute_instruction(self, fix_corruption=False):

        if self.instruction_pointer >= len(self.instructions):
            raise InstructionOverRunError

        if self.instruction_pointer in self.executed_instructions:
            raise InfiniteLoopError

        self.executed_instructions.add(self.instruction_pointer)
        instruction = self.instructions[self.instruction_pointer]

        if instruction.operation == "acc":
            self.accumulator += instruction.value
            self.instruction_pointer += 1
            return

        if (
            fix_corruption
            and self.corrupted_instruction is None
            and self.instruction_pointer not in self.confirmed_correct
        ):
            self.corrupted_instruction = self.instruction_pointer
            if instruction.operation == "jmp":
                instruction = Instruction("nop", instruction.value)
            else:
                instruction = Instruction("jmp", instruction.value)

        if instruction.operation == "jmp":
            self.instruction_pointer += instruction.value
            return

        self.instruction_pointer += 1
        return

    def reset_cpu(self):
        self.accumulator = 0
        self.executed_instructions = set()
        self.instruction_pointer = 0
        self.corrupted_instruction = None
