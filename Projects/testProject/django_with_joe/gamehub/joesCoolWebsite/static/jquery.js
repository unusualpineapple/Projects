var btns = document.querySelectorAll("subresults");
    
for(var i=0; i<btns.length; i++) {
    btns[i].addEventListener("click", function(){
        alert("Button clicked!");
    });
}