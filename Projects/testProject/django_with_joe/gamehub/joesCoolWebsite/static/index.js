var btns = document.querySelectorAll("subresults");
    
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