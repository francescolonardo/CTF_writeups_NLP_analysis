## Trapped Source
> Solved by Starry-Lord

![challenge description](https://i.imgur.com/QhaEep8.png)


When we open the devtools and check the network tab, we can already catch a script.js:

![network tab](https://i.imgur.com/hV9DZ4t.png)


script.js content:


    currentPin = []
    
    const checkPin = () => {
            pin = currentPin.join('')
    
            if (CONFIG.correctPin == pin) {
                    fetch('/flag', {
                            method: 'POST',
                            headers: {
                                    'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                    'pin': CONFIG.correctPin
                            })
                    })
                    .then((data) => data.json())
                    .then((res) => {
                            $('.lockStatus').css('font-size', '8px')
                            $('.lockStatus').text(res.message)
                    })
                    return
            }
    
            $('.lockStatus').text('INVALID!')
            setTimeout(() => {
                    reset()
            }, 3000)
    
    }
    
    const unlock = (pin) => {
            currentPin.push(pin)
    
            if (currentPin.length > 4) return
    
            $('.lockStatus').text(currentPin.join(' '))
    }
    
    const reset = () => {
            currentPin.length = 0
            $('.lockStatus').css('font-size', 'x-large')
    
            $('.lockStatus').text('LOCKED')
    }

We can see some code that checks for a 4 digit pin and fetches the flag, depending on the pin being equal to the value of “CONFIG.correctPin” or not. Switching to the console, we can try and log the “CONFIG”, to see what comes back:


![get variables](https://i.imgur.com/0NPqIRJ.png)


Typing the correct pin and pressing enter returns our flag:


![flag for this challenge](https://i.imgur.com/YmTsLrt.png)
