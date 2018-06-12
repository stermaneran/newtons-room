# // The colors to blend
# source = {'r': 255, 'g': 213, 'b': 0, 'a': 0.6}
# backdrop = {'r': 141, 'g': 214, 'b': 214, 'a': 0.6}

def colorme(colors):
# // This example shows the result of blending 'source' and 'backdrop' with the 'hue' blending mode, according to the W3C or Adobe spec
# // However the composite could also be calculated by 'saturation', 'color' or 'luminosity' mode
#     data = [1,2,3,4,5,6]
#     for i,k in zip(data[0::2], data[1::2]):
#         print (str(i), '+', str(k), '=', str(i+k))
    first = True
    source = {'r': colors[0][0], 'g': colors[0][1], 'b': colors[0][2], 'a': colors[0][3]}
    for c in colors:
        if first:
            first = False
        else:
            backdrop = {'r': c[0], 'g': c[1], 'b': c[2], 'a': c[3]}

            # // The mentioned colour compositing formula as a function
            def colourCompositingFormula(a, ab, ar, Cs, Cb, Bbs):
                return (1 - (a / ar)) * Cb + (a / ar) * round((1 - ab) * Cs + ab * Bbs)

            # // Calculate the opacity of the result
            resultingAlpha = source['a'] + backdrop['a'] * (1 - source['a'])

            source = {
                # // Adobe PDF Format Part 1 - page 328
                'r': colourCompositingFormula(source['a'], backdrop['a'], resultingAlpha, source['r'], backdrop['r'], resultingAlpha),
                'g': colourCompositingFormula(source['a'], backdrop['a'], resultingAlpha, source['g'], backdrop['g'], resultingAlpha),
                'b': colourCompositingFormula(source['a'], backdrop['a'], resultingAlpha, source['b'], backdrop['b'], resultingAlpha),
                'a': resultingAlpha
            }

    return source['r'], source['g'], source['b']