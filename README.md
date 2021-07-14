# Gerador de texto de João Guimarães Rosa

Gerador de texto treinado nas obras de João Guimarães Rosa para escrever como o autor. 

O site com resultado do projeto pode ser encontrado [aqui](http://gerador-texto-guimaraes.herokuapp.com/):

[![gerador.png](https://i.postimg.cc/FKHs65LR/gerador.png)](https://postimg.cc/jDBbW1v0)

## Uso
As dependências do projeto estão disponíveis em [requirements.txt](requirements.txt) e podem ser instaladas com o seguinte comando:

```pip install -r requirements.txt```


## Extração de dados 
O corpus foi montado utilizando todas as obras de João Guimarães Rosa, são elas: *Sagarana*, *Corpo de Baile*, *Grande Sertão Veredas*, *Primeiras Estórias*, *Tutameia*, *Estas estórias* e *Ave, palavra*. Os PDFs de todos as obras foram coletados do site [LeLivros](https://lelivros.love).

A extração do texto dos PDFs foi realizada com o arquivo [extract_pdf.py](corpus/extract_pdf.py).

Informações como notas da editora, prefácios e textos teóricos de outros autores sobre os livros foram retirados manualmente. 

## Modelo
A construção do modelo utilizado para criar o gerador de texto está disponível em [geração_texto.ipynb](model/geração_texto.ipynb).


#
Feito por: *[Julia Pocciotti](https://github.com/juliapocciotti)*
