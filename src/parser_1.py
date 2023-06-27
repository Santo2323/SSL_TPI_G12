from logicaMenu import logicaMenu
from helpers import pedirRuta
from obtenerHtml import exportarHtml

import ply.yacc as yacc  # parser
# Importar lexer para luego reiniciarlo (para no guardar su estado anterior)
import lexer
from lexer import tokens

from importlib import reload

exportarTxt = list()
contadorErrores = 0

# Mayusculas = No Terminales; Minusculas = Terminales

def p_SIGMA(p):
    ''' SIGMA : doctype ARTICLE'''
    print("Ejecución completa!")
    exportarTxt.append(['Prod. Sigma -->', p.slice])


def p_ARTICLE(p):
    '''ARTICLE : article contenido_texto cierreArticle
                
    '''
    exportarTxt.append(['Prod. ARTICLE -->', p.slice])
    
# def p_RSS(p):
#     '''RSS : rss CHANNEL cerrarrss
#     '''
#     exportarTxt.append(['Prod. RSS -->', p.slice])


# def p_CHANNEL(p):
#     '''CHANNEL : channel ET_OBL ITEM_REC cerrarchannel'''
#     exportarTxt.append(['Prod. CHANNEL -->', p.slice])


# def p_ET_OBL(p):
#     '''ET_OBL : ET_TITLE ET_LINK ET_DESC ET_CATEGORY ET_COPYRIGHT ET_IMG
#     '''
#     exportarTxt.append(['Prod. ET_OBL -->', p.slice])


# def p_LAMBDA(p):
#     'LAMBDA :'
#     pass


# def p_ET_TITLE(p):
#     '''ET_TITLE : titulo CONT_TEXTO cerrartitulo
#     '''
#     exportarTxt.append(['Prod. ET_TITLE -->', p.slice])


# def p_ET_LINK(p):
#     '''ET_LINK : link CONT_LINK cerrarlink
#     '''
#     exportarTxt.append(['Prod. ET_LINK -->', p.slice])


# def p_ET_URL(p):
#     '''ET_URL : url CONT_LINK cerrarurl
#     '''
#     exportarTxt.append(['Prod. ET_URL -->', p.slice])


# def p_ET_DESC(p):
#     '''ET_DESC : description CONT_TEXTO cerrardescription
#     '''
#     exportarTxt.append(['Prod. ET_DESC -->', p.slice])


# def p_ET_CATEGORY(p):
#     '''ET_CATEGORY : category CONT_TEXTO cerrarcategory
#                     | LAMBDA
#     '''
#     exportarTxt.append(['Prod. ET_CATEGORY -->', p.slice])


# def p_ET_COPYRIGHT(p):
#     '''ET_COPYRIGHT : copyright CONT_TEXTO cerrarcopyright
#                     | LAMBDA
#     '''
#     exportarTxt.append(['Prod. ET_COPYRIGHT -->', p.slice])


# def p_CONT_TEXTO(p):
#     '''CONT_TEXTO : contenido_texto CONT_TEXTO
#                 | contenido_texto
#     '''
#     exportarTxt.append(['Prod. CONT_TEXTO -->', p.slice])


# def p_ET_IMG(p):
#     '''ET_IMG : image CONT_IMG cerrarimage
#               | LAMBDA
#     '''
#     exportarTxt.append(['Prod. ET_IMG -->', p.slice])


# def p_CONT_IMG(p):
#     '''CONT_IMG : ET_IMG_OBL ET_IMG_OP
#                 | ET_IMG_OBL
#     '''
#     exportarTxt.append(['Prod. CONT_IMG -->', p.slice])


# def p_ET_IMG_OBL(p):
#     '''ET_IMG_OBL  : ET_TITLE ET_LINK ET_URL
#                    | ET_TITLE ET_URL ET_LINK
#                    | ET_URL ET_TITLE ET_LINK
#                    | ET_URL ET_LINK ET_TITLE
#                    | ET_LINK ET_TITLE ET_URL
#                    | ET_LINK ET_URL ET_TITLE
#     '''
#     exportarTxt.append(['Prod. ET_IMG_OBL  -->', p.slice])


# def p_ET_IMG_OP(p):
#     '''ET_IMG_OP  : ET_HEIGHT ET_IMG_OP
#                   | ET_WIDTH ET_IMG_OP
#                   | ET_HEIGHT
#                   | ET_WIDTH
#     '''
#     exportarTxt.append(['Prod. ET_IMG_OP  -->', p.slice])


# def p_ET_HEIGHT(p):
#     '''ET_HEIGHT : height digito cerrarheight
#                  | height contenido_texto cerrarheight
#     '''
#     global contadorErrores
#     # Posicion 2 = Valor de la etiqueta height
#     heightValue = int(p[2])
#     HEIGHT_LIMIT = 400
#     if (type(heightValue) is not int):
#         print('Valor de Height NO es un numero')
#         contadorErrores += 1
#         p[2] = 0
#     elif (heightValue > HEIGHT_LIMIT):
#         print('Superó el limite de', HEIGHT_LIMIT, 'en HEIGHT')
#         # 2 es `digito` o `contenido_texto`
#         print('Linea:', p.lineno(2))
#         contadorErrores += 1
#     exportarTxt.append(['Prod. ET_HEIGHT -->', p.slice])


# def p_ET_WIDTH(p):
#     '''ET_WIDTH : width digito cerrarwidth
#                 | width contenido_texto cerrarwidth
#     '''
#     global contadorErrores

#     # Posicion 2 = Valor de la etiqueta width
#     widthValue = int(p[2])
#     WIDTH_LIMIT = 144
#     if (type(widthValue) is not int):
#         print('Valor de Width NO es un numero')
#         contadorErrores += 1
#         p[2] = 0
#     elif (widthValue > WIDTH_LIMIT):
#         print('Superó el limite de', WIDTH_LIMIT, 'en WIDTH')
#         print('Linea:', p.lineno(2))
#         contadorErrores += 1
#     exportarTxt.append(['Prod. ET_WIDTH -->', p.slice])


# def p_CONT_LINK(p):
#     '''CONT_LINK : protocolo DOMINIO_GRAL FINAL_URL
#                  | protocolo DOMINIO_GRAL
#     '''
#     exportarTxt.append(['Prod. CONT_LINK -->', p.slice])


# def p_FINAL_URL(p):
#     '''FINAL_URL : slash RUTA numeral LOCALIZADOR
#                  | slash RUTA
#     '''
#     exportarTxt.append(['Prod. CONT_LINK -->', p.slice])


# def p_DOMINIO_GRAL(p):
#     '''DOMINIO_GRAL : DOMINIO dospuntos PUERTO
#                     | DOMINIO
#     '''
#     exportarTxt.append(['Prod. DOMINIO_GRAL -->', p.slice])


# def p_LOCALIZADOR(p):
#     '''LOCALIZADOR : contenido_texto
#     '''
#     exportarTxt.append(['Prod. LOCALIZADOR -->', p.slice])


# def p_DOMINIO(p):
#     '''DOMINIO : contenido_texto
#     '''
#     exportarTxt.append(['Prod. DOMINIO -->', p.slice])


# def p_RUTA(p):
#     '''RUTA : contenido_texto
#     '''
#     exportarTxt.append(['Prod. RUTA -->', p.slice])


# def p_PUERTO(p):
#     '''PUERTO : digito
#               | contenido_texto
#     '''
#     exportarTxt.append(['Prod.  -->', p.slice])


# def p_ITEM_REC(p):
#     '''ITEM_REC : ET_ITEM ITEM_REC
#                 | ET_ITEM
#     '''
#     exportarTxt.append(['Prod. ITEM_REC -->', p.slice])

# def p_ET_ITEM(p):
#     '''ET_ITEM : item ET_OBL_ITEM cerraritem
#     '''
#     exportarTxt.append(['Prod. ET_ITEM -->', p.slice])


# def p_ET_OBL_ITEM(p):
#     '''ET_OBL_ITEM : ET_TITLE ET_DESC ET_LINK ET_CATEGORY
#                 | ET_TITLE ET_DESC ET_CATEGORY ET_LINK
#                 | ET_TITLE  ET_CATEGORY  ET_DESC ET_LINK
#                 | ET_TITLE  ET_CATEGORY  ET_LINK ET_DESC
#                 | ET_TITLE ET_LINK ET_CATEGORY  ET_DESC
#                 | ET_TITLE ET_LINK  ET_DESC ET_CATEGORY
#                 | ET_DESC  ET_TITLE ET_LINK ET_CATEGORY
#                 | ET_DESC  ET_TITLE ET_CATEGORY ET_LINK
#                 | ET_DESC ET_CATEGORY ET_TITLE ET_LINK
#                 | ET_DESC ET_CATEGORY ET_LINK ET_TITLE
#                 | ET_DESC ET_LINK ET_CATEGORY ET_TITLE
#                 | ET_DESC ET_LINK  ET_TITLE ET_CATEGORY
#                 | ET_CATEGORY ET_DESC ET_TITLE ET_LINK
#                 | ET_CATEGORY ET_TITLE ET_DESC  ET_LINK
#                 | ET_CATEGORY ET_DESC  ET_LINK ET_TITLE
#                 | ET_CATEGORY ET_LINK ET_TITLE ET_DESC
#                 | ET_CATEGORY ET_LINK ET_DESC ET_TITLE
#                 | ET_LINK ET_CATEGORY ET_TITLE ET_DESC
#                 | ET_LINK ET_CATEGORY ET_DESC ET_TITLE
#                 | ET_LINK ET_TITLE ET_DESC ET_CATEGORY
#                 | ET_LINK ET_TITLE ET_CATEGORY ET_DESC
#                 | ET_LINK ET_DESC ET_CATEGORY ET_TITLE
#                 | ET_LINK ET_DESC ET_TITLE ET_CATEGORY
#     '''
#     exportarTxt.append(['Prod. ET_OBL_ITEM -->', p.slice])


def p_error(p):
    # p regresa como un objeto del Lexer.
    # p.__dict__ -> ver propiedades del objeto.
    global contadorErrores
    if (p):
        print(f'Error parser --> Tipo: {p.type} | Valor: {p.value}')
        print('Error sintáctico en LINEA:', p.lineno)
        exportarTxt.append(['Error parser -->', p])
    else:
        exportarTxt.append(['Error parser --> falta `cerrarrss`', None])

    contadorErrores += 1

parser = yacc.yacc()  # Ignorar warnings.
# errorlog=yacc.NullLogger()

opcionesMenu = {
    1: 'Analizar texto desde un archivo, indicando su ruta.',
    2: 'Escanear texto línea por línea (escribiendo en terminal).',
    3: 'Salir.',
}

def analizarPorRuta():
    cleanPath = pedirRuta()
    global contadorErrores
    # Ejecución "analisis de archivo de texto"
    try:
        file = open(cleanPath, "r", encoding='utf8')
        strings = file.read()
        file.close()
        result = parser.parse(strings)
        try:
            with open(f'producciones-analizadas.txt', 'w', encoding='UTF8') as f:
                f.write('Producciones analizadas por el parser\n-----------------\n')
                contador = 0
                for line in exportarTxt:
                    contador += 1
                    f.write(f'{contador}) {line[0]} | {line[1]}\n')
                    f.write('-------------\n')
                f.write('-------------\n')
                f.write(f'Total de tokens analizados: {contador}.\n')
            f.close()
        except:
            print('Error creando logs')
        if contadorErrores > 0:
            print('(⨉) Ocurrió un error sintáctico.')
            # Resetear contador
            contadorErrores = 0
            reload(lexer)
        else:
            print('✅ El archivo es sintacticamente correcto!')
            # Ejecutar exportacion de html
            # exportarHtml(strings, cleanPath)
            print('(✅) Sintácticamente correcto. Se exportó un .html con los comentarios.')
            print('(!) Se exportó un .txt con las producciones analizadas.')
    except IOError:
        print('Ocurrió un error leyendo archivo:', cleanPath)


def analizarPorLinea():
    # Ejecución "normal"
    print(
        'Para interrumpir la ejecucion: [ctrl] + [C] | Para volver al menu principal: _salir')
    while True:
        s = input('>> ')
        if s == '_salir':
            break
        result = parser.parse(s)
        print(result)


if __name__ == "__main__":
    logicaMenu(
        'Parser',
        opcionesMenu,
        analizarPorRuta,
        analizarPorLinea,
    )
