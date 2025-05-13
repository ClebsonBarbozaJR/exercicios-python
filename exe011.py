largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('A dimensão da sua parede é de {}x{} e sua área de {}m2'.format(largura,altura,area))
tinta = area / 3
print('Sua parede precisa de {}l de tinta para ser pintada.'.format(tinta))