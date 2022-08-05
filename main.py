import math

# # Juros compostos .
#
# É a adi ç ã o de juros ao capital principal de um empr é stimo ou dep ó sito ,
# ou em outras palavras , juros sobre juros .
#
# É o resultado do reinvestimento dos juros , ao inv é s de pag á -lo ,
# de tal forma que a taxa no pr ó ximo per í odo é calculada
# sobre o principal , mais os juros recebidos previamente .
#
# A fun ç ã o de acumula ç ã o mostra como uma unidade monet á ria
# cresce ap ó s o per í odo de tempo .
#
# @param r taxa de juros nominal .
# @param t per í odo de tempo total no qual os juros s ã o aplicados
# ( expressa nas mesmas unidades de tempo de r , usualmente anos ).
# @param n frequ ê ncia de composi ç ã o ( pagamento dos juros ) , por exemplo ,
# mensal , trimestral ou anual .
# @return juros obtidos no per í odo : (1 + r/n) nt − 1
#

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

# # Calcula o montante final , imposto , rendimento e
# rentabilidade equivalente .
#
# @param c capital
# @param cdi taxa cdi anual
# @param p taxa poupan ç a anual = 0.70 * selic
# @param t rentabilidade da aplica ç ã o em fun ç ã o do CDI
# @param i al í quota do imposto de renda
# @param m meses
# @return
# - montante da aplica ç ão ,
# - montante poupan ça ,
# - imposto de renda retido ,
# - rendimento em m meses (%) ,
# - rendimento em m meses ,
# - rendimento l í quido em 1 m ês ,
# - rentabilidade para igualar poupan ç a (%) CDI
#
def CDB ( c : float , cdi : float , p : float , t : float , i : float , m : int = 1) -> float :
    return None
#... Essa deve ser implementada por voc ê ... 

print(jc(0.1,24,12))

print(year2month ( 0.12 ))
print(day2year ( 0.00049037 ))


