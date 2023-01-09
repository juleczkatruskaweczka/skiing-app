var eventBox = document.getElementById('event-box')
var table = document.getElementById("table");
var koniec;
setInterval(()=>{
    for( var i = 1; i < table.rows.length; i++){
        eventDate = table.rows[i].cells[2].textContent
        minuty = table.rows[i].cells[3].textContent
        minuty = minuty.replace(" minut","")
        eventDate = Date.parse(eventDate.replace(" ","T"))
        console.log()
        const now = new Date().getTime();
        const diff = eventDate - now;
        const d = Math.floor((eventDate/(1000 * 60 * 60 * 24) - (now/(1000 * 60 * 60 * 24))) % 60)
        const h = Math.floor((eventDate/(1000 * 60 * 60) - (now/(1000 * 60 * 60 ))) % 60 )
        const m = Math.floor((eventDate/(1000 * 60 ) - (now/(1000 * 60 ))) % 60 )
        const s = Math.floor((eventDate/(1000) - (now/(1000))) % 60 )
        if (diff > 0){
            table.rows[i].cells[4].innerHTML =  d +  " dni,"  + h + " godzin, " + m + "minut"
        }else{
            if (now < eventDate+(parseInt(minuty)*60*1000)){
                table.rows[i].cells[4].innerHTML =  "Trwa"
            }else{
                table.rows[i].cells[4].innerHTML =  "Wydarzenie już się odbyło"
            }
        }
    }
},1000)
