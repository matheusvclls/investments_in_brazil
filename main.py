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
def jc ( r : float , t : int , n : int = 1) -> float :
    return (1 + r / float ( n ))**( n * t ) - 1

# # Converte uma taxa di á ria para uma taxa anual .
# Em matem á tica financeira , consideramos 252 dias por ano .
#
# @param d taxa de juros di á ria .
# @param wd n ú mero de dias ú teis por ano .
# @return taxa de juros anual dada a taxa di á ria ,
# na forma de um percentual .
def day2year ( d : float , wd : int = 252) -> float :
    return 100 * jc (d , wd )

# # Converte uma taxa de juros anual para uma taxa mensal .
#
# @param a taxa de juros anual .
# @return taxa de juros mensal dada a taxa anual ,
# na forma de um percentual .
def year2month ( a : float ) -> float :
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
    return math * log (2 , 1 + r )
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
