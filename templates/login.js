/*document.getElementById("button-n-2").addEventListener("click",(event) =>{
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
        console.log(value);
        document.cookie = "token="+value+"; SameSite=None; Secure;path=/base"
        console.log(document.cookie);
        window.location.href = "/base"
    });
    
});*/
document.getElementsByClassName("login-submit")[0].addEventListener("click", function(event) {
    let username = document.getElementById("exampleInputUsername");
    let password = document.getElementById("exampleInputPassword1");
    let email = document.getElementById("exampleInputEmail1")
  
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
        console.log(value);
        document.cookie = "token="+value+"; SameSite=None; Secure;path=/base"
        console.log(document.cookie);
        window.location.href = "/base"
    });
});