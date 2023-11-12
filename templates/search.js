/*let count = 0;
document.querySelector(".add_basket").addEventListener("click", (e) => {
    let names = document.getElementsByClassName("name");
    let oses = document.getElementsByClassName("os");
    let prices = document.getElementsByClassName("price");
    console.log(document.cookie);
    let data = {
        name:names[0].textContent, 
        os:  oses[0].textContent, 
        price: prices[0].textContent, 
        quantity:count,
    }

    fetch("/Orders",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(data),
    }).then(async (res)=>{
        let value = res.json()
    })
})*/
const searchBar = document.querySelector("#search-text");

searchBar.addEventListener("keyup",(e)=>{
    const searchLetters = e.target.value;
    const card = document.querySelectorAll(".box");
    filterElement(searchLetters,card);

})

function  filterElement(letter, elements) {
        for(let i = 0;i<elements.length;i++){
            if(elements[i].textContent.toLowerCase().includes(letter)){
                elements[i].style.display = "block";
            }else{
                elements[i].style.display = "none";
            }
        }
        
    
}

let count = 0;
let numberOfPurchases = 0;

const addToCartButtons = document.querySelectorAll('.add_basket');

addToCartButtons.forEach(button => {
    button.addEventListener('click', function() {
        let numberOfPurchases = 0;
        const name = button.getAttribute("data-name")
        const os = button.getAttribute("data-os")
        const price = button.getAttribute("data-price")
        console.log(name);
    
        function getCookie(cname) {
            let name = cname + "=";
            let decodedCookie = decodeURIComponent(document.cookie);
            let ca = decodedCookie.split(';');
            for(let i = 0; i <ca.length; i++) {
              let c = ca[i];
              while (c.charAt(0) == ' ') {
                c = c.substring(1);
              }
              if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
              }
            }
            return "";
          }

          token = getCookie("token")
          console.log(token);
        const data = {
            "token":token,
            name: name,
            os: os,
            price: price,
            quantity: count // Utilisation de la variable 'count'
        };

    if (data["token"] !== "") {
        
        fetch("/Orders", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }).then(async (res) => {
            let value = await res.json();
            //document.cookie = "token=" + token ";
            // Faites quelque chose avec la réponse 'value' si nécessaire
            numberOfPurchases += 1;
            updateCartCount()
            document.cookie = "username="+token+";SameSite=None; secure;path=/bucket"
        }).catch(error => {
            console.error('Erreur :', error);
        });
    }
    });

});

const details = document.getElementsByClassName("details");

for (let i = 0; i < details.length; i++) {
  details[i].addEventListener("click", (e) => {
    const detailsText = document.getElementById("text_details");
    detailsText.style.backgroundColor = "black";
  });
}

function updateCartCount() {
    const cartCountElement = document.getElementById('cart_count');
    cartCountElement.textContent = numberOfPurchases.toString();
}

numberOfPurchases += 1;