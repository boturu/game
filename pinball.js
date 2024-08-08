var fixedRect1,fixedRect2,fixedRect3,fixedRect4,movingRect;
var car,wall1,wall2,wall3,wall4;

function preload(){
    music = loadSound("music.mp3");
}


function setup(){
    createCanvas(800,600);
  fixedRect1 = createSprite(600, 400, 50, 80);
  fixedRect1.shapeColor = "green";
  fixedRect1.debug = true;
  
  fixedRect2 = createSprite(800, 400, 50, 80);
  fixedRect2.shapeColor = "red";
  fixedRect2.debug = true;

  fixedRect3 = createSprite(400, 400, 50, 80);
  fixedRect3.shapeColor = "blue";
  fixedRect3.debug = true;

  fixedRect4 = createSprite(200, 400, 50, 80);
  fixedRect4.shapeColor = "yellow";
  fixedRect4.debug = true;

  movingRect = createSprite(400,200,80,30);
  movingRect.shapeColor = "white";
  movingRect.debug = true;

  car =createSprite(200,200,30,30);
  car.shapeColor="red";

  wall1=createSprite(1000,200,30,100);
  wall1.shapeColor="red";

  wall2=createSprite(1000,200,30,100);
  wall2.shapeColor="red";

  wall3=createSprite(1000,200,30,100);
  wall3.shapeColor="red";

  wall4=createSprite(1000,200,30,100);
  wall4.shapeColor="red";

  car.velocityX=5;

}

function draw() {
    background(0,0,0);  
    movingRect.x = World.mouseX;
    movingRect.y = World.mouseY;
  
    if(isTouching(car,movingRect)){
      text("you win",400,600);
    }
    bounceOff(car,wall1);
    bounceOff(car,wall2);
    bounceOff(car,wall3);
    bounceOff(car,wall4); 
    drawSprites();
}
