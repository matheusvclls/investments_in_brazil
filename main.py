import math

TAXA_SELIC_ANUAL = 0.1325
TAXA_CDI_ANUAL = 0.1315

def jc ( r : float , t : int , n : int = 1) -> float :
    '''
    Função responsável por calcular os juros compostos sobre o capital

    Args:
        r (float): taxa de juros nominal
        t (int): período total no qual os juros são aplicados
        n (int): frequência em que os juros incorrem sobre o capital. Por exemplo: anual, trimestral ou semestral.

    Returns:
        float: total de juros obtidos no período
    '''
    return (1 + r / float ( n ))**( n * t ) - 1


def day2year ( d : float , wd : int = 252) -> float :
    '''
    Função responsável por converter a taxa de juros diária para anual.
    Como o valor de dias úteis é opcional, o default é 252

    Args:
        d (float): taxa de juros diária
        wd (int, optional): números de dias úteis no ano
    
    Returns:
        float: taxa de juros anual (em formato de percentual)
    '''
    return 100 * jc (d , wd )


def year2month ( a : float ) -> float :
    '''
    Função responsável por converter a taxa de juros anual para mensal

    Args:
        a (float): taxa de juros anual
    
    Returns:
        float: taxa de juros mensal (em formato de percentual)
    '''
    return 100 * jc (a , 1 / 12.0)

# # Calcula o logaritmo de 2 na base 1 + r.
# Pode ser aproximado por 72/(100 ∗ r).
#
# É usada para calcular o tempo necess á rio
# para dobrar o principal quando sujeito uma taxa de juros dada .
#
# @param r taxa de juros nominal .
# @return tempo para dobrar o principal .
#
def doublePrincipal ( r : float ) -> float :
    # apenas checar se podemos utilizar a taxa nominal ou não
    return math.log(2,10)/math.log(1+r,10)
#... Inclua suas fun ç õ es aqui ...


def CDB ( c : float , cdi : float , p : float , t : float , i : float , m : int = 1) -> float :
    '''
    Função responsável por calcular o  montante final , imposto , rendimento e
    rentabilidade equivalente da poupança e do CDI

    Args:
        c (float): capital investido
        cdi (float): taxa cdi anual
        p (float): taxa da poupança anual que é igual a 0.70 * selic
        t (float): rentabilidade da aplicação em função do CDI
        i (float): alíquota do imposto de renda
        m (int): meses

    Returns:
        montante da aplicação
        montante poupança
        imposto de renda retido
        rendimento em m meses (%)
        rendimento em m meses
        rendimento líquido em 1 mês
        rentabilidade para igualar poupança (%) CDI
    '''

    taxa_cdi_mensal = round(year2month(cdi),4)
    taxa_cdi_diaria = "ainda falta implementar"
    taxa_poupanca_anual = p*.7
    taxa_poupanca_mensal = round(year2month(taxa_poupanca_anual),4)

    print("\n")
    print("Capital = ${:.2f}".format(c))

    print("Taxa SELIC = {}%".format(p*100))

    print("Taxa CDI = {}% ao ano = {}% ao mês = {}% ao dia".format(cdi*100, taxa_cdi_mensal, taxa_cdi_diaria))
    
    # print com erro -> verificar
    print("Taxa Poup = {}% ao ano = {}% ao mês".format(taxa_poupanca_anual*100,taxa_poupanca_mensal))
    

    print("\n")
    print("IR = {}%".format(i))
    print("\n")

    rentabilidade_percentual_cdi = round(t*cdi,2)
    rentabilidade_liquida_cdi = round(t*((100-i)/100),2)
    rentabilidade_liquida_percentual_cdi = round(rentabilidade_percentual_cdi*((100-i)/100),2)

    print("Rentabilidade = {:.1f}% CDI = {}%".format(t, rentabilidade_percentual_cdi))
    print("Com impostos = {}% CDI = {}%".format(rentabilidade_liquida_cdi,rentabilidade_liquida_percentual_cdi))
    
    print("\n")
    print("Meses = {}".format(m))

    print("\n")
    return None

CDB(1000, 0.1315, 0.1325, 93, 22.5)
