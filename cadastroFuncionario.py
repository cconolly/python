import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

def lin():
    print('=' * 25)

lin()
print('CADASTRO DE COLABORADORES')
lin()
print()

nome = input('Digite o nome do colaborador: ')

while len(nome) < 3:
    print('Nome Inválido! Digite novamente!')
    nome = input('Digite o nome do colaborador: ')


idade = int(input('Digite a idade do colaborador: '))

while idade <= 0 or idade > 150:
    print('Idade Inválida! Digite novamente:')
    idade = int(input('Digite a idade do colaborador: '))

salario = float(input('Digite o salário do colaborador: '))

while salario <= 0:
    print('Salário inválido! Digite novamente!')
    salario = float(input('Digite o salário do colaborador: '))

while True:
    sexo = input('Digite o sexo do colaborador(M/F): ').lower()

    if sexo == 'm':
        sexo = 'Masculino'
        break
    elif sexo == 'f':
        sexo = 'Feminino'
        break
    else:
        print('Sexo Inválido! Digite novamente!.')

while True:
    estadoCivil = input('Digite o estado civil do colaborador(S/C/V/D): ').lower()
    if estadoCivil == 's':
        estadoCivil = 'Solteiro'
        break
    elif estadoCivil == 'c':
        estadoCivil = 'Casado'
        break
    elif estadoCivil == 'v':
        estadoCivil = 'Viúvo'
        break
    elif estadoCivil == 'd':
        estadoCivil = 'Divorciado'
        break
    else:
        print('Estado Civil Inválido! Digite novamente!')


os.system('cls' if os.name == 'nt' else 'clear')

lin()
print('CADASTRO REALIZADO COM SUCESSO!')
lin()
time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')

lin()
print('Nome:', nome)
print('Idade:', idade, 'anos')
print(f'Salário: R${salario:.2f}')
print('Sexo:', sexo)
print('Estado Civil:', estadoCivil)
lin()

fimPrograma = input('Fim do programa! Aperte enter para encerrar!')