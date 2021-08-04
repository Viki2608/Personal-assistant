import screen_brightness_control as sbc


def increase_brightness():
    sbc.set_brightness(100)


def zero_brightness():
    sbc.set_brightness(0)


def increase_brightness():
    sbc.set_brightness('+25')


def decrease_brightness():
    sbc.set_brightness('-25')


def half_brightness():
    sbc.set_brightness('50')
