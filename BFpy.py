#!/usr/bin/python
'''
Assumes correct Brainfuck formatting. Also, still broken.
'''
py_code = [""]

py_file = open("bf_to_.py", 'w')

def inc_ptr():
    return "\tptr += 1\n"
    
def dec_ptr():
    return "\tptr -= 1\n"
    
def inc_bte():
    return "\ttape[ptr] += 1\n"

def dec_bte():
    return "\ttape[ptr] -= 1\n"

def out_ptr():
    return "\tprint(chr(tape[ptr]))\n"

def inp_usr():
    return "\ttape[ptr] = ord(input())\n"

def jmp_for():
    return "\twhile tape[ptr] != 0:\n\t"

def jmp_bck():
    return "#figure me out ]"

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
    py_file.write("#!/usr/bin/python\n\n")
    py_file.write("ptr = 0\n")
    py_file.write("tape = [0] * 30000\n\n")
    py_file.write("def bf_to_py():\n")
    convert_bf(bf_code)
    py_file.write("\ndef main():\n")
    py_file.write("\tbf_to_py()\n\n")
    py_file.write("if __name__ == \"__main__\": main()")
    py_file.close()
    return "written to bf_to_.py"

def convert_bf(bf_code):
    for char in bf_code:
        py_file.write(bf_commands[char]())
    return

def main():
    print(write_py(input("Enter valid Brainfuck code -> ")))

if __name__ == "__main__": main()
        
