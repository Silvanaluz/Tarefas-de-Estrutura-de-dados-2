
import re
import time
from avl import AVL

def processar_texto(caminho_arquivo):
    arvore = AVL()
    inicio = time.time()
     
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for num_linha, linha in enumerate(f, 1):
            # Regex para pegar apenas palavras (letras a-z e acentos)
            palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", linha.lower())
            for p in palavras:
                arvore.raiz = arvore.inserir(arvore.raiz, p, num_linha)
    fim = time.time()
    return arvore, (fim - inicio)

def main():

    arquivo = "proverbiosB.txt" 
    
    print(f"Processando '{arquivo}'...")
    arvore, tempo = processar_texto(arquivo)
    
    if not arvore: return

    # --- Teste 1: Busca com ME ---
    print("\n--- Teste 1: buscar_com_me ---")
    termo = "sabedoria" 
    status = arvore.buscar_com_me(termo)
    if status == -1: print(f"A palavra '{termo}' não foi encontrada.")
    elif status == 0: print(f"A palavra '{termo}' foi encontrada e o ME é zero.")
    else: print(f"A palavra '{termo}' existe (ME impresso acima).")

    # --- Teste 2: Busca por Prefixo ---
    prefixo = "pro" 
    print(f"\n--- Teste 2: buscar_prefixo ('{prefixo}') ---")
    print(arvore.buscar_prefixo(prefixo))

    # --- Teste 3: Palavra mais frequente ---
    freq = arvore.palavra_mais_frequente()
    if freq:
        print(f"\n--- Teste 3: Palavra mais frequente ---")
        print(f"Palavra: '{freq.palavra}' | Aparece em {len(freq.linhas)} linhas.")

    # --- 4. Imprimir Índice Completo na Tela ---
    arvore.imprimir_indice_completo(tempo)

if __name__ == "__main__":
    main()