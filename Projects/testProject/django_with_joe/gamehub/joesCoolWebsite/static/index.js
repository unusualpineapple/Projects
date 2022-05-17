var btns = document.querySelectorAll("subresults");
let objDiv = document.getElementById("divExample");
objDiv.scrollTop = objDiv.scrollHeight;
    
for(var i=0; i<btns.length; i++) {
    btns[i].addEventListener("click", function(){
        alert("Button clicked!");
    });
}

function showUpdates(update){
    console.log("Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    var show = document.getElementById(update)
    console.log(show)
    if(show.style.display === "none"){
        (show.style.display = "block")
    }
    else{
        show.style.display = "none"
    }
}





// If you don't know when data comes, you can set an interval:
window.setInterval(function() {
    // var elem = document.getElementById('yourDivWithScrollbar');
    // elem.scrollTop = elem.scrollHeight;
    // }, 5000);
    
  // If you do know when data comes, you can do it like the following:
    var elem = document.getElementById('yourDivWithScrollbar');
    elem.scrollTop = elem.scrollHeight;
})