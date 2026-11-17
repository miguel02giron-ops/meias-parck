"""Cria a árvore de diretórios da loja de meias.

Uso:
    python arquivo.py            # cria em ./loja-de-meias
    python arquivo.py meu-destino
"""

import sys
from pathlib import Path

RAIZ = "loja-de-meias"

PASTAS = [
    "docs/identidade-visual",
    "catalogo/meias-casuais/listradas",
    "catalogo/meias-casuais/estampadas",
    "catalogo/meias-casuais/lisas",
    "catalogo/meias-esportivas/cano-curto",
    "catalogo/meias-esportivas/cano-alto",
    "catalogo/meias-esportivas/compressao",
    "catalogo/meias-sociais",
    "catalogo/meias-termicas",
    "catalogo/meias-infantis",
    "catalogo/meias-divertidas/animais",
    "catalogo/meias-divertidas/frutas",
    "catalogo/meias-divertidas/edicoes-limitadas",
    "catalogo/kits-presente",
    "estoque/entradas",
    "estoque/saidas",
    "estoque/inventario",
    "fornecedores/contratos",
    "fornecedores/pedidos-de-compra",
    "vendas/pedidos",
    "vendas/clientes",
    "vendas/devolucoes-trocas",
    "vendas/relatorios",
    "marketing/campanhas/dia-dos-namorados",
    "marketing/campanhas/black-friday",
    "marketing/campanhas/natal",
    "marketing/redes-sociais",
    "marketing/fotos-produtos",
    "marketing/email-newsletter",
    "site/public/imagens",
    "site/public/fontes",
    "site/src/componentes",
    "site/src/paginas",
    "site/src/estilos",
    "logistica/embalagens",
    "logistica/transportadoras",
    "logistica/etiquetas-de-envio",
    "financeiro/notas-fiscais",
    "financeiro/contas-a-pagar",
    "financeiro/contas-a-receber",
]

ARQUIVOS = {
    "README.md": "# Loja de Meias\n",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n.DS_Store\nnode_modules/\n",
    "docs/plano-de-negocios.md": "# Plano de Negócios\n",
}


def criar_arvore(base: Path) -> None:
    for pasta in PASTAS:
        (base / pasta).mkdir(parents=True, exist_ok=True)

    for caminho, conteudo in ARQUIVOS.items():
        arquivo = base / caminho
        arquivo.parent.mkdir(parents=True, exist_ok=True)
        if not arquivo.exists():
            arquivo.write_text(conteudo, encoding="utf-8")


if __name__ == "__main__":
    destino = Path(sys.argv[1] if len(sys.argv) > 1 else RAIZ)
    criar_arvore(destino)
    print(f"Árvore criada em: {destino.resolve()}")
