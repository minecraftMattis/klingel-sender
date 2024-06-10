radio.onReceivedNumber(function (receivedNumber) {
    music.play(music.stringPlayable("C C5 D B F E G E ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(0)
})
radio.setGroup(1)
basic.forever(function () {
    basic.showString("BITTE KLINGELN")
})
