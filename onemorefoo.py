from foo import *

try:
    arg = int(input('Введіть ціле число, що буде кількістю ітерацій в циклі(не менше 10 мільйонів): '))
    a1 = intunoplus(arg)
    a2 = intunominus(arg)
    a3 = intplus(arg)
    a4 = intminus(arg)
    a5 = intmult(arg)
    a6 = intdiv(arg)
    a9 = floatplus(arg)
    a10 = floatminus(arg)
    a11 = floatmult(arg)
    a12 = floatdiv(arg)
except ValueError:
    print('You input wrong value')
finally:
    print('u+ \t', 'int', '{:.6e}'.format(a1), '\t\t', 'X' * 100, '100 %')
    print('u- \t', 'int', '{:.6e}'.format(a2), '\t\t', 'X' * (a2 * 100 // a1), (a2 * 100 // a1), '%' )
    print('+ \t', 'int', '{:.6e}'.format(a3), '\t\t', 'X' * (a3 * 100 //a1), (a3 * 100 // a1), '%')
    print('- \t', 'int', '{:.6e}'.format(a4), '\t\t', 'X' * (a4 *100 // a1), (a4 * 100 // a1), '%')
    print('* \t', 'int', '{:.6e}'.format(a5), '\t\t', 'X' * (a5 *100 // a1), (a5 * 100 // a1), '%')
    print('// \t', 'int', '{:.6e}'.format(a6), '\t\t', 'X' * (a6 *100 // a1), (a6 * 100 // a1), '%')
    print('+ \t', 'float', '{:.6e}'.format(a9), '\t', 'X' * (a9 *100 // a1), (a9 * 100 // a1), '%')
    print('- \t', 'float', '{:.6e}'.format(a10), '\t', 'X' * (a10 *100 // a1), (a10 * 100 // a1), '%')
    print('* \t', 'float', '{:.6e}'.format(a11), '\t', 'X' * (a11 *100 // a1), (a11 * 100 // a1), '%')
    print('/ \t', 'float', '{:.6e}'.format(a12), '\t', 'X' * (a12 *100 // a1), (a12 * 100 // a1), '%')
