function onLoginClick(){
  const usernameElement = document.getElementById("username");
  const username = usernameElement.value;
  console.log(username);
  const passwordElement = document.getElementById("password");
  const password = passwordElement.value;
  console.log(password);

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 400){
      alert("username or password incorrect")
    }


    else if (this.readyState == 4 && this.status == 201{

        window.location.href = "/dashboard"
      }
    }

    xhttp.open("POST", "{% url 'login_api' %}", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("username="+username+"&password="+password);
    }
