input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let letter = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?"]
    let biconvs = ["000000", "000001", "000010", "000011", "000100", "000101", "000110", "000111", "001000", "001001", "001010", "001011", "001100", "001101", "001110", "001111", "010000", "010001", "010010", "010011", "010100", "010101", "010110", "010111", "011000", "011001", "011010", "011011", "011100", "011101", "011110", "011111", "100000", "100001", "100010", "100011", "100100", "100101", "100110", "100111", "101000", "101001", "101010", "101011", "101100", "101101", "101110", "101111", "110000", "110001", "110010", "110011", "110100", "110101", "110110", "110111", "111000", "111001", "111010", "111011", "111100", "111101", "000000", "111110", "111111"]
    basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
    basic.pause(5000)
    basic.clearScreen()
    let finalletter = ""
    let finalmessage = []
    let messageinbit = []
    let end = 0
    let countingbits = 0
    let letterbit = ""
    let letterconv = []
    let startlight = 0
    let endlight = 150
    while (end != 1) {
        if (input.lightLevel() > 200 && startlight != 1) {
            startlight = 1
            led.plot(0, 4)
            pause(40)
        }
        
        while (startlight == 1) {
            led.unplot(0, 4)
            while (end != 1) {
                if (input.lightLevel() > 10 && input.lightLevel() < 30) {
                    messageinbit.push(0)
                    led.plot(4, 0)
                    pause(50)
                    led.unplot(4, 0)
                } else if (input.lightLevel() > 235 && input.lightLevel() < 255) {
                    messageinbit.push(1)
                    led.plot(0, 0)
                    pause(50)
                    led.unplot(0, 0)
                }
                
                if (input.lightLevel() > 60 && input.lightLevel() < 80) {
                    end = 1
                    startlight = 0
                    led.plot(4, 4)
                    pause(50)
                    led.unplot(4, 4)
                }
                
            }
        }
    }
    for (let i = 0; i < messageinbit.length; i++) {
        letterconv.push(messageinbit)
        countingbits += 1
        if (countingbits == 6) {
            letterbit = _py.py_string_join("", letterconv)
            finalletter = letter[_py.py_array_index(biconvs, letterbit)]
            finalmessage.push(finalletter)
            letterconv = []
            finalletter = ""
        }
        
    }
    pause(5000)
    basic.showString(_py.py_string_join("", finalmessage))
})
