import time
import googletrans
translator = googletrans.Translator()

def translate(text,target_language):
    translated_text = translator.translate(text,dest=target_language)
    return translated_text.text
def get_lang():
    print("\nInsira o codigo do idioma para qual deseja traduzir\ncaso não saiba o codigo insira /h para ver a lista de codigos\n")
    lang = str(input(''))
    if lang == '/h':
        print('\n'+'codigo : idioma'+'\n')
        for key, value in googletrans.LANGUAGES.items():
            print(key, ":", value)
        return get_lang()
        
    elif lang in googletrans.LANGUAGES.keys():
        return lang
    else:
        print('codigo invalido')
        time.sleep(1)
        return get_lang()

print("Insira oque deseja traduzir:")
text = str(input(''))
lang = get_lang()
print('\n'+translate(text,lang))