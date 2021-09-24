import mysql.connector
import time
from colorama import init, Fore, Back, Style # colorir parte do codigo


print(Fore.GREEN + "Bem Vindo ao programa de cadastramento de medicos")
time.sleep(2)

inicio = str(input("Deseja Iniciar o sistema?(Sim/Não) ")).upper()
if inicio == 'SIM':

  def senior():
    con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='')

    cursor = con.cursor()

      #CRIAÇÃO DA TABELA E DO BANCO DE DADOS

#    def CriarBase():                                        #1
#      cursor.execute("CREATE DATABASE cadastro")
#    print("Banco de Dados criado com sucesso!")


#    def CriarTabela():                                      #2
#      cursor.execute("CREATE TABLE medicos (ID INT AUTO_INCREMENT PRIMARY KEY, NOME TEXT, CPF int(15), NUMERO int(15), AREA TEXT)")
 


    print(Fore.GREEN + "\n\n-+-+-+-+ HOSPITAL NOBRE -+-+-+-+\n")
    time.sleep(2)

    def chance():
      nome = str(input(Fore.GREEN + "Digite seu nome Completo para entrar no Sistema de Cadastramento: ")).upper()
      print("\nVERIFICANDO")
      time.sleep(2)
      if nome == 'ANDRE NOBRE':
        print(Fore.BLUE + "\nBem Vindo ao Sistema de Cadastramento de Médicos\n")
        time.sleep(2)
      else:
        print(Fore.RED + "\nACESSO NEGADO!!!\n")
        time.sleep(1)
        tent = str(input(Fore.YELLOW + "Deseja Tentar Novamente?(SIM/NÃO) ")).upper()
        if tent == 'SIM':
          time.sleep(1.5)
          chance()
        else:
          exit(Fore.RED + "- SISTEMA FINALIZADO -")

    chance()

      # execução Do 'def CriarBase() e CriarTabela()' 

    #CriarBase()
    #CriarTabela()

    def InserirDados():                                     #3
      input_nome = input(Fore.GREEN + "1 - Digite o Nome do Medico: ")   
      input_cpf = int(input("2 - Digite o CPF do Medico: "))
      input_num = input("3 - Digite o Número de Telefone do Medico: ") 
      input_area = input("4 - Digite a Área de Atuação do Medico: ")
      time.sleep(0.2)
      print("AGUARDE...")

      confirm = str(input(f"O Nome {input_nome}, O CPF {input_cpf}, O Número {input_num}, A Área de Atuação: {input_area} Estão corretos?(SIM/NÃO)" )).upper()
      if confirm != 'SIM':
        print("AGUARDE...")
        InserirDados()
      elif confirm == 'SIM':
        print("INSERINDO...")
        time.sleep(3)

      comando_SQL = "INSERT INTO medicos (NOME, CPF, NUMERO, AREA) VALUES (%s, %s, %s, %s)"
      valores = (input_nome, input_cpf, input_num, input_area)

      cursor.execute(comando_SQL, valores)
      con.commit()

      print("Dados Inseridos com Sucesso")

    InserirDados()    
  senior()

else:
  exit(Fore.RED + "- SISTEMA FINALIZADO -")

