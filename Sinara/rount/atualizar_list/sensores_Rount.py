from Sinara.model.sensor.lista_Sensores import ListaSensores

from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount


class SensoresRount:

    __caractere_antigo = None

    def __init__(self):

        self.varclass_ls = ListaSensores()

        # vem dos caracteres
        self.varclass_cr = CaracteteRount()

    def ler_caractere(self):
        """Lê o caractere atual e atualiza a lista de sensores."""

        var_letra = self.varclass_cr.get_rount_caractere()

        # Verifica se o caractere é alfabético
        if var_letra is not None:

            var_bool_sensor = self.varclass_ls.get_bool_sensor()

            if var_bool_sensor == False:

                self.varclass_ls.atualizar_adiciona_valor_sensor(
                    var_letra, 100)
                
                SensoresRount.__caractere_antigo = var_letra

            elif var_bool_sensor == True:

                # desativa o caractere antigo,
                self.varclass_ls.atualizar_adiciona_valor_sensor(
                    SensoresRount.__caractere_antigo, 0 )
                
                # ativa o novo caractere
                self.varclass_ls.atualizar_adiciona_valor_sensor(
                    var_letra, 100)
                
                SensoresRount.__caractere_antigo = var_letra
                


    """def atualizar_lista_ls(self, letra, valor):
        
        Atualiza a lista de sensores com os dados mais recentes.
        

        self.varclass_ls.atualizar_valor_sensor(letra, valor)

    def verificar_caracteres(self, letra):
        
        Verifica se o caractere é alfabético.
        
        self.varclass_ls.criar_item_lista(letra)
        self.varclass_ls.atualizar_valor_sensor(letra, 100)

    def get_celulas_ativas(self):
        
        Retorna a lista de sensores ativos.
        
        var_list_IR = self.varclass_ls.get_lista_100()
        return {
            id: valor
            for id, (referencia, valor) in enumerate(var_list_IR.items())
            if valor == 100
        }"""
