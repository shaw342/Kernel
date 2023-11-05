document.getElementById("button-n-2").addEventListener("click",(event) =>{
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    let email = document.getElementById("mail")
  
    let valuePass = password.value;
    let valueUser = username.value;
    let valueMail = email.value;
    event.preventDefault();
    console.log(valueMail);
    console.log(valueUser);
    console.log(valuePass);

    let playload = {
        "pass":valuePass,
        "user":valueUser,
        "mail":valueMail
    }
    fetch("/success",{
        method : "POST",
        headers :{
            "Content-Type": "application/json",
        },
        body:JSON.stringify(playload),
    }
    )
    .then(async (res) =>{
        let value = await res.json()
        console.log("result", value);
        window.location.href = "/base"
    });
    
});