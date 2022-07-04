#!/usr/bin/python3

import re
import cmath
import sys
import argparse 

"""
   below are definned 2 custom excceptions
"""
class Error(Exception):
    pass

class ExtraParametersError(Error):
    pass

class TooFewParametersError(Error):
    pass

"""
    the below function is responsible for getting filename from command line
"""
def arg_parse_foo():
    linear_parse=argparse.ArgumentParser(description="this script takes a file\
            as an argument from command line in which in ideal shold be an\
            quadric  equation and creates another file containing the solution\
            of the given equation and as a feedback compares the got solution\
            with right solution")
    linear_parse.add_argument('-f', "--file", required = True)
    arguments = linear_parse.parse_args()
    return arguments.file

"""
    the below function is responsible for reading content from file input from command line
"""
def read_from_file():
    try:
        with open(arg_parse_foo()) as my_file:
            equat_str = my_file.read()
        equat_str = equat_str.split("\n")[0]
        return equat_str
    except :
        print("File not exist")
        sys.exit()

"""
    the below function is responsible for getting content of file as string and returning abc as float array
"""
def get_abc(abc_str):
    abc = abc_str.split()
    try:
        for each in abc:
            try:
                float(each)
            except ValueError:
                print(f"\"{each}\" from input file is not convertable to float")
                sys.exit()
        if 3 < len(abc):
            raise ExtraParametersError
        elif 3 > len(abc):
            raise TooFewParametersError
    except ExtraParametersError:
            print("extra parameters got from input file\n")
            sys.exit()
    except TooFewParametersError:
            print("too few parameters got from input file\n")
            sys.exit()
    return float(abc[0]), float(abc[1]), float(abc[2])

"""
    the below function is responsible for getting abc as float array and returns roots also as float array
"""
def solve_quad_equation(abc):
    try:
        if 0 == abc[0]:
            if 0 == ab[1]:
                if 0 != ab[1]:
                    raise ZeroDivisionError
                else:
                    print("the got parameters suit for identity\n")
                    print("interrupt the execution. No output file will be generated\n")
                    sys.exit()
    except TypeError:
        print ("input file is not correct")
        sys.exit()
    except ZeroDivisionError:
        print("a and b are zero while while c is not zero\n")
        sys.exit()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    dis = (b**2) - (4 * a*c)
    ans1 = (-b-cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)
    return ans1.real, ans2.real 

"""
    the below function is responsible for getting roots compareing them with those in golden.txt
    and returns true or false according to result
"""
def test(x_1, x_2):
    try:
        with open("golden.txt") as golden_num_f:
            golden_num_str = golden_num_f.read()
        golds = golden_num_str.split()
        if (x_1 == float(golds[0]) and x_1 == float(golds[1])) or \
                        (x_2 == float(golds[0]) and x_2 == float(golds[1])):
            return True
        else:
            return False
    except IOError:
        print("Golden file not exist")
        sys.exit()

"""
    the below function is responsible for getting roots cnd test_result
    generating output.txt containing the result and feedback
"""
def create_output_file(roots, is_right):
    roots_str = str(roots[0]) + ' ' + str(roots[1])
    if is_right:
        roots_str += '   Right solution\n'
    else:
        roots_str += '   wrong solution\n'
    with open('output.txt', 'w') as output_f:
        output_f.write(roots_str)

def main():
    try:
        abc_str = read_from_file()
        abc = get_abc(abc_str)
        roots = solve_quad_equation(abc)
        create_output_file(roots, test(roots[0], roots[1]))
    except TypeError:
        print("File arguments are not correct ")


if __name__ == '__main__':
    main()
