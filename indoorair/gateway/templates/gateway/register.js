function onRegisterClick(){
  const firstName = document.getElementById("first_name").value
  const lastName = document.getElementById("last_name").value
  const userName = document.getElementById("username").value
  const password = document.getElementById("password").value
  const email = document.getElementById("email").value
  console.log(firstName)


  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 400){
      alert("username or password incorrect")
    }
    else if (this.readyState == 4 && this.status == 201) { // Thisis the callback function
           // Get the string data that the server sent us.
           window.location.href = "{% url 'registered_page' %}";

       }
   }
  xhttp.open('POST',"{% url 'register_api' %}", true)
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("last_name="+lastName+"&first_name="+firstName +"&username="+ userName + "&password="+password +"&email="+ email);
}
