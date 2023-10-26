document.getElementById("search").addEventListener("click",(event) =>{
    let searchInfo = document.getElementById("search-text").value;
    let fail = document.getElementById("fail");
    data =[
        {
            name:"acer",
            price:400,
            os:"ubuntu linux"
        },
        {
            name:"dell",
            price:600,
            os:"ubuntu debian"
        }
]

let name =[]

for (let i = 0; i<data.length;i++){
    name[i] = data[i].name
}

function filtreTexte(arr, requete) {
    return arr.filter(function (el) {
      return el.toLowerCase().indexOf(requete.toLowerCase()) !== -1;
    });
  }
  if (filtreTexte(name,searchInfo).length === 0){
    fail.innerHTML = "FAIL"
  }else{
    console.log(filtreTexte(name,searchInfo));

  }
  
}) 

document.getElementById("search-text").addEventListener("keyup",(e)=>{
    const letter = e.target.value;
    const box = document.getElementsByClassName("box")

console.log(e.target.value);
    data =[
        {
            name:"acer",
            price:400,
            os:"ubuntu linux"
        },
        {
            name:"dell",
            price:600,
            os:"linux debian"
        },
        {
            name:"hp",
            price:300,
            os:"arch linux"
        }
]
let reelName = []
for(i = 0;i<data.length;i++){
    reelName[i] =data[i].name; 
}

function filter(arr, request){
    return arr.filter(function (el){
        return el.toLowerCase().indexOf(request.toLowerCase()) !== -1;
    })
}
if (filter(reelName,letter).length === 0){
    console.error("hello");
}else{
    console.log(filter(reelName,letter));
    const name = filter(reelName,letter);
    const eventName = document.getElementById(name);
    eventName.classList.add("newClass")
}
})