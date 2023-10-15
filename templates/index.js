
let username = document.getElementById("username")
let email = document.getElementById("email")
let password = document.getElementById("password")

let data = {
    username:username,
    email:email,
    password:password,
} 

url = "http://localhost:8000/logout"
fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data)
    
  })
  .catch(error => {
    console.error(error)
  });