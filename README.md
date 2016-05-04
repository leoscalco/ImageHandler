# ImageHandler

Código para retirar pixels de determinada cor e mesclar imagens.

Foi utilizado a biblioteca PIL, para montar funções de retirada de pixels de determinada cor e para mesclas duas imagens.

Como usar:

Invocar a class ImageHandler, passando por paramentro a tolerância.

Abrir imagem com PIL, passando o PATH da imagem.

Definir cor que se deseja retirar.

Invocar método para retirar cor da imagem, respeitando tolerância.

Abrir background.

Aplicar background na imagem passada anteriormente.

ih = ImageHandler(80) 

im = pil_im.open("images/inputs/fundoVerde.jpg")

color = [1, 255, 2]

ih.remove_background(im, color)

back_im = pil_im.open("images/inputs/background.jpg")

ih.put_background(back_im)
