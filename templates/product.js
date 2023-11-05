document.getElementById("button_address").addEventListener("click",(event)=>{
    console.log("hello");
    let state = document.getElementById("state");
    let country = document.getElementById("country");
    let postalNumber = document.getElementById("postal_number");

    let address_data = {
        state:state,
        country:country,
        postalNumber:postalNumber
    }
    fetch("/address_save",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify(address_data)
    }).then(async (res) =>{
        let value = await res.json();
    })
})