import math
import sys
import getopt


def usage():
    print(
        'Usage: ./' +
        sys.argv[0] +
        ' -c [ capital ] -a [ CDI anual ] -s [ Selic ]-i [ al í quota IR ] -t [ taxa CDI ] -m [ meses ] -h [ help ]')


def get_args():
    '''
    Function responsible for get args passed by users

    Args
        None

    Returns
        capital (float): initial capital
        taxa_cdi (float): cdi rate
        taxa_imposto (float): tax rate
        percentual_do_cdi (float): percent of total cdi rate
        taxa_selic (float): selic rate
        meses (int): months to calc
    '''

    capital = None
    taxa_imposto = None
    percentual_do_cdi = None
    taxa_cdi = None
    taxa_selic = None
    month = 1

    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "c:i:t:a:s:m:h", ["help", "h"])

        # Instrução de erro sem parâmetros
        if opts == []:
            print("Sem parâmetros passados. Gentileza seguir a instrução abaixo:")
            usage()
            sys.exit()

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        if o in ['-c']:
            capital = float(a)
        elif o in ['-i']:
            taxa_imposto = float(a)
        elif o in ['-t']:
            percentual_do_cdi = float(a)
        elif o in ['-a']:
            taxa_cdi = float(a)
        elif o in ['-s']:
            taxa_selic = float(a)
        elif o in ['-m']:
            month = int(a)
        else:
            assert False, "unhandled option"

    # Checar se todos os argumentos obrigatórios foram passados
    if capital is not None and taxa_cdi is not None and taxa_imposto is not None and percentual_do_cdi is not None and taxa_selic is not None:
        pass
    else:
        print("Falta de parâmetros obrigatórios. Gentileza seguir a instrução abaixo:")
        usage()
        sys.exit()
    return capital, taxa_cdi, taxa_imposto, percentual_do_cdi, taxa_selic, month


def jc(r: float, t: int, n: int = 1) -> float:
    '''
    Função responsável por calcular os juros compostos sobre o capital

    Args:
        r (float): taxa de juros nominal
        t (int): período total no qual os juros são aplicados
        n (int): frequência em que os juros incorrem sobre o capital. Por exemplo: anual, trimestral ou semestral.

    Returns:
        float: total de juros obtidos no período
    '''
    return (1 + r / float(n))**(n * t) - 1


def day2year(d: float, wd: int = 252) -> float:
    '''
    Função responsável por converter a taxa de juros diária para anual.
    Como o valor de dias úteis é opcional, o default é 252

    Args:
        d (float): taxa de juros diária
        wd (int, optional): números de dias úteis no ano

    Returns:
        float: taxa de juros anual (em formato de percentual)
    '''
    return 100 * jc(d, wd)


def year2month(a: float) -> float:
    '''
    Função responsável por converter a taxa de juros anual para mensal

    Args:
        a (float): taxa de juros anual

    Returns:
        float: taxa de juros mensal (em formato de percentual)
    '''
    return 100 * jc(a, 1 / 12.0)


def doublePrincipal(r: float) -> float:
    """
    Função responsável pelo cálculo do tempo que o capital dobrará
    com base na taxa de juros passada na variável "r"

    Args
        r (float): taxa de juros nominal

    Returns
        time_to_double_capital (float): tempo para dobrar o capital
    """
    return math.log(2, 10) / math.log(1 + r, 10)


def calculo_rendimento_poupanca(taxa_selic: float) -> float:
    '''
    Função responsável por calcular a taxa de rendimento da poupança

    Args
        taxa_selic (float): taxa selic anual e em forma de decimal

    Returns
        calculo_rendimento_poupanca (float): rendimento anual da poupança liquido
    '''
    if taxa_selic < 0.085:
        calculo_rendimento_poupanca = taxa_selic * .7

    else:
        calculo_rendimento_poupanca = 0.0617

    return calculo_rendimento_poupanca


def CDB(c: float, cdi: float, p: float,
        t: float, i: float, m: int = 1) -> float:
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

    taxa_cdi_mensal = round(year2month(cdi), 4)
    taxa_cdi_diaria = "ainda falta implementar"  # fix this part
    rendimento_poupanca_anual = calculo_rendimento_poupanca(p)
    rendimento_poupanca_mensal = round(
        year2month(rendimento_poupanca_anual), 4)

    print("\n")
    print("Capital = ${:.2f}".format(c))

    print("Taxa SELIC = {}%".format(p * 100))

    print("Taxa CDI = {}% ao ano = {}% ao mês = {}% ao dia".format(
        cdi * 100, taxa_cdi_mensal, taxa_cdi_diaria))

    print("Taxa Poup = {}% ao ano = {:.4f}% ao mês".format(
        rendimento_poupanca_anual * 100, rendimento_poupanca_mensal))

    print("\n")
    print("IR = {}%".format(i))
    print("\n")

    rentabilidade_percentual_cdi = round(t * cdi, 2)
    rentabilidade_liquida_cdi = round(t * ((100 - i) / 100), 2)
    rentabilidade_liquida_percentual_cdi = round(
        rentabilidade_percentual_cdi * ((100 - i) / 100), 2)
    rentabilidade_liquida_cdi_mensal = year2month(
        rentabilidade_liquida_percentual_cdi / 100) / 100

    print("Rentabilidade = {:.1f}% CDI = {}%".format(
        t, rentabilidade_percentual_cdi))
    print(
        "Com impostos = {}% CDI = {}%".format(
            rentabilidade_liquida_cdi,
            rentabilidade_liquida_percentual_cdi))

    print("\n")
    print("Meses = {}".format(m))

    print("\n")
    montatnte_aplicacao = round(
        (jc(rentabilidade_liquida_cdi_mensal, 1, 1)) * c + c, 2)
    montante_poupanca = round(
        (jc(rendimento_poupanca_mensal / 100, 1, 1)) * c + c, 2)
    print("Montante Aplicação = ${}".format(montatnte_aplicacao))
    print("Montante Poupança = ${:.2f}".format(montante_poupanca))
    diferenca_aplicacoes = montatnte_aplicacao - montante_poupanca
    print("Ap1 - Poup ({} meses) = ${:.2f}".format(m, diferenca_aplicacoes))

    rentabilidade_percentual_cdi_mensal = year2month(
        rentabilidade_percentual_cdi / 100)
    montatnte_aplicacao_com_impostos = round(
        (1 + (rentabilidade_percentual_cdi_mensal / 100)) * c, 2)
    total_impostos = (montatnte_aplicacao_com_impostos - montatnte_aplicacao)
    # ainda errada utilizar a função jc
    print("Imposto = ${:.4f}".format(total_impostos))
    print("Rendimento em {} meses = {:.4f}%".format(
        m, rentabilidade_liquida_cdi_mensal * 100))

    print("\n")
    percentual_diferenca_aplicacoes = diferenca_aplicacoes / c * 100
    print("Ap1 - Poup ({} meses) = {:.4f}%".format(m,
          percentual_diferenca_aplicacoes))
    taxa_do_cdi_igual_poupanca = rendimento_poupanca_mensal / \
        rentabilidade_liquida_cdi_mensal
    print("Ap1 = Poup = {:.2f}% CDI".format(taxa_do_cdi_igual_poupanca))

    tempo_dobrar_poupanca_anos = doublePrincipal(rendimento_poupanca_anual)
    tempo_dobrar_poupanca_meses = doublePrincipal(
        rendimento_poupanca_mensal / 100)
    print("Tempo 2x Poupança = {:.2f} anos = {:.2f} meses".format(
        tempo_dobrar_poupanca_anos, tempo_dobrar_poupanca_meses))

    tempo_dobrar_aplicacao_anos = doublePrincipal(
        rentabilidade_liquida_percentual_cdi / 100)
    tempo_dobrar_aplicacao_meses = doublePrincipal(
        rentabilidade_liquida_cdi_mensal)
    print("Tempo 2x Aplicação = {:.2f} anos = {:.2f} meses".format(
        tempo_dobrar_aplicacao_anos, tempo_dobrar_aplicacao_meses))
    return None


if __name__ == "__main__":
    capital, taxa_cdi, taxa_imposto, percentual_do_cdi, taxa_selic = get_args()
    CDB(capital, taxa_cdi, taxa_selic, percentual_do_cdi, taxa_imposto)
