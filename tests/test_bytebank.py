from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given -> Contexto
        esperado = 22
        
        funcionarioTeste = Funcionario('Teste', entrada, 1111)
        
        resultado = funcionarioTeste.idade() #When -> Ação
        
        assert resultado == esperado #Then -> Desfecho
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = 'Carvalho'
        
        funcionarioTeste = Funcionario(entrada, '13/03/2000', 1000) 
        resultado = funcionarioTeste.sobrenome() #When
        
        assert resultado == esperado #Then
        