document.getElementById("button")
  .addEventListener("click", (event) => {
    let elementMail = document.getElementById("email");
    let elementUser = document.getElementById("username");
    let elementPass = document.getElementById("password");

    let valueMail = elementMail.value;
    let valueUser = elementUser.value;
    let valuePass = elementPass.value;

    let payload = {
      "mail": valueMail,
      "user": valueUser,
      "pass": valuePass,
    };

    fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })
    .then(async (res) => {
      let value = await res.json();
      console.log("result->", value);
    });

  });
