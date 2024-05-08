

date_h= document.querySelector("#date");
time_h=document.querySelector("#time1");
const month_name = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
print("*********************")
//print(date)
print("*********************")
function getTime(){
    now_d = new Date();
    year = now_d.getFullYear();
    month = month_name[now_d.getMonth()];
    day = now_d.getDate();
    console.log(month+"  "+day+" , "+year)
    //time_h.innerText = month+"  "+day+" , "year ; 
}

print("*********************")
//print(date)
print("*********************")

getTime()











