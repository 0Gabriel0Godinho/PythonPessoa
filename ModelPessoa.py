#Classe de Model Pessoa - Onde é criado os metodos
class ModelPessoa:
    # Declaração de variaveis
    def __initi__(self): #Metodo Construtor
        self.cpf = 0   #Onde tem 0 é uma declaração de variaveis numericas
        self.nome = "" #Onde tem as "" é uma variavel de texto
        self.telefone = 0
        self.endereco = ""
        self.email = ""

    def cadastrarPessoa(self,cpf,nome,telefone,endereco,email):
        self.cpf = cpf   #A utilização do self.cpf é pra saber da onde vem as informações
        self.nome = nome  #(com o self o programa "vê" que é variavel)
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def consultarPessoa(self):  #Não precisa de parametro pois ira apenas devolver os dados
        consulta =  f"CPF {self.cpf}\n Nome: {self.nome}\n Telefone: {self.telefone}\n" \
                    f"Endereço: {self.endereco}\n E-mail: {self.email}"
        return consulta

    def atualizarPessoa(self,opcao,dado): #O parametro dado é uma variavel generica, pode ser usado pra
        if opcao == 1:                    #qualquer variavel, pois ela mudará apenas de 1 em 1
            self.nome = dado
        elif opcao == 2:
            self.telefone = dado
        elif opcao == 3:
            self.endereco = dado
        elif opcao == 4:
            self.email = dado

    def excluirPessoa(self):
            self.cpf = 0
            self.nome = ""
            self.telefone = 0
            self.endereco = ""
            self.email = ""
