document.onscroll = function(){
    if(window.scrollY > 20) {
        document.getElementById('headerInSide').style.background='rgba(235, 235, 235, 0.795)';
    }
    else 
        document.getElementById('headerInSide').style.background='';
}

