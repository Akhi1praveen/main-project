function getHFValue(){
    var uiHF = document.getElementsByName('uiHF');
    for(var i = 0; i < uiHF.length; i++){
        if(uiHF[i].checked){
            return parseInt(uiHF[i].value);  // Get the actual value of the selected radio button
        }
    }
    return 0;  // Default to 0 if no selection is made
}

function onClickedprediction(){
    console.log("prediction button clicked");
    var Rainfall = document.getElementById("uirf");
    var Temperature = document.getElementById("uitemp");
    var Humidity = document.getElementById("uihum");
    var River_Discharge = document.getElementById("uird");
    var Water_Level = document.getElementById("uiwl");
    var Elevation = document.getElementById("uiele");
    var Historical_Floods   = getHFValue()
    var flood_pred = document.getElementById("uiest_pred");
    var flood_prob = document.getElementById("uiest_prob");
    var url = "http://127.0.0.1:5000/flood_predict";
    $.post(url, {
        Rainfall : parseFloat(Rainfall.value),
        Temperature : parseFloat(Temperature.value),
        Humidity : parseFloat(Humidity.value),
        River_Discharge : parseFloat(River_Discharge.value),
        Water_Level : parseFloat(Water_Level.value),
        Elevation : parseFloat(Elevation.value),
        Historical_Floods : Historical_Floods
    },function(data, status) {
        console.log(data.flood_predicted);
        let probabilityPercentage = (data.flood_probability * 100).toFixed(2);
        if(data.flood_predicted==1){
            flood_pred.innerHTML = "<h2>Flood predicted</h2>";
            flood_prob.innerHTML = `<h2>Flood Possibility: ${probabilityPercentage}%</h2>`;
        }
        else{
            flood_pred.innerHTML = "<h2>Flood not predicted</h2>";
            flood_prob.innerHTML = `<h2>Flood Possibility: ${probabilityPercentage}%</h2>`;
        }
       console.log(status);
    });
  }