import sys

# Lets run this py script like:
# sudo python3.7 pythotevDemoRunPythonScriptWithArgs.py ThisIsArg1 5

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg2MultipliedByTwo = 2 * int(arg2)

print(f'First argument passed to the execution of this python script was {arg1}.')
print(f'Second argument passed to the execution of this python script was {arg2}. {arg2} multiplied by 2 is {arg2MultipliedByTwo}.')
