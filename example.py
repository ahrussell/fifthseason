import json

from composer import Composer
from constants import PIECES

# compose 4 pieces each in the style of each season
for piece, file in PIECES.iteritems():
    bot = Composer({piece: file})
    markov_piece = bot.measurify(bot.write(350), 4, 4)
    
    with open("output/json/" + piece + ".json", "w") as fp:
    
        json.dump(markov_piece, fp)

# write a fifth piece in the style of all 4 seasons
bot = Composer(PIECES)
markov_piece = bot.measurify(bot.write(350), 4, 4)

with open("output/json/" + piece + ".json", "w") as fp:

    json.dump(markov_piece, fp)
