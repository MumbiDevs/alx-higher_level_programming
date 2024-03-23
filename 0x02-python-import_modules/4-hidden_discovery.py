#!/usr/bin/python3.8
import dis

if __name__ == "__main__":
    # Load the bytecode from the compiled module
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()

    # Disassemble the bytecode
    instructions = dis.get_instructions(bytecode)

    # Extract the names of functions and variables that don't start with '__'
    names = {instr.argval for instr in instructions if isinstance(instr.argval, str) and not instr.argval.startswith("__")}

    # Sort the names alphabetically and print them
    for name in sorted(names):
        print(name)
