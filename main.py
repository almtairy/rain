rain: game.LedSprite = None
rain1: game.LedSprite = None
rain2: game.LedSprite = None

def on_forever():
    global rain, rain1, rain2
    rain = game.create_sprite(randint(0, 4), 0)
    rain1 = game.create_sprite(randint(0, 4), 0)
    rain2 = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        rain.change(LedSpriteProperty.Y, 1)
        rain1.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
        rain2.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
    rain.delete()
    rain1.delete()
    rain2.delete()
basic.forever(on_forever)
