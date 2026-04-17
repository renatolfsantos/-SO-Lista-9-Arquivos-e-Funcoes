import os

def Gravar(s):
    dir = 'C:/temp/exercicios/'
    arq = '37.txt'
    file_path = ''
    enc = 'utf-8'
    tipo = 'a'

    file_path = dir + arq

    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        
    os.chmod(dir, 0o744)

    if os.path.exists(dir) and os.path.isdir(dir):
        with open(file_path, tipo, encoding=enc) as file:
            file.write(s + '\n')

def CalcFib(n):
    atual = 1
    anterior = 0
    proximo = 0
    
    fib = '0,1'
    
    if n == 1:
        Gravar('0')
        return
    elif n == 2:
        Gravar('0,1')
        return
    for i in range(2, n):
        proximo = atual + anterior
        
        fib = fib + ',' + str(proximo)
        
        anterior = atual
        atual = proximo

    Gravar(fib)
        

def main():
    num = 0

    num = int(input('Digite um número: '))

    CalcFib(num)

if __name__ == '__main__':
    main()
