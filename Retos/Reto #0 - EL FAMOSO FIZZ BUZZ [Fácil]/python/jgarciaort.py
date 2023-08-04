"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""
n=0
while n<100:
    n = n+1
    if n%3 == 0 and n%5 == 0:
        print("\nFizzBuzz")
    elif n%3 == 0:
        print("\nfizz")
    elif n%5 == 0:
        print("\nbuzz")
    else: 
        print(n)
