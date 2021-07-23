import os
import datetime

def logToTxtFile(input):
	content = f'{str(datetime.datetime.now()).replace(" ", "T")} | {input}'
	directory = str(os.path.realpath(__file__)).replace(".py", ".txt")
	os.system(f'echo "{content}" >> {directory}')

def logToTxtFile(input, directory):
	content = f'{str(datetime.datetime.now()).replace(" ", "T")} | {input}'
	os.system(f'echo "{content}" >> {directory}')
