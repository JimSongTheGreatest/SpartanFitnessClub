var start = document.getElementById('start');
var stop  = document.getElementById('stop');
var reset = document.getElementById('reset');

var wh = document.getElementById('w_hours');
var wm = document.getElementById('w_minutes');
var ws = document.getElementById('w_seconds');



//store a reference to a timer variable
var startTimer;

start.addEventListener('click', function(){
    
    //startTimer = setInterval(timer, 1000)
    if(startTimer === undefined){
        startTimer = setInterval(timer, 1000)
    } else {
        alert("Timer is already running, Press Ok to continue");
    }
})

reset.addEventListener('click', function(){
    wh.innerText = "00";
    wm.innerText = "00";
    ws.innerText = "00";

    stopInterval()
    startTimer = undefined;
})

stop.addEventListener('click', function(){
    stopInterval()
    startTimer = undefined;
})


//Start Timer Function
function timer(){
    //Work Timer Countdown
    ws.innerText++;
    
    if (ws.innerText == 60)
    {
        ws.innerText = 00;
        wm.innerText++;
    }
    else if (wm.innerText == 60)
    {
        wm.innerText = 00;
        wh.innerText++;
    }

}

//Stop Timer Function
function stopInterval()
{
    clearInterval(startTimer);
}