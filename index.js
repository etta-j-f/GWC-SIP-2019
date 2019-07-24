console.log("Hello, World");

var i = 0;
// for loop- sets i to 0 then add 2 to i when i <=20
for(i = 0; i <= 20; i +=2){
  console.log(i);

}

i = 0;
while(i <=20){
  console.log(i);
  i +=2;
}

function getTemp(){
  return 22.5;

}

var temperature = getTemp();
console.log(temperature);

function getTemp2(type){
  if (type == "c"){
    alert("it is a rainy day");
    return 22.5;
  }
  if (type == "f"){
    alert("It is really hot today");
    return 100;
  }
}
console.log(getTemp2("f"))
console.log(getTemp2("c"))

document.getElementById("adjectives").addEventListener("mouseover" ,
function (){
document.getElementById("adjectives").style.color = "red"
}
