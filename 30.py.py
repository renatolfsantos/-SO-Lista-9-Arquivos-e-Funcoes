import os

def Gravar(n):
    global counter
    dir = 'C:/temp/exercicios/'
    arq = '30.txt'
    file_path = ''
    enc = 'utf-8'
    tipo = ''

    file_path = dir + arq

    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        
    os.chmod(dir, 0o744)

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        enc = 'utf-8'

        if os.path.exists(file_path):
            tipo = 'a'

        with open(file_path, tipo, encoding=enc) as file:
            file.write(f'{n}\n')


def CalcSerie():
    for i in range(10, 151):
        Gravar(i * i)

def main():
    CalcSerie()

if __name__== '__main__':
    main()
