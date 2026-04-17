import os

def Printar(c):
    if int(c) % 2 != 0:
        print(c)
    else:
        return -1

def Ler():
    dir = 'C:/temp/exercicios/'
    arq = '37.txt'
    file_path = ''
    enc = 'utf-8'
    tipo = 'r'
    ant = ''
    
    file_path = dir + arq

    with open(file_path, tipo, encoding=enc) as file:
        for linha in file:
            for char in linha:
                if char.isdigit():
                        ant += char 
                else:
                    Printar(ant)
                    ant = ''  
def main():
    Ler()
    
if __name__ == '__main__':
    main()
