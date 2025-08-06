# 🖼️ apply_watermark

Um script de linha de comando em Python para aplicar uma **marca d'água em padrão de repetição (tile)** sobre imagens de uma pasta.

---

## 📦 Requisitos

- Python 3.8 ou superior
- [Pillow](https://pypi.org/project/Pillow/)
- [Typer](https://pypi.org/project/typer/)

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como usar

```bash
python main.py \
 --input ./in \
 --output ./out \
 --error ./erro \
 --watermark ./watermark.png \
 --opacity 0.8 \
 --spacing 50 \
 --watermark-scale 0.2 \
 --max-width 800 \
 --max-height 800
```

```bash
⚙️ Parâmetros
Parâmetro Descrição
--input, -i Caminho da pasta de entrada com as imagens
--output, -o Caminho da pasta de saída para imagens processadas
--error, -e Pasta para mover imagens com erro durante o processo
--watermark, -w Caminho da imagem .png com transparência que será usada como marca d’água
--opacity, -p Opacidade da marca d água (0.0 a 1.0). Ex: 0.3 para 30%
--spacing, -s Espaçamento entre cada marca d’água repetida na imagem
--watermark-scale, -ws Escala da marca d’água (ex: 0.5 = 50%, 2.0 = 200%)
--max-width Largura máxima da imagem de saída (0 para não redimensionar)
--max-height Altura máxima da imagem de saída (0 para não redimensionar)
```

## 🖼️ Exemplo prático

```bash
python main.py --input ./in --output ./out --error ./error --watermark ./watermark.png --opacity 0.8 --spacing 50 --watermark-scale 0.2  --max-width 1024 --max-height 768
```

Esse comando:

Aplica a imagem watermark.png com 50% de opacidade,

Escala a marca d'água para 40% do tamanho original,

Adiciona espaçamento de 30px entre cada repetição da marca,

Redimensiona a imagem original para no máximo 1024x768,

Move imagens com erro para a pasta erro.

## 🧼 Comportamento

As imagens de entrada são removidas após o processamento com sucesso.

Imagens com erro são movidas para a pasta de erro (caso definida).

## 🧪 Logs

O script imprime logs no terminal:

INFO: Indica progresso e redimensionamento.

ERROR: Mostra falhas de leitura, escrita ou formatação.

## 🧊 Dica

Use marcas d’água .png com fundo transparente para melhor resultado.
