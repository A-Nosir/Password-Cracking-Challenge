function init(){
    initCollapsible();
}

function initCollapsible(){
    var coll = document.getElementsByClassName("collapsible");
      var i;
      
      for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
          this.classList.toggle("active");
          var content = this.nextElementSibling;
          if (content.style.display === "block") {
            content.style.display = "none";
          } else {
            content.style.display = "block";
          }
        });
      }
    return;
}

function login(){ 
    var cnum = document.getElementById("cnum").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(cnum == false || username == false || password == false){
        alert("Please fill out all the text boxes");
        return;
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.response);
            let result = JSON.parse(this.response);
            console.log(result);
            if(result.passed === true){
                alert("Congrats!! You solved the challenge!");
            } else {
                alert("Your login attempt was incorrect");
            }
            
        }
    }
    xhttp.open("GET", window.location.href+ `/login?cnum=${cnum}&username=${username}&password=${password}`, true);
    xhttp.send();
}