const employeeId = document.getElementById("username");
const password = document.getElementById("password");


async function login(){
    localStorage.setItem("id", employeeId.value);

    let response  = await fetch("http://127.0.0.1:5000/employee/login", {

        method:"POST", 
        mode : "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            employeeId: employeeId.value,
            password: password.value
        })
    }
)
    if (response.status === 200){
        let body = await response.json()
        console.log(body)
        if (employeeId.value != 1){
            window.location.href = "page2.html"
        } else {
            // window.open("page3.html")
            window.location.href = "page3.html"
        }
        
    } else {
        alert("Bad Login Credentials.  You're as bad as Spiderman!  Try Again.")
    }
}

