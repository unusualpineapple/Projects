const squares = document.querySelectorAll('.square')
const mole = document.querySelector('.mole')
const time = document.querySelector('#timeLeft')
const score = document.querySelector('#score')
const button = document.querySelector('.start')



let result = 0
let hitPosition
let currentTime = 10
let timerId = null
let countDownTimerId

var startGame = document.getElementById(startGame);



function randomSquare() {
    squares.forEach(square => {
        square.classList.remove('mole')
    })
    
    let randomSquare = squares[Math.floor(Math.random() * 9)]
    randomSquare.classList.add('mole')

    hitPosition = randomSquare.id
}

squares.forEach(square => {
    square.addEventListener('mousedown', () => {
        if (square.id == hitPosition) {
            result++
            score.textContent = result
            var tester = document.querySelector("#test")
            tester.setAttribute("value", result)
            hitPosition = null
        }
    })
})

function moveMole(){

    timerId = setInterval(randomSquare, 500)
}


// function countDown(){
//     currentTime--
//     tim
// }


// function countDown(timer) {
    // if (timer <= 0) {
    //     clearInterval(countDownTimerId);
    //     clearInterval(timer);
    //     return
    // }
//     timer--
// }


function StartGame() {
    console.log("this is the timeinner" + time.innerHTML)
    console.log("beginning function")
    let count = time.innerHTML
    if (count > 0){
        moveMole()
        countDownTimerId = setInterval(function(){
            count--;
            time.innerHTML--;
            if (count == 0){
                clearInterval(countDownTimerId)
                clearInterval(timerId)
                return
            } 
        }, 1000)

        console.log(count)


    
    if (count === 0){
        clearInterval(countDownTimerId)
        clearInterval(time.innerHTML)
    }
    }
    console.log("this is ther html" + time.innerHTML)
    }


function Restart(){
    console.log("Printed")
    // if (currentTime == 0){
    //     clearInterval(countDownTimerId)
    //     clearInterval(timerId)
    document.getElementById('score').innerHTML = 0
    // console.log(timerId)
    button.addEventListener('start',startGame)
    }
// }

function EndGame(){
    console.log("hey this is good")
    clearInterval
}
// sessionStorage.removeItem('mole')

var data = {
    'gamescore':{
        "score" : result
    }
}

console.log(typeof(data))
console.log(Array.isArray(data))
console.log(Array.isArray(data.gamescore))

console.log(data[gamescore][0].score)