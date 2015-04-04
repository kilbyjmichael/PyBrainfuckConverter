#!/usr/bin/python
'''
Assumes correct Brainfuck formatting. Also, still broken.
'''

py_file = open("bf_to_.py", 'w')

def inc_ptr(level):
    return indent("ptr += 1", level)
    
def dec_ptr(level):
    return indent("ptr -= 1", level)
    
def inc_bte(level):
    return indent("tape[ptr] += 1", level)

def dec_bte(level):
    return indent("tape[ptr] -= 1", level)

def out_ptr(level):
    return indent("print(chr(tape[ptr]))", level)

def inp_usr(level):
    return indent("tape[ptr] = ord(input())", level)

def jmp_for(level):
    global indent_level
    indent_level += 2
    return indent("if tape[ptr] != 0:\n\twhile tape[ptr] != 0:", level)

def jmp_bck(level):
    global indent_level
    indent_level -= 2
    return indent("break", level)

indent_level = 0

def indent(line, level = indent_level):
    return "\t" * level + line + "\n"

bf_commands = {#tes commands
                '>' : inc_ptr,
                '<' : dec_ptr,
                '+' : inc_bte,
                '-' : dec_bte,
                '.' : out_ptr,
                ',' : inp_usr,
                '[' : jmp_for,
                ']' : jmp_bck,
}

def write_py(bf_code):
    global indent_level
    py_file.write("#!/usr/bin/python\n\n")
    py_file.write("ptr = 0\n")
    py_file.write("tape = [0] * 30000\n\n")
    py_file.write("def bf_to_py(ptr):\n")
    indent_level += 1 #indent after def
    convert_bf(bf_code)
    py_file.write("\ndef main():\n")
    py_file.write("\tbf_to_py(ptr)\n\n")
    py_file.write("if __name__ == \"__main__\": main()")
    py_file.close()
    return "written to bf_to_.py"

def convert_bf(bf_code):
    for char in bf_code:
        py_file.write(bf_commands[char](indent_level))
    return

def main():
    print(write_py(input("Enter valid Brainfuck code -> ")))

if __name__ == "__main__": main()
        
