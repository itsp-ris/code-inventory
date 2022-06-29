// FIT2102 2018 Assignment 1
// https://docs.google.com/document/d/1woMAgJVf1oL3M49Q8N3E1ykTuTu5_r28_MQPVS5QIVo/edit?usp=sharing

/** function for a different version of pong, returns nothing
* @param svg is the parent SVG object that will host the new element
* @param paddle is the child SVG object hosted by the svg
* @param level is 1 by default but incremented by 1 when this function is 
* called to increase the velocity of the ball
* @param checkScore is 11 by default but incremented by 10 when this function 
* is called; the game is over when either player reached the checkScore
* @param firstBall is an optional argument which is only passed if existed;
* passed into the function for easy unsubscription when the user is playing
* this version 
*/ 
function crazyMode(svg: HTMLElement, paddle: Elem, level: number, checkScore: number, firstBall?: Elem): void {
  // restart the scoreboard to not append the stats from the original pong play
  document.getElementById("playerLeft")!.textContent = String(0),
  document.getElementById("playerRight")!.textContent = String(0);
  const svgRect = svg.getBoundingClientRect();
    let 
      ball = new Elem(svg, "circle")
        .attr('cx', Math.random()*svgRect.width)
        .attr('cy', Math.random()*svgRect.height)
        .attr('r', 10)
        .attr('fill', '#ffd700'),
      otherAiPaddle = makeElement(svg, 20, 260, 10, 80, '#fff'),
      // animate the newly created ball by calling animateBall function
      // subscribed to the ball movement, the change of direction after 
      // bouncing off boundaries(, etc.) 
      start = animateBall(svg, ball, otherAiPaddle, paddle, level, checkScore, firstBall).subscribe(() => {});

    // animate the newly created AI paddle by calling AIMove function
    // subscribed to the paddle movement which corresponds to the newly
    // created ball
    AIMove(svg, ball, otherAiPaddle).subscribe(() => {});
    
    // unsubscribe from animateBall when subscribed keyboard key 'Q' is pressed 
    // detect key 'Q' by passing all press keyboard key values through
    // a filter function
    Observable.fromEvent<KeyboardEvent>(document, "keypress")
      .filter(e => e.key == "q" || e.key == "Q" || e.key == "81")
      .subscribe(() => {
        start(); document.getElementById("backdrop")!.style.display = "block", 
        document.getElementById("popup")!.style.display = "block"})
}
//

/** function to move the AI paddle; returns an observable
 * @param svg is the parent SVG object that will host the new element
 * @param ball is the child SVG object hosted by the svg
 * @param paddle is the child SVG object hosted by the svg
 */
function AIMove(svg: HTMLElement, ball: Elem, paddle: Elem): Observable<any> {
  let vy = 1

  // map the paddle, a child SVG object, to its new coordinates 
  // after move which corresponds to the ball, also a child SVG object.
  // only coordinates within the svg canvas is taken into the mapping function 
  // by passing all values through filtering function 
  return Observable.interval(5)
    .filter(() => Number(ball.attr('cy')) > Number(paddle.attr('y'))+Number(paddle.attr('height'))/2 || 
      Number(ball.attr('cy')) < Number(paddle.attr('y'))+Number(paddle.attr('height'))/2)
    .filter(() => Number(ball.attr('cy')) > Number(paddle.attr('y'))+Number(paddle.attr('height'))/2 ? 
      Number(paddle.attr('y'))+Number(paddle.attr('height'))+vy < 600:Number(paddle.attr('y'))-vy > 0)
    .map(() => Number(ball.attr('cy')) > Number(paddle.attr('y'))+Number(paddle.attr('height'))/2 ?
      paddle.attr('y', Number(paddle.attr('y'))+vy):paddle.attr('y', Number(paddle.attr('y'))-vy))
}
//

/** function to move the User paddle, returns an observable
 * @param svg is the parent SVG object that will host the new element
 * @param paddle is the child SVG object hosted by the svg
 */
function mouseMove(svg: HTMLElement, paddle: Elem): Observable<any> {
  const svgRect = svg.getBoundingClientRect()
  
  // triggered by mouse movement to map the paddle, a child SVG
  // object, to its new coordinates which corresponds to the direction 
  // of the mouse along the y axis.
  // only coordinates within the svg canvas is taken into the mapping function
  // by passing all values through a filter function
  return Observable.fromEvent<MouseEvent>(svg, "mousemove")
    .filter(({clientY}) => Number(clientY)-svgRect.top > 0 && 
      Number(clientY)+Number(paddle.attr('height'))-svgRect.top < 600)
    .map(({clientY}) => paddle.attr('y', Number(clientY)-svgRect.top))
}
//

/** function to modify the scoreboard and players' statistics, returns void
 * @param dx is a number which indicates the direction of the ball
 * @param ball is the child SVG object hosted by the svg
 * @param checkScore is 11 by default; the game is over when either 
 * player reached the checkScore
 * @param firstBall is an optional argument which is only passed if existed
 */
function scoreboardUpdate(dx: number, ball: Elem, checkScore: number, firstBall?: Elem): void {
  let 
    playerRightScore =  document.getElementById("playerRight")!.textContent,
    playerLeftScore =  document.getElementById("playerLeft")!.textContent,
    userStats = document.getElementById("user-stats")!.innerHTML,
    aiStats = document.getElementById("ai-stats")!.innerHTML;

  dx > 0 ? document.getElementById("playerLeft")!.textContent = String(Number(playerLeftScore)+1):
  document.getElementById("playerRight")!.textContent = String(Number(playerRightScore)+1);

  if (Number(document.getElementById("playerRight")!.textContent) === checkScore || 
    Number(document.getElementById("playerLeft")!.textContent) === checkScore) {
    // map the position of the ball to the center of the canvas when the game is over
    // subscribed to the ball movement and position
    let 
      stopBall = Observable.interval(1).map(() => 
        ball.attr('cx', 300).attr('cy', 300)).subscribe(() => {}),
      stopFirstBall = Observable.interval(1).map(() => 
        firstBall!.attr('cx', 300).attr('cy', 300)).subscribe(() => {})

    Number(document.getElementById("playerRight")!.textContent) === checkScore ? 
    (document.getElementById("player")!.innerHTML = "User", 
    document.getElementById("user-stats")!.innerHTML = String(Number(userStats)+1)) :
    (document.getElementById("player")!.innerHTML = "AI", 
    document.getElementById("ai-stats")!.innerHTML = String(Number(aiStats)+1)),

    document.getElementById("restart-backdrop")!.style.display = "block",
    document.getElementById("game-over")!.style.display = "block"
    
    setTimeout(function () {document.getElementById("restart-backdrop")!.style.display = "none", 
      document.getElementById("game-over")!.style.display = "none",
      document.getElementById("playerLeft")!.textContent = String(0), 
      document.getElementById("playerRight")!.textContent = String(0),
      // unsusbscribe from the mapping function mentioned earlier when the game restart
      stopBall(), stopFirstBall();}, 3000); 
  }
}
//

/** function to randomise between the two numbers 1 and -1, returns number
 * to randomise direction of the ball coming onto the canvas at the start
 * of the game
 */
function randomise(): number {
  return (Math.round(Math.random())*2)-1
}
//

/** function to animate the ball, returns an observable 
 * @param svg is the parent SVG object that will host the new element
 * @param paddleOne is the child SVG object hosted by the svg
 * @param paddleTwo is the child SVG object hosted by the svg
 * @param level is 1 by default
 * @param checkScore is 11 by default; the game is over when either 
 * player reached the checkScore
 * @param firstBall is an optional argument which is only passed if existed
 */
function animateBall(svg: HTMLElement, ball: Elem, paddleOne: Elem, paddleTwo: Elem, level: number, checkScore: number, firstBall?: Elem): Observable<any> {
  const svgRect = svg.getBoundingClientRect()
  let 
    dy = randomise()*level,
    dx = 1

  // animate the ball by mapping the previous position (direction and magnitude) 
  // of the ball to the velocity change.
  // check whether the ball is within the canvas and change its direction after 
  // off the boundaries.
  // boundaries used the border and the paddles' surfaces as indicator
  return Observable.interval(3).map(() => ball.attr('cx', dx+(Number(ball.attr('cx')))).attr('cy', dy+Number(ball.attr('cy'))))
    .map(() => 
      Number(ball.attr('cy'))+2*Number(ball.attr('r')) >= 600 || 
      Number(ball.attr('cy'))-2*Number(ball.attr('r')) <= 0 ? 
      dy = -dy:Number(ball.attr('cx')) >= 600 ? 
      ball.attr('cx', Number(ball.attr('cx'))-svgRect.width) && scoreboardUpdate(dx, ball, checkScore, firstBall):Number(ball.attr('cx')) <= 0 ? 
      ball.attr('cx', Number(ball.attr('cx'))+svgRect.width) && scoreboardUpdate(dx, ball, checkScore, firstBall):(dy = dy, dx = dx))
      // bounce off the right paddle
    .map(() => {if ((dx > 0 && 
      Number(ball.attr('cx'))+Number(ball.attr('r')) >= Number(paddleTwo.attr('x')) && 
      Number(ball.attr('cy'))+Number(ball.attr('r')) > Number(paddleTwo.attr('y')) && 
      Number(ball.attr('cy'))-Number(ball.attr('r')) < Number(paddleTwo.attr('y'))+Number(paddleTwo.attr('height'))) ||
      //
      // bounce off the left paddle 
      (dx < 0 && 
      Number(ball.attr('cx'))-Number(ball.attr('r')) <= Number(paddleOne.attr('x'))+Number(paddleOne.attr('width')) && 
      Number(ball.attr('cy'))+Number(ball.attr('r')) > Number(paddleOne.attr('y')) && 
      Number(ball.attr('cy'))-Number(ball.attr('r')) < Number(paddleOne.attr('y'))+Number(paddleOne.attr('height')))) {
      //
        dx = -dx
    }})
}
//

/** function to create new SVG element, returns the element
 * @param svg is the parent SVG object that will host the new element
 * @param x is the x-coordinate to place the new element
 * @param y is the y-coordinate to place the new element
 * @param width is the width size of the to-be-created element
 * @param height is the height size of the to-be-created element 
 * @param fill is a string representing the hex code of a colour to 
 * set the colour of the to-be-created element
 * @param tag could be "rect", "line", "ellipse", etc.
 */
function makeElement(svg: HTMLElement, x: number, y: number, 
  width: number, height: number, fill: string, tag: string = 'rect'): Elem {
    return new Elem(svg, tag)
      .attr('x', x)
      .attr('y', y)
      .attr('width', width)
      .attr('height', height)
      .attr('fill', fill)
}
//

function pong(): void {
  // Inside this function you will use the classes and functions 
  // defined in svgelement.ts and observable.ts
  // to add visuals to the svg element in pong.html, animate them, and make them interactive.
  // Study and complete the tasks in basicexamples.ts first to get ideas.

  // You will be marked on your functional programming style
  // as well as the functionality that you implement.
  // Document your code!  
  // Explain which ideas you have used ideas from the lectures to 
  // create reusable, generic functions.

  const
    // the code to create a new element is refactored into a function
    // for easy repeated actions
    classic = document.getElementById("classic-mode")!,
    crazy = document.getElementById("crazy-mode")!,
    svg = document.getElementById("canvas")!,
    svgRect = svg.getBoundingClientRect(),
    topBorder = makeElement(svg, 0, 0, svgRect.width, 10, '#fff'),
    rightBorder = makeElement(svg, 590, 0, 10, svgRect.height, '#fff'),
    bottomBorder = makeElement(svg, 0, 590, svgRect.width, 10, '#fff'),
    leftBorder = makeElement(svg, 0, 0, 10, svgRect.height, '#fff'),
    aiPaddle = makeElement(svg, 20, 260, 10, 80, '#fff'),
    userPaddle = makeElement(svg, 570, 260, 10, 80, '#fff');

  let ball = new Elem(svg, 'circle')
        .attr('cx', Math.random()*svgRect.width)
        .attr('cy', Math.random()*svgRect.height)
        .attr('r', 10)
        .attr('fill', '#fff'),
      level = 1,
      checkScore = 11,
      // subscribed to the observable returned from animateBall function
      // subscribed to ball movement, change of direction after bouncing
      // off the boundaries(, etc.)
      start = animateBall(svg, ball, aiPaddle, userPaddle, level, checkScore).subscribe(() => {});

  // subscribed to the observable returned from mouseMove function
  // subscribed to mouse movement, paddle movement(, etc.)
  mouseMove(svg, userPaddle).subscribe(() => {});
  // subscribed to the observable returned from AIMove function
  // subscribed to ball movement, paddle movement(, etc.)
  AIMove(svg, ball, aiPaddle).subscribe(() => {});

  // triggered by a click to the object passed as argument to the 
  // fromEvent method: classic
  // subscribed to clicking action and accepts the next function
  // which reload the page to call pong() again
  // for a guaranteed default version of pong()
  Observable.fromEvent(classic, "click")
  .subscribe(() => location.reload())

  // triggered by a click to the object passed as argument to the 
  // fromEvent method: crazy
  // subscribed to clicking action and accepts the next function
  // which responds by calling the crazyMode function
  Observable.fromEvent(crazy, "click")
    .subscribe(() => crazyMode(svg, userPaddle, level = level+1, checkScore = checkScore+10, ball))
  
  // unsubscribe from animateBall when subscribed keyboard key 'Q' is pressed 
  // detect key 'Q' by passing all press keyboard key values through
  // a filter function
  Observable.fromEvent<KeyboardEvent>(document, "keypress")
    .filter(e => e.key == "q" || e.key == "Q" || e.key == "81")
    .subscribe(() => {
      start(); document.getElementById("backdrop")!.style.display = "block",
      document.getElementById("popup")!.style.display = "block"})

}

// the following simply runs your pong function on window load.  Make sure to leave it in place.
if (typeof window != 'undefined')
  window.onload = ()=>{
    pong();
  }
 