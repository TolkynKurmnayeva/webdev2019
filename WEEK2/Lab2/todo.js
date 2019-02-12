
function addItem() {
    
    var inputValue = document.getElementById("new-item").value;
    
    if(inputValue=== '')
     return;

    var li = document.createElement("li");
    li.className="elements";
    li.append(document.createTextNode(inputValue));

    li.onclick = function () {
        if(this.style.textDecoration =="line-through"){
                this.style.textDecoration ="none";
                this.style.background ="salmon";
        }
        else {
                this.style.textDecoration ="line-through";
                this.style.background ="rosybrown";
        }
    }

    document.getElementById("new-item").value = "";


    var button = document.createElement("button");
    button.type="button";
    
    button.onclick= function (){
        this.parentNode.style.display = 'none';
    }
    button.innerText='✖';
    li.appendChild(button);
    document.getElementById("ulist").appendChild(li);
}
