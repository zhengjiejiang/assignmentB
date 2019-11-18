function onRegisterClick() {
    const firstNameObject = document.getElementById("first_name")
    const firstName = firstNameObject.value;
    const lastName = document.getElementById("last_name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;
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
  xhttp.send("first_name="+firstName+"&last_name="+lastName+"&email="+email+"&username="+username+"&password="+password);
}
