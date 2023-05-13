def on_forever():
    rain = game.create_sprite(randint(0, 4), 0)
    rain1 = game.create_sprite(randint(0, 4), 0)
    rain2 = game.create_sprite(randint(0, 4), 0)
    for i in range(4):
        rain.change(LedSpriteProperty.Y, 1)
        rain1.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
        rain2.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
    rain.delete()
    rain1.delete()
    rain2.delete()
basic.forever(on_forever)

