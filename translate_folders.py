import os
from deep_translator import GoogleTranslator
import xml.etree.ElementTree as ET

def traduzir_resx(file_path, output_path, source_lang, target_lang):
    """
    Traduz um arquivo .resx para o idioma alvo.
    :param file_path: Caminho do arquivo .resx original.
    :param output_path: Caminho do arquivo .resx traduzido.
    :param source_lang: Idioma de origem (ex.: 'pt').
    :param target_lang: Idioma de destino (ex.: 'it').
    """
    try:
        # Carregar o arquivo .resx
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Inicializar o tradutor
        translator = GoogleTranslator(source=source_lang, target=target_lang)

        # Traduzir todos os elementos <value>
        for data in root.findall('data'):
            value_element = data.find('value')
            if value_element is not None and value_element.text:
                try:
                    # Traduzir o texto
                    translated_text = translator.translate(value_element.text)
                    value_element.text = translated_text
                    print(f"Traduzido [{target_lang}]: '{value_element.text}' -> '{translated_text}'")
                except Exception as e:
                    print(f"Erro ao traduzir '{value_element.text}': {e}")

        # Salvar o arquivo traduzido
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
        print(f"Arquivo traduzido salvo como: {output_path}")
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")

# Caminho para a pasta principal
base_folder = 'FormMessages'

# Idiomas e caminhos de saída
idiomas = ['it', 'es', 'en']  # Lista de idiomas de destino

# Percorrer a estrutura de pastas
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.endswith('.resx'):
            file_path = os.path.join(root, file)
            for lang in idiomas:
                # Nomear o arquivo traduzido com o idioma de destino
                output_path = os.path.join(root, f"{os.path.splitext(file)[0]}.{lang}.resx")
                traduzir_resx(file_path, output_path, 'pt', lang)
