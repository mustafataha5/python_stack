

$(document).ready(function(){
    const month_name = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    function getTime(){
        now_d = new Date();
        year = now_d.getFullYear();
        month = month_name[now_d.getMonth()];
        day = now_d.getDate();
        hour = now_d.getHours();
        min = now_d.getMinutes();
        sec= now_d.getSeconds();  
        $("#date").text(month+"  "+day+" , "+year) ;
        $("#time1").text(hour+":"+min+":"+sec)
        //time_h.innerText = month+"  "+day+" , "year ; 
    }
    
    setInterval(getTime,1000);
  });
















