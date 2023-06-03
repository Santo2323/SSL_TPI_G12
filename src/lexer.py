import ply.lex as lex   # lexer -> tokens
import re
from logicaMenu import cls, logicaMenu
from helpers import pedirRuta

contadorErrores = 0

# Terminales
tokens = [
    # simbolos
     'dospuntos',
    #  'slash',

    # Opcionales TODO: Verificar cuales serian nuestros opcionales
    # 'height',
    # 'cerrarheight',
    # 'width',
    # 'cerrarwidth',

    # Simbolos URL
     'protocolo',

    # etiquetas
    'article',
    'cierreArticle',
    
    'section',
    'cierreSection',
    
    'info',
    'cierreInfo'
    
    'simpleSection',
    'cierreSimpleSection',
    
    'title',
    'cierreTitle',
    
    'itemizedlist',
    'cierreItemizedlist',

    'important',
    'cierreImportant',
    
    'para',
    'cierrePara',
    
    'simpara',
    'cierreSimpara',

    'address',
    'cierreAddress',

    # 'mediaObject' //TODO: NO TENGO IDEA DE COMO HACERLO, A VER MAS TARDE  

    'informalTable',
    'cierreInformalTable',
    
    'comment',
    'cierreComment',

    'abstract',
    'cierreAbstract',
    
    'author',
    'cierreAuthor',
    
    'date',
    'cierreDate',
    
    'copyright',
    'cierreCopyright',
    
    'street',
    'cierreStreet',
    
    'city',
    'cierreCity',
    
    'state',
    'cierreState',
    
    # Contenido entre etiquetas
    'contenido_texto',
    # 'URL'

]

# PLY detecta variables que empiecen con 't_'
# Terminos:
# w = letras o numeros
# s = todo lo que sea espacios.
# S = contrario a 's'.
# d = digitos.
#  = 0 o más.
# + = 1 o más.

# Definición de símbolos atómicos #

# Etiquetas

def t_article(t): r'<article>'; return(t);
def t_cierreArticle(t): r'</article>'; return(t);

def t_section(t): r'<section>'; return(t);
def t_cierreSection(t): r'</section>';  return(t);

def t_info(t): r'<info>'; return(t);
def t_cierrreInfo(t): r'</info>'; return(t);   

def t_simpleSection(t): r'<simplesect>'; return(t);
def t_cierreSimpleSection(t): r'</simplesect>'; return(t);

def t_title(t): r'<title>'; return(t);
def t_cierreTitle(t): r'</title>'; return(t);

def t_itemizedlist(t): r'<itemizedlist>'; return (t);
def t_cierreItemizedlist(t): r'</itemizedlist>'; return (t);

def t_important(t): r'<important>'; return (t);
def t_cierreImportant(t): r'</important>'; return (t);

def t_para(t): r'<para>'; return (t);
def t_cierrePara(t): r'</para>'; return (t);

def t_simpara(t): r'<simpara>'; return (t);
def t_cierreSimpara(t): r'</simpara>'; return (t);

def t_address(t): r'<address>'; return (t);
def t_cierreAddress(t): r'</address>'; return (t);

def t_informalTable(t): r'<informaltable>'; return (t);
def t_cierreInformalTable(t): r'</informaltable>'; return (t);

def t_comment(t): r'<comment>'; return (t);
def t_cierreComment(t): r'</comment>'; return (t);

def t_author(t): r'<author>'; return (t);
def t_cierreAuthor(t): r'</author>'; return (t);

def t_date(t): r'<date>'; return (t);
def t_cierreDate(t): r'</date>'; return (t);

def t_copyright(t): r'<copyright>'; return (t);
def t_cierreCopyright(t): r'</copyright>'; return (t);

def t_street(t): r'<street>'; return (t);
def t_cierreStreet(t): r'</street>'; return (t);

def t_state(t): r'<state>'; return (t);
def t_cierreState(t): r'</state>'; return (t);






# Protocolos
def t_protocolo(t): r'(https|http|ftps|ftp):\/\/'; return (t)

# Etiquetas opcionales
# def t_height(t): r'<height>'; return(t)
# def t_cerrarheight(t): r'<\/height>'; return(t)

# def t_width(t): r'<width>'; return(t)
# def t_cerrarwidth(t): r'<\/width>'; return(t)

# def t_image(t): r'<image>'; return(t)
# def t_cerrarimage(t): r'<\/image>'; return(t)

# def t_copyright(t): r'<copyright>'; return(t)
# def t_cerrarcopyright(t): r'<\/copyright>'; return(t)

# Resto
# t_digito = r'\d+'
t_dospuntos = r'\:'
# t_slash = r'/'
# t_numeral = r'\#'

# PLY ignorará espacios, saltos de lineas y tabs.
t_ignore = ' \t'

def t_error(t):
    global contadorErrores
    print(f'Caracter ilegal! : \'{t.value[0]}\'.')
    print(f'En linea: {t.lineno}. Posición: {t.lexpos}')
    contadorErrores += 1
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_contenido_texto(t): r'([\w\W])+?(?=<\/)'; return (t)

# Logica para menu
menu_options = {
    1: 'Analizar tokens desde un archivo, indicando su ruta.',
    2: 'Escanear tokens línea por línea.',
    3: 'Salir.',
}

def analizarPorRuta():
    pathClean = pedirRuta()
    lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula
    # Ejecución "analisis de archivo de texto"
    try:
        file = open(pathClean,"r",encoding='utf8')
        strings = file.read()
        file.close()
        lexer.input(strings)
        analizarTokens('archivo', lexer)
    except IOError:
        print('Ocurrió un error leyendo archivo:', pathClean)

def analizarPorLinea():
    lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula

    # Ejecución "normal"
    print('Terminar la ejecución: [ctrl] + [C] | Para volver al menú principal escribir: _salir')
    while True:
        s = input('>> ')
        if s == '_salir':
            cls()
            break;
        lexer.input(s)
        analizarTokens('normal', lexer)
# Fin logica para menu

# Exportar TOKENS a un .txt
def exportarTokens(arrAnalizar):
    global contadorErrores
    fileNameExport = f'tokens-analizados.txt'
    with open(fileNameExport, 'w', encoding='UTF8') as f:
        f.write('TOKEN | VALOR\n')
        f.write('-------------\n')
        contador = 0
        for line in arrAnalizar:
            contador += 1
            f.write(f'{contador}- {line[0]}: {line[1]}')
            f.write('\n')
        f.write('-------------\n')
        f.write(f'Total de tokens válidos analizados: {contador}.\n')
        if (contadorErrores > 0):
            f.write(f'Total de tokens NO válidos: {contadorErrores}.')
    f.close()
    if (contadorErrores > 0):
        print('(⨉) El lexer NO acepta este archivo.')
    else:
        print('(✅) El lexer ACEPTA este archivo.')
    print('(!) Se exportó un .txt con los tokens analizados.')

# Se pasa como argumento al objeto lexer ya que,
# la expresion de `t_contenido_texto` debe ser sobreescribida
# según el modo de ejecución.
def analizarTokens(modoEjecucion, lexer):
        global contadorErrores
        exportArray = []
        while True:
                tok = lexer.token()
                if not tok:
                    if (modoEjecucion == 'archivo'):
                        exportarTokens(exportArray)
                    break
                if (modoEjecucion == 'archivo'):
                    exportArray.append([tok.type,tok.value]);
                else: print(f'Tipo: {tok.type} | Valor: {tok.value}')

# Solo si se ejecuta desde lexer.py hacer...
if __name__ == "__main__":
    logicaMenu(
        'Lexer',
        menu_options,
        analizarPorRuta,
        analizarPorLinea,
    )
else:
    # Se exporta al `lexer` para que pueda ser ocupado desde,
    # por ejemplo, el parser.
    lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula
