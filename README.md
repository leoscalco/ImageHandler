# ImageHandler

Código para retirar pixels de determinada cor e mesclar imagens.

Foi utilizado a biblioteca PIL, para montar funções de retirada de pixels de determinada cor e para mesclas duas imagens.

Como usar:

Invocar a class ImageHandler, passando por paramentro a tolerância.
ih = ImageHandler(80) 

Abrir imagem com PIL, passando o PATH da imagem.
im = pil_im.open("images/inputs/fundoVerde.jpg")

Definir cor que se deseja retirar.
color = [1, 255, 2]

Método invocado para retirar cor da imagem, respeitando tolerância.
ih.remove_background(im, color)

Abrir background.
back_im = pil_im.open("images/inputs/background.jpg")

Aplicar background na imagem passada anteriormente.
ih.put_background(back_im)
