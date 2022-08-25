import time

print('DLang compiler')

inputFile = "MusicBot.dragonlang"
outputFile = "MusicBot.py"

lineNum = 0
errorsNum = 0

def checkLine(lineNum, outputLine):
	global errorsNum
	if 'print' in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1
	if 'import' in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1
	if 'def' in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1
	if 'input' in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1
	if "f'" in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1
	if 'f"' in outputLine:
		if outputLine.startswith("__"): pass
		else:
			print(f'[ERROR] Compile error!')
			print(f'[ERROR] Line: {lineNum}')
			print(f'[ERROR] Unknown word: {outputLine}')
			errorsNum = errorsNum + 1

try:
	with open(inputFile, "r") as inputF:
		with open(outputFile, "w") as output:
			for line in inputF:
				#time.sleep(0.1)
				lineNum = lineNum + 1
				print(f'[{lineNum}] INPUT: {line}')

				outputLine = line.replace("moduse", "import").replace("Console.Output", "print").replace("func", "def").replace("Console.Input", "input").replace("()", ":").replace("<", "(").replace(">", ")").replace("__", "#").replace("FTEXT", "f").replace("?VL", "{").replace("VR?", "}").replace("ML_", '"""').replace("_ML", '"""')

				checkLine(lineNum, line)

				output.write(outputLine)
except Exception as errExc:
	print(f'[ERROR] Compile error!')
	print(f'[ERROR] Line: {lineNum}')
	print(f'[ERROR] Error: {errExc}')
	errorsNum = errorsNum + 1
	#import ExitFromDLangCompiler

if errorsNum >= 1:
	print('Compile was completed with errors!')
	print(f'Lines of code: {lineNum}')
	print(f'Errors: {errorsNum}')
else:
	print()
	print('Compile done without errors!')
	print(f'Lines of code: {lineNum}')
	print(f'Errors: {errorsNum}')
	print()

	#import os
	#os.system("python dragonlangtest.py")