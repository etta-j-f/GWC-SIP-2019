// console.log("hello world");

// var h1tag = document.getElementById("h1")[0];
//
// var loc = document.getElementById("adjectives")[3];

var adjectives = ['Italian','a conspiracy theorist', 'the government', 'happy', 'amazing', 'sweet', 'wonderful', 'a BTS Stan'];
var fonts = ["Fascinate"]
var pos=0;


var loc =  document.getElementById("adjectives")

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if(pos>= adjectives.length){
  pos = 0;
  }
}

var foz = document.getElementById("the name")
function changeFontColor(){
  foz.setAttribute("style", "color:blue")
}
var fonts = ["'Darker Grotesque', sans-serif;" , "'Hanalei', cursive;",
 "'Geostar', cursive;" ,"'Roboto Mono', monospace"];

var poz = 0;

function fontChange(){
  foz.setAttribute("style" , `font-family: ${fonts[poz]}`)
  poz++;
  if(poz>=fonts.length){
    poz=0;
  }
}

Math.random()
var x = document.getElementsByTagName("body")[0]

function colorfulBackground(){
  x.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)},
  ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`)

}
