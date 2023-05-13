let rain: game.LedSprite = null
let rain1: game.LedSprite = null
let rain2: game.LedSprite = null
basic.forever(function () {
    rain = game.createSprite(randint(0, 4), 0)
    rain1 = game.createSprite(randint(0, 4), 0)
    rain2 = game.createSprite(randint(0, 4), 0)
    for (let index = 0; index < 4; index++) {
        rain.change(LedSpriteProperty.Y, 1)
        rain1.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
        rain2.change(LedSpriteProperty.Y, 1)
        basic.pause(25)
    }
    rain.delete()
    rain1.delete()
    rain2.delete()
})
