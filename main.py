def on_received_number(receivedNumber):
    music.play(music.string_playable("C C5 D B F E G E ", 120),
        music.PlaybackMode.UNTIL_DONE)
radio.on_received_number(on_received_number)

def on_button_pressed_b():
    radio.send_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)

def on_forever():
    basic.show_string("bitte klingeln")
basic.forever(on_forever)
