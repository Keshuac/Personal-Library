print("Input Number:")
NumberInput = int(input())
print("\nBinary: " + format(NumberInput, '08b'))
#Number Input

Temp = NumberInput >>7
MSB = bin(NumberInput)[2]
print("MSB is " + MSB)
#Retrieving the MSB

print("\nInput Shift Amount:")
ShiftBy = int(input())
#Input the shift amount


BinaryShifted = NumberInput>>1
ShiftBy= ShiftBy-1
if int(MSB) == 1:
   BinaryShifted = BinaryShifted | 128

while ShiftBy != 0:

    BinaryShifted = BinaryShifted>>1
    if int(MSB) == 1:
        BinaryShifted = BinaryShifted | 128
    ShiftBy = ShiftBy - 1
   

print("\n"+format(BinaryShifted, '08b'))
ProgramEnd = input()

#Shifted
