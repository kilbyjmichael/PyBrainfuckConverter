#!/usr/bin/python

ptr = 0
tape = [0] * 30000

def bf_to_py(ptr):
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	ptr += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	ptr += 1
	tape[ptr] = ord(input())
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	tape[ptr] += 1
	print(chr(tape[ptr]))
	ptr -= 1
	print(chr(tape[ptr]))
	ptr -= 1
	print(chr(tape[ptr]))

def main():
	bf_to_py(ptr)

if __name__ == "__main__": main()