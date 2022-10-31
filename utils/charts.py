import random

months = [
    'ENERO', 'FEBRERO', 'MARZO', 'ABRIL',
    'MAYO', 'JUNIO', 'JULIO', 'AGOSTO',
    'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'
]


""" colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#FF5733',
                '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8',
                '#FFF933', '#C4FF33', '#4FFF33', '#33FFF0'] """


def generate_color_palette(amount):
    colorPalette = []
    for j in range(10):
        colors = '#'+''.join([random.choice('abcdef0123456789')
                              for i in range(6)])
        colorPalette.append(colors)
    palette = []
    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette
