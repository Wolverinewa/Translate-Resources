from deep_translator import GoogleTranslator
import xml.etree.ElementTree as ET

# Caminho para o arquivo .resx original
file_path = 'FrmProductionMessages.pt-BR.resx'

output_path = 'FrmProductionMessages.it-IT.resx'

# Carregar o arquivo .resx
tree = ET.parse(file_path)
root = tree.getroot()

# Inicializar o tradutor
translator = GoogleTranslator(source='pt', target='it')

# Traduzir todos os elementos <value> para o idioma italiano
for data in root.findall('data'):
    value_element = data.find('value')
    if value_element is not None and value_element.text:
        # Traduzir o texto para italiano
        translated_text = translator.translate(value_element.text)
        value_element.text = translated_text

# Salvar o arquivo traduzido
tree.write(output_path, encoding='utf-8', xml_declaration=True)

print(f"Arquivo traduzido salvo como: {output_path}")

output_path = 'FrmProductionMessages.es-ES.resx'

# Carregar o arquivo .resx
tree = ET.parse(file_path)
root = tree.getroot()

# Inicializar o tradutor
translator = GoogleTranslator(source='pt', target='es')

# Traduzir todos os elementos <value> para o idioma italiano
for data in root.findall('data'):
    value_element = data.find('value')
    if value_element is not None and value_element.text:
        # Traduzir o texto para italiano
        translated_text = translator.translate(value_element.text)
        value_element.text = translated_text

# Salvar o arquivo traduzido
tree.write(output_path, encoding='utf-8', xml_declaration=True)

print(f"Arquivo traduzido salvo como: {output_path}")

output_path = 'FrmProductionMessages.en.resx'

# Carregar o arquivo .resx
tree = ET.parse(file_path)
root = tree.getroot()

# Inicializar o tradutor
translator = GoogleTranslator(source='pt', target='en')

# Traduzir todos os elementos <value> para o idioma italiano
for data in root.findall('data'):
    value_element = data.find('value')
    if value_element is not None and value_element.text:
        # Traduzir o texto para italiano
        translated_text = translator.translate(value_element.text)
        value_element.text = translated_text

# Salvar o arquivo traduzido
tree.write(output_path, encoding='utf-8', xml_declaration=True)

print(f"Arquivo traduzido salvo como: {output_path}")
