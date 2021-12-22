//  Manager Page
// ---------------------Logout Button-------------------------
function logout(){
    sessionStorage.clear();
    window.location.href = "trial.html"
}

// ----------------------Constants------------------------------
let tableCounter = 0;
const table = document.getElementById("reimbursementsTable");
const tableBody = document.getElementById("reimbursementsBody");
const tablePast = document.getElementById("reimbursementsPastTable");
const tableBodyPast = document.getElementById("reimbursementsPastBody");
const transactionIdHolder = document.getElementById("transId");
const statsOneEmployeeId = document.getElementById("employeeIdForStatOne");

// -------Fetches data and auto-populates with employee pending data -------

async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/reimbursements/pending" 

    let response = await fetch(url);

    if (response.status == 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem getting the information of retreiving info")
    }
}

// ---------Populates the data for getAllEmployeeData--------------------
function populateData(responseBody){
    
    for (let emp of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td id="transId">${emp.transactionId}</td>
        <td>${emp.employeeId}</td>
        <td>$${emp.reimbursementAmount}</td>
        <td>${emp.expenseReason}</td>
        <td>${emp.status}</td>
        <td>${emp.managerComment}</td>
        <td>${emp.date}</td>`
        // <input type="text" id="commentBox" placeholder="Place A Comment"></input>
        // <button onclick=submitComment()>Submit</button>`
        tableBody.appendChild(tableRow);
        tableCounter++;
    }
}
// --------------------Leave Comment------------------------------------
async function leaveComment(){

    let transIdInput = document.getElementById("transIdBox");
    let commentInput = document.getElementById("commentBox");
    
    let commentResponse  = await fetch("http://127.0.0.1:5000/reimbursements/comment/"+transIdInput.value, {
        
        method:"PATCH", 
        mode : "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            managerComment: commentInput.value
        })
    }
)
if (commentResponse.status === 200){
    let body = await commentResponse.json()
    console.log(transIdInput.value);
    console.log(commentInput.value);
    updateAllEmployees()
    
} else {
    alert("No")
    }
}
//  Function for deleting Field
function updateAllEmployees(){
    
    for (let i = tableCounter; i > 0; i--){
        document.getElementById("reimbursementsTable").deleteRow(i);
    }
    getAllEmployeeData();
}
// --------------------Approve / Deny Request Function--------------------
async function approvalFunction(){

    let transactIdInput = document.getElementById("transactIdBox");
    let approvalInput = document.getElementById("approvalBox");
    
    let commentResponse  = await fetch("http://127.0.0.1:5000/reimbursements/approval/"+transactIdInput.value, {
        
        method:"PATCH", 
        mode : "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            status: approvalInput.value
        })
    }
)
if (commentResponse.status === 200){
    let body = await commentResponse.json()
    console.log(transactIdInput.value);
    console.log(approvalInput.value);
    updateAllEmployees()
} else {
    alert("No")
    }
}
//  Function for deleting Field
function updateAllEmployees(){
    
    for (let i = tableCounter; i > 0; i--){
        document.getElementById("reimbursementsTable").deleteRow(i);
    }
    getAllEmployeeData();
}
// ----------------------Past Request Data-----------------------------
async function getAllPastEmployeeData(){
    let urlPast = "http://127.0.0.1:5000/reimbursements/past" 

    let response = await fetch(urlPast);

    if (response.status == 200){
        let body = await response.json();
        populatePastData(body);
    } else {
        alert("There was a problem getting the information of retreiving info")
    }
}

// ---------------------Populates the data for Past--------------------
function populatePastData(responseBody){
    
    for (let emp of responseBody){
        let tableRowPast = document.createElement("tr");
        tableRowPast.innerHTML = `<td>${emp.transactionId}</td>
        <td>${emp.employeeId}</td>
        <td>$${emp.reimbursementAmount}</td>
        <td>${emp.expenseReason}</td>
        <td>${emp.status}</td>
        <td>${emp.managerComment}</td>
        <td>${emp.date}</td>`
        tableBodyPast.appendChild(tableRowPast);
    }
}


// ------------------------Stat 1-------------------------------

const statsOneURL = "http://127.0.0.1:5000/reimbursements/stats/one/";
const statsTwoURL = "http://127.0.0.1:5000/reimbursements/stats/two/";
const statsThreeURL = "http://127.0.0.1:5000/reimbursements/stats/three/";
const statsFourURL = "http://127.0.0.1:5000/reimbursements/stats/four/";
const statsFiveURL = "http://127.0.0.1:5000/reimbursements/stats/five/";
let button = document.getElementById("getStatsButton");
let buttonTwo = document.getElementById("getStatsButtonTwo");
let buttonThree = document.getElementById("getStatsButtonThree");
let buttonFour = document.getElementById("getStatsButtonFour");
let buttonFive = document.getElementById("getStatsButtonFive");
button.onclick = showStats;
buttonTwo.onclick = showStatsTwo;
buttonThree.onclick = showStatsThree;
buttonFour.onclick = showStatsFour;
buttonFive.onclick = showStatsFive;
let data = document.getElementById("statsData");

async function showStats(){

    let userInput = document.getElementById("employeeIdForStatOne");
    data.innerHTML = "";

    let response = await fetch(statsOneURL + userInput.value);
    if (response.status === 200){
        let info = await response.json()
        populatingStats(info)
        console.log(info)
    } else {
        data.textContent = "No info found";
    }
}

//  Populating the data for Stat 1
function populatingStats(newData){
    let statisticsName = document.createElement("h3");
    statisticsName.textContent = newData;
    document.body.append("The average reimbursement request for this employee is:")
    document.body.appendChild(statisticsName);
}

// ------------------------Stat 2------------------------------
async function showStatsTwo(){

    let userInput = document.getElementById("employeeIdForStatTwo");
    data.innerHTML = "";

    let response = await fetch(statsTwoURL + userInput.value);
    if (response.status === 200){
        let info = await response.json()
        populatingStatsTwo(info)
        console.log(info)
    } else {
        data.textContent = "No info found for stat 2";
    }
}

//  Populating the data for Stat 2
function populatingStatsTwo(newData){
    let statisticsName = document.createElement("h3");
    statisticsName.textContent = newData;
    document.body.append("All reimbursement requests combined for this employee is:")
    document.body.appendChild(statisticsName);
}

// ----------------------------Stat 3----------------------
async function showStatsThree(){

    let userInput = document.getElementById("employeeIdForStatThree");
    data.innerHTML = "";

    let response = await fetch(statsThreeURL + userInput.value);
    if (response.status === 200){
        let info = await response.json()
        populatingStatsThree(info)
        console.log(info)
    } else {
        data.textContent = "No info found";
    }
}

//  Populating the data for Stat 3
function populatingStatsThree(newData){
    let statisticsName = document.createElement("h3");
    statisticsName.textContent = newData;
    document.body.append("The number of requests for this employee is:")
    document.body.appendChild(statisticsName);
}
// ---------------------------Stat 4---------------------------------
async function showStatsFour(){

    let userInput = document.getElementById("employeeIdForStatFour");
    data.innerHTML = "";

    let response = await fetch(statsFourURL + userInput.value);
    if (response.status === 200){
        let info = await response.json()
        populatingStatsFour(info)
        console.log(info)
    } else {
        data.textContent = "No info found";
    }
}

//  Populating the data for Stat 4
function populatingStatsFour(newData){
    let statisticsName = document.createElement("h3");
    statisticsName.textContent = newData;
    document.body.append("The highest request for this employee is:")
    document.body.appendChild(statisticsName);
}
// ---------------------------Stat 5---------------------------------
async function showStatsFive(){

    let userInput = document.getElementById("employeeIdForStatFive");
    data.innerHTML = "";

    let response = await fetch(statsFiveURL + userInput.value);
    if (response.status === 200){
        let info = await response.json()
        populatingStatsFive(info)
        console.log(info)
    } else {
        data.textContent = "No info found";
    }
}

//  Populating the data for Stat 5
function populatingStatsFive(newData){
    let statisticsName = document.createElement("h3");
    statisticsName.textContent = newData;
    document.body.append("The lowest request for this employee is:")
    document.body.appendChild(statisticsName);
}



getAllEmployeeData();
getAllPastEmployeeData();