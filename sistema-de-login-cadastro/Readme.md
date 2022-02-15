                   ==>> Para a execução correta do código, necessário a instalação e execução do MySQL workbench <<==

                                                                 1° Crie o Banco

def CriarBase():                                      
  cursor.execute("CREATE DATABASE cadastro")
  print("Banco de Dados criado com sucesso!")
  
  
                                                                 2° Crie a Tabela 

def CriarTabela():                                      #2
  cursor.execute("CREATE TABLE medicos (ID INT AUTO_INCREMENT PRIMARY KEY, NOME TEXT, CPF int(15), NUMERO int(15), AREA TEXT)")
  
