import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

print(printer.printString("Hello World!"))
print("Soma:", printer.soma(2, 3))
print("Quantidade de caracteres:", printer.countChars("Hello World!"))
