const squares = document.querySelectorAll('.square')
const mole = document.querySelector('.mole')
const time = document.querySelector('#timeLeft')
const score = document.querySelector('#score')
const button = document.querySelector('.start')

let result = 0
let hitPosition
let currentTime = 10
let timerId = null

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
            hitPosition = null
        }
    })
})

function moveMole(){

    timerId = setInterval(randomSquare, 500)
}



function countDown() {
    currentTime--
    time.textContent = currentTime
    
    if (Math.floor(currentTime) === 0){
        clearInterval(countDownTimerId)
        clearInterval(timerId)
        alert('GAME OVER your score is ' + result)
    }
}
// let countDownTimerId = setInterval()

function StartGame() {
    console.log("beginning function")
    if (currentTime == 10){
        moveMole()
        countDownTimerId = setInterval(countDown, 1000)
        console.log("end function")
    }
    }


function Restart(){
    console.log("Printed")
    if (currentTime == 0){
        clearInterval(countDownTimerId)
        clearInterval(timerId)
    console.log(timerId)
    }
}
button.addEventListener('start',startGame)

function EndGame(){
    console.log("hey this is good")
    if (currentTime == 0){
        
    }
}
// sessionStorage.removeItem('mole')