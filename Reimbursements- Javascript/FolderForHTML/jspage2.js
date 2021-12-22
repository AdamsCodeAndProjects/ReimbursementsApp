
// const header = document.createElement("h1");
// header.textContent = `Your login was successful`;
// document.body.appendChild(header);


function logout(){
    sessionStorage.clear();
    window.location.href = "trial.html"
}

function greeting(){

}

let inputBox = document.getElementById("amount");
let invalidChars = ["-", "+", "e", "E"];
inputBox.addEventListener("keydown", function(e){
    if (invalidChars.includes(e.key)){
        e.preventDefault();
    }
})

async function createRequest(){
    const employee = document.getElementById("employee");
    const amount = document.getElementById("amount");
    const reason = document.getElementById("reason");
    const todaysDate = document.getElementById("date");
    // console.log({
    //     transactionId: "default",
    //     employeeId: employee.value,
    //     reimbursementAmount: amount.value,
    //     expenseReason: reason.value,
    //     status: "pending",
    //     managerComment: "NA",
    //     date: todaysDate.value
    // })
    let response  = await fetch("http://127.0.0.1:5000/reimbursements/create", { 

        method:"POST", 
        mode : "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            transactionId: "default",
            employeeId: Number(employee.value),
            reimbursementAmount: Number(amount.value),
            expenseReason: reason.value,
            status: "pending",
            managerComment: "NA",
            date: todaysDate.value
        })
    }
)
    if (amount.value < 0) {
        console.log(amount.value)
        console.log(amount)
        alert("Cannot request negative amounts!")
    }
    if (amount.value != Number) {
        alert("Must request real amount!")
    } else if(amount.value == e){
        alert("Don't request this")
    } else if (response.status === 200) {
        let body = await response.json();
        console.log(body);
        alert("Request submitted");
        
    } else {
        let body = await response.json;
        console.log(body)
    }
}
// CODE BELOW IS FOR PAST REQUESTS
const table = document.getElementById("reimbursementsPastTable");
const tableBody = document.getElementById("reimbursementsPastBody")

async function getAllPastEmployeeData(){
    let newId = localStorage.getItem("id");
    let url = "http://127.0.0.1:5000/reimbursements/review/" + newId;
    console.log(newId);

    let response = await fetch(url);

    if (response.status == 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem getting the information")
    }
}

function populateData(responseBody){
    
    for (let emp of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${emp.transactionId}</td>
        <td>${emp.employeeId}</td>
        <td>${emp.reimbursementAmount}</td>
        <td>${emp.expenseReason}</td>
        <td>${emp.status}</td>
        <td>${emp.managerComment}</td>
        <td>${emp.date}</td>`
        tableBody.appendChild(tableRow);
    }
}

getAllPastEmployeeData();