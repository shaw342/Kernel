let count = 0;
document.getElementById("add_basket").addEventListener("click", (e) => {
    count++;
    let names = document.getElementsByClassName("name");
    let oses = document.getElementsByClassName("os");
    let prices = document.getElementsByClassName("price");

    let data = {
        name: names[0].textContent, 
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
        console.log(value);
    })
})
