def on_button_pressed_a():
    
    letter = [" ",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "?"]
    biconvs = ["000000",
        "000001",
        "000010",
        "000011",
        "000100",
        "000101",
        "000110",
        "000111",
        "001000",
        "001001",
        "001010",
        "001011",
        "001100",
        "001101",
        "001110",
        "001111",
        "010000",
        "010001",
        "010010",
        "010011",
        "010100",
        "010101",
        "010110",
        "010111",
        "011000",
        "011001",
        "011010",
        "011011",
        "011100",
        "011101",
        "011110",
        "011111",
        "100000",
        "100001",
        "100010",
        "100011",
        "100100",
        "100101",
        "100110",
        "100111",
        "101000",
        "101001",
        "101010",
        "101011",
        "101100",
        "101101",
        "101110",
        "101111",
        "110000",
        "110001",
        "110010",
        "110011",
        "110100",
        "110101",
        "110110",
        "110111",
        "111000",
        "111001",
        "111010",
        "111011",
        "111100",
        "111101",
        "000000",
        "111110",
        "111111"]
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
    basic.pause(5000)

    basic.clear_screen()
    finalletter = ""
    finalmessage = []
    messageinbit = []
    end = 0
    countingbits = 0
    letterbit = ""
    letterconv = []
    startlight = 0
    endlight = 150
    
    while end != 1:
        if input.light_level() > 200 and startlight != 1:
            startlight = 1
            led.plot(0,4 )
            pause(40)
        while startlight == 1:
            led.unplot(0,4)
            while end != 1:
                if input.light_level() > 10 and input.light_level() < 30:
                    messageinbit.append(0)
                    led.plot(4,0)
                    pause(50)
                    led.unplot(4, 0)
                elif input.light_level() > 235 and input.light_level() < 255:
                    messageinbit.append(1)
                    led.plot(0, 0)
                    pause(50)
                    led.unplot(0, 0)
                if input.light_level() >60 and input.light_level() <80:
                    end=1
                    startlight=0
                    led.plot(4,4)
                    pause(50)
                    led.unplot(4, 4)
    for i in range(len(messageinbit)):
        letterconv.append(messageinbit)
        countingbits += 1
        if countingbits == 6:
            letterbit = "".join(letterconv)
            finalletter = letter[biconvs.index(letterbit)]
            finalmessage.append(finalletter)
            letterconv = []
            finalletter = ""
    pause(5000)
    basic.show_string("".join(finalmessage))

input.on_button_pressed(Button.A, on_button_pressed_a)