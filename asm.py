import sys

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
else:
    print("No command line argument prodided, usage: " + sys.argv[1] + " <assmbly-term>")
    print("An assembly-term can be a register or an instruction (like 'mov', but not 'mov eax, eax'. Or 'eax' itself)")
    exit()
instruction_db = {
    "mov": {
        "description": "Move: Copies the value from one location to another.",
        "example": "Example: mov eax, ebx",
        "example_description": "Example Description: This instruction moves the value in the ebx register to the eax register.",
    },
    "push": {
        "description": "Push: Pushes a value onto the top of the stack.",
        "example": "Example: push eax",
        "example_description": "Example Description: This instruction pushes the value in the eax register onto the stack.",
    },
    "pop": {
        "description": "Pop: Removes the value from the top of the stack and stores it in a destination.",
        "example": "Example: pop ebx",
        "example_description": "Example Description: This instruction pops the value from the top of the stack and stores it in the ebx register.",
    },
    "lea": {
        "description": "Load effective address: Calculates the effective address of a memory operand and stores it in a register.",
        "example": "Example: lea edx, [eax+ebx*2]",
        "example_description": "Example Description: This instruction calculates the effective address of the memory operand [eax+ebx*2] and stores it in the edx register.",
    },
    "xchg": {
        "description": "Exchange: Swaps the contents of two operands.",
        "example": "Example: xchg eax, ebx",
        "example_description": "Example Description: This instruction exchanges the values in the eax and ebx registers.",
    },
    "add": {
        "description": "Add: Adds two operands and stores the result in a destination.",
        "example": "Example: add eax, ebx",
        "example_description": "Example Description: This instruction adds the values in the eax and ebx registers and stores the result in eax.",
    },
    "sub": {
        "description": "Subtract: Subtracts one operand from another and stores the result in a destination.",
        "example": "Example: sub ecx, edx",
        "example_description": "Example Description: This instruction subtracts the value in the edx register from the value in the ecx register and stores the result in ecx.",
    },
    "inc": {
        "description": "Increment: Increments the value of an operand by one.",
        "example": "Example: inc eax",
        "example_description": "Example Description: This instruction increments the value in the eax register by one.",
    },
    "dec": {
        "description": "Decrement: Decrements the value of an operand by one.",
        "example": "Example: dec ebx",
        "example_description": "Example Description: This instruction decrements the value in the ebx register by one.",
    },
    "mul": {
        "description": "Multiply: Multiplies two operands and stores the result in a destination.",
        "example": "Example: mul ebx",
        "example_description": "Example Description: This instruction multiplies the value in the ebx register with the value in the accumulator register and stores the result in the product register.",
    },
    "imul": {
        "description": "Signed multiply: Multiplies two signed operands and stores the result in a destination.",
        "example": "Example: imul ecx, 2",
        "example_description": "Example Description: This instruction multiplies the value in the ecx register by 2 and stores the signed result in the ecx register.",
    },
    "div": {
        "description": "Divide: Divides the value in the dividend register by an operand and stores the quotient in the quotient register and the remainder in the remainder register.",
        "example": "Example: div ebx",
        "example_description": "Example Description: This instruction divides the value in the accumulator register by the value in the ebx register, storing the quotient in the accumulator register and the remainder in the edx register.",
    },
    "idiv": {
        "description": "Signed divide: Divides the value in the dividend register by a signed operand and stores the quotient in the quotient register and the remainder in the remainder register.",
        "example": "Example: idiv ecx",
        "example_description": "Example Description: This instruction divides the value in the accumulator register by the signed value in the ecx register, storing the quotient in the accumulator register and the remainder in the edx register.",
    },
    "and": {
        "description": "Logical AND: Performs a bitwise AND operation between two operands and stores the result in a destination.",
        "example": "Example: and eax, ebx",
        "example_description": "Example Description: This instruction performs a bitwise AND operation between the values in the eax and ebx registers and stores the result in the eax register.",
    },
    "or": {
        "description": "Logical OR: Performs a bitwise OR operation between two operands and stores the result in a destination.",
        "example": "Example: or eax, ebx",
        "example_description": "Example Description: This instruction performs a bitwise OR operation between the values in the eax and ebx registers and stores the result in the eax register.",
    },
    "xor": {
        "description": "Logical XOR: Performs a bitwise XOR operation between two operands and stores the result in a destination.",
        "example": "Example: xor eax, ebx",
        "example_description": "Example Description: This instruction performs a bitwise XOR operation between the values in the eax and ebx registers and stores the result in the eax register.",
    },
    "not": {
        "description": "Logical NOT: Performs a bitwise NOT operation on an operand and stores the result in a destination.",
        "example": "Example: not eax",
        "example_description": "Example Description: This instruction performs a bitwise NOT operation on the value in the eax register and stores the result in the eax register.",
    },
    "shl": {
        "description": "Shift left: Shifts the bits of an operand to the left by a specified number of positions.",
        "example": "Example: shl eax, 2",
        "example_description": "Example Description: This instruction shifts the bits of the eax register to the left by 2 positions.",
    },
    "shr": {
        "description": "Shift right: Shifts the bits of an operand to the right by a specified number of positions.",
        "example": "Example: shr ecx, 1",
        "example_description": "Example Description: This instruction shifts the bits of the ecx register to the right by 1 position.",
    },
    "jmp": {
        "description": "Unconditional jump: Jumps to a specified location unconditionally.",
        "example": "Example: jmp label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label unconditionally.",
    },
    "je": {
        "description": "Jump if equal: Jumps to a specified location if the previous comparison was equal.",
        "example": "Example: je label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was equal.",
    },
    "jne": {
        "description": "Jump if not equal: Jumps to a specified location if the previous comparison was not equal.",
        "example": "Example: jne label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was not equal.",
    },
    "jz": {
        "description": "Jump if zero: Jumps to a specified location if the previous result was zero.",
        "example": "Example: jz label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous result was zero.",
    },
    "jnz": {
        "description": "Jump if not zero: Jumps to a specified location if the previous result was not zero.",
        "example": "Example: jnz label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous result was not zero.",
    },
    "jc": {
        "description": "Jump if carry: Jumps to a specified location if the previous arithmetic operation generated a carry.",
        "example": "Example: jc label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous arithmetic operation generated a carry.",
    },
    "jnc": {
        "description": "Jump if not carry: Jumps to a specified location if the previous arithmetic operation did not generate a carry.",
        "example": "Example: jnc label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous arithmetic operation did not generate a carry.",
    },
    "ja": {
        "description": "Jump if above: Jumps to a specified location if the previous comparison was above (unsigned).",
        "example": "Example: ja label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was above (unsigned).",
    },
    "jae": {
        "description": "Jump if above or equal: Jumps to a specified location if the previous comparison was above or equal (unsigned).",
        "example": "Example: jae label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was above or equal (unsigned).",
    },
    "jb": {
        "description": "Jump if below: Jumps to a specified location if the previous comparison was below (unsigned).",
        "example": "Example: jb label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was below (unsigned).",
    },
    "jbe": {
        "description": "Jump if below or equal: Jumps to a specified location if the previous comparison was below or equal (unsigned).",
        "example": "Example: jbe label",
        "example_description": "Example Description: This instruction jumps to the location specified by the label if the previous comparison was below or equal (unsigned).",
    },
    "call": {
        "description": "Call procedure: Calls a procedure at a specified location.",
        "example": "Example: call subroutine",
        "example_description": "Example Description: This instruction calls the subroutine located at the specified label.",
    },
    "ret": {
        "description": "Return from procedure: Returns from a called procedure.",
        "example": "Example: ret",
        "example_description": "Example Description: This instruction returns from a called procedure.",
    },
    "cmps": {
        "description": "Compare string: Compares two strings byte by byte.",
        "example": "Example: cmps byte ptr [esi], byte ptr [edi]",
        "example_description": "Example Description: This instruction compares the byte at the memory location pointed to by the esi register with the byte at the memory location pointed to by the edi register.",
    },
    "scas": {
        "description": "Scan string: Compares a string in memory with a byte in the accumulator.",
        "example": "Example: scasb",
        "example_description": "Example Description: This instruction compares the byte in the accumulator register with the byte at the memory location pointed to by the edi register.",
    },
    "lods": {
        "description": "Load string: Loads a string element into a register and advances the pointer.",
        "example": "Example: lodsb",
        "example_description": "Example Description: This instruction loads the byte at the memory location pointed to by the esi register into the accumulator register and advances the esi register.",
    },
    "stos": {
        "description": "Store string: Stores a string element from a register into memory and advances the pointer.",
        "example": "Example: stosb",
        "example_description": "Example Description: This instruction stores the byte in the accumulator register into the memory location pointed to by the edi register and advances the edi register.",
    },
    "int": {
        "description": "Interrupt: Triggers a software interrupt.",
        "example": "Example: int 0x80",
        "example_description": "Example Description: This instruction triggers a software interrupt with interrupt number 0x80.",
    },
    "iret": {
        "description": "Interrupt return: Returns from an interrupt handler.",
        "example": "Example: iret",
        "example_description": "Example Description: This instruction returns from an interrupt handler.",
    },
    "cli": {
        "description": "Clear interrupt flag: Disables interrupts.",
        "example": "Example: cli",
        "example_description": "Example Description: This instruction disables interrupts by clearing the interrupt flag.",
    },
    "sti": {
        "description": "Set interrupt flag: Enables interrupts.",
        "example": "Example: sti",
        "example_description": "Example Description: This instruction enables interrupts by setting the interrupt flag.",
    },
    "hlt": {
        "description": "Halt: Halts the processor until an interrupt occurs.",
        "example": "Example: hlt",
        "example_description": "Example Description: This instruction halts the processor until an interrupt occurs.",
    },
    "nop": {
        "description": "No operation: Performs no operation.",
        "example": "Example: nop",
        "example_description": "Example Description: This instruction performs no operation.",
    },
}
register_db = {
    # x86 32-bit registers
    "eax": {
        "description": "Accumulator register: Used for arithmetic, logical, and data operations.",
        "size": "32 bits",
    },
    "ebx": {
        "description": "Base register: Used as a base pointer for memory access.",
        "size": "32 bits",
    },
    "ecx": {
        "description": "Counter register: Used for loop and string operations.",
        "size": "32 bits",
    },
    "edx": {
        "description": "Data register: Used for arithmetic, logical, and data operations.",
        "size": "32 bits",
    },
    "esi": {
        "description": "Source index register: Used as a source index for string operations.",
        "size": "32 bits",
    },
    "edi": {
        "description": "Destination index register: Used as a destination index for string operations.",
        "size": "32 bits",
    },
    "ebp": {
        "description": "Base pointer register: Used for referencing function parameters and local variables.",
        "size": "32 bits",
    },
    "esp": {
        "description": "Stack pointer register: Points to the top of the stack.",
        "size": "32 bits",
    },
    "eip": {
        "description": "Instruction pointer register: Holds the memory address of the next instruction to be executed.",
        "size": "32 bits",
    },
    # x64 64-bit registers
    "rax": {
        "description": "Accumulator register: Used for arithmetic, logical, and data operations.",
        "size": "64 bits",
    },
    "rbx": {
        "description": "Base register: Used as a base pointer for memory access.",
        "size": "64 bits",
    },
    "rcx": {
        "description": "Counter register: Used for loop and string operations.",
        "size": "64 bits",
    },
    "rdx": {
        "description": "Data register: Used for arithmetic, logical, and data operations.",
        "size": "64 bits",
    },
    "rsi": {
        "description": "Source index register: Used as a source index for string operations.",
        "size": "64 bits",
    },
    "rdi": {
        "description": "Destination index register: Used as a destination index for string operations.",
        "size": "64 bits",
    },
    "rbp": {
        "description": "Base pointer register: Used for referencing function parameters and local variables.",
        "size": "64 bits",
    },
    "rsp": {
        "description": "Stack pointer register: Points to the top of the stack.",
        "size": "64 bits",
    },
    "rip": {
        "description": "Instruction pointer register: Holds the memory address of the next instruction to be executed.",
        "size": "64 bits",
    },
    # xmm registers (for floating-point operations)
    "xmm0": {
        "description": "XMM register 0: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm1": {
        "description": "XMM register 1: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm2": {
        "description": "XMM register 2: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm3": {
        "description": "XMM register 3: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm4": {
        "description": "XMM register 4: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm5": {
        "description": "XMM register 5: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm6": {
        "description": "XMM register 6: Used for floating-point operations.",
        "size": "128 bits",
    },
    "xmm7": {
        "description": "XMM register 7: Used for floating-point operations.",
        "size": "128 bits",
    },
    # Additional registers and their descriptions can be added here
}

if (1):
    instruction = arg1
    
    if instruction in instruction_db:
        description = instruction_db[instruction]["description"]
        example = instruction_db[instruction]["example"]
        example_description = instruction_db[instruction]["example_description"]
        print()
        print(description)
        print(example)
        print(example_description)
        print()
    elif instruction in register_db:
        description = register_db[instruction]["description"]
        size = register_db[instruction]["size"]
        print()
        print(description)
        print("Size:", size)
        print()
    elif instruction == "exit":
        exit()
    else:
        print("Instruction or register not found in the database.")
