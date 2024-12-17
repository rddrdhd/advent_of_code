# Task: https://adventofcode.com/2024/day/17
f = open('y2024/data/day17.txt', 'r')
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]


def parse_input(input_str):
    registers, program = input_str.split("\n\n")
    rA, rB, rC = registers.splitlines()
    return (
        int(rA.split(": ")[1]),
        int(rB.split(": ")[1]),
        int(rC.split(": ")[1]),
        [int(x) for x in program.removeprefix("Program: ").split(",")],
    )


class Computer:
    def __init__(self, rA, rB, rC, program):
        self.a = rA
        self.b = rB
        self.c = rC
        self.program = program
        self.output = []
        self.ptr = 0

        self.operations = {
            0: self.adv,
            1: self.blx,
            2: self.bst,
            3: self.jnz,
            4: self.bcx,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def operand_value(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c

    def divide(self, operand):
        return self.a // (2 ** self.operand_value(operand))

    def adv(self, operand):
        self.a = self.divide(operand)
        self.ptr += 2

    def blx(self, operand):
        self.b ^= operand
        self.ptr += 2

    def bst(self, operand):
        self.b = self.operand_value(operand) % 8
        self.ptr += 2

    def jnz(self, operand):
        if self.a != 0 and self.ptr != operand:
            self.ptr = operand
        else:
            self.ptr += 2

    def bcx(self, _):
        self.b ^= self.c
        self.ptr += 2

    def out(self, operand):
        self.output.append(self.operand_value(operand) % 8)
        self.ptr += 2

    def bdv(self, operand):
        self.b = self.divide(operand)
        self.ptr += 2

    def cdv(self, operand):
        self.c = self.divide(operand)
        self.ptr += 2

    def compute(self, opcode, operand):
        self.operations[opcode](operand)

    def run(self):
        while self.ptr < len(self.program):
            opcode = self.program[self.ptr]
            operand = self.program[self.ptr + 1]
            self.compute(opcode, operand)
        return self.output


def compute_output(rA, rB, rC, program):
    return Computer(rA, rB, rC, program).run()


def find_reg_a(rB, rC, program):
    candidates = [0]
    for length in range(1, len(program) + 1):
        prev_candidates = candidates
        candidates = []
        for current_candidate in prev_candidates:
            for digit in range(8):
                rA = 8 * current_candidate + digit
                output = compute_output(rA, rB, rC, program)
                if output == program[-length:]:
                    candidates.append(rA)
    return min(candidates)


def part1():
    rA, rB, rC, program = parse_input("\n".join(lines))
    output = compute_output(rA, rB, rC, program)
    return ",".join(map(str, output))


def part2():
    _, rB, rC, program = parse_input("\n".join(lines))
    return find_reg_a(rB, rC, program)


if __name__ == "__main__":
    print("P1", part1())  # 1,5,7,4,1,6,0,3,0
    print("P2", part2())  # 108107574778365
