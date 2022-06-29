"use strict";
function crazyMode(svg, paddle, level, checkScore, firstBall) {
    document.getElementById("playerLeft").textContent = String(0),
        document.getElementById("playerRight").textContent = String(0);
    const svgRect = svg.getBoundingClientRect();
    let ball = new Elem(svg, "circle")
        .attr('cx', Math.random() * svgRect.width)
        .attr('cy', Math.random() * svgRect.height)
        .attr('r', 10)
        .attr('fill', '#ffd700'), otherAiPaddle = makeElement(svg, 20, 260, 10, 80, '#fff'), start = animateBall(svg, ball, otherAiPaddle, paddle, level, checkScore, firstBall).subscribe(() => { });
    AIMove(svg, ball, otherAiPaddle).subscribe(() => { });
    Observable.fromEvent(document, "keypress")
        .filter(e => e.key == "q" || e.key == "Q" || e.key == "81")
        .subscribe(() => {
        start();
        document.getElementById("backdrop").style.display = "block",
            document.getElementById("popup").style.display = "block";
    });
}
function AIMove(svg, ball, paddle) {
    let vy = 1;
    return Observable.interval(5)
        .filter(() => Number(ball.attr('cy')) > Number(paddle.attr('y')) + Number(paddle.attr('height')) / 2 ||
        Number(ball.attr('cy')) < Number(paddle.attr('y')) + Number(paddle.attr('height')) / 2)
        .filter(() => Number(ball.attr('cy')) > Number(paddle.attr('y')) + Number(paddle.attr('height')) / 2 ?
        Number(paddle.attr('y')) + Number(paddle.attr('height')) + vy < 600 : Number(paddle.attr('y')) - vy > 0)
        .map(() => Number(ball.attr('cy')) > Number(paddle.attr('y')) + Number(paddle.attr('height')) / 2 ?
        paddle.attr('y', Number(paddle.attr('y')) + vy) : paddle.attr('y', Number(paddle.attr('y')) - vy));
}
function mouseMove(svg, paddle) {
    const svgRect = svg.getBoundingClientRect();
    return Observable.fromEvent(svg, "mousemove")
        .filter(({ clientY }) => Number(clientY) - svgRect.top > 0 &&
        Number(clientY) + Number(paddle.attr('height')) - svgRect.top < 600)
        .map(({ clientY }) => paddle.attr('y', Number(clientY) - svgRect.top));
}
function scoreboardUpdate(dx, ball, checkScore, firstBall) {
    let playerRightScore = document.getElementById("playerRight").textContent, playerLeftScore = document.getElementById("playerLeft").textContent, userStats = document.getElementById("user-stats").innerHTML, aiStats = document.getElementById("ai-stats").innerHTML;
    dx > 0 ? document.getElementById("playerLeft").textContent = String(Number(playerLeftScore) + 1) :
        document.getElementById("playerRight").textContent = String(Number(playerRightScore) + 1);
    if (Number(document.getElementById("playerRight").textContent) === checkScore ||
        Number(document.getElementById("playerLeft").textContent) === 11) {
        let stopBall = Observable.interval(1).map(() => ball.attr('cx', 300).attr('cy', 300)).subscribe(() => { }), stopFirstBall = Observable.interval(1).map(() => firstBall.attr('cx', 300).attr('cy', 300)).subscribe(() => { });
        Number(document.getElementById("playerRight").textContent) === checkScore ?
            (document.getElementById("player").innerHTML = "User",
                document.getElementById("user-stats").innerHTML = String(Number(userStats) + 1)) :
            (document.getElementById("player").innerHTML = "AI",
                document.getElementById("ai-stats").innerHTML = String(Number(aiStats) + 1)),
            document.getElementById("restart-backdrop").style.display = "block",
            document.getElementById("game-over").style.display = "block";
        setTimeout(function () {
            document.getElementById("restart-backdrop").style.display = "none",
                document.getElementById("game-over").style.display = "none",
                document.getElementById("playerLeft").textContent = String(0),
                document.getElementById("playerRight").textContent = String(0),
                stopBall(), stopFirstBall();
        }, 3000);
    }
}
function randomise() {
    return (Math.round(Math.random()) * 2) - 1;
}
function animateBall(svg, ball, paddleOne, paddleTwo, level, checkScore, firstBall) {
    const svgRect = svg.getBoundingClientRect();
    let dy = randomise() * level, dx = 1;
    return Observable.interval(3).map(() => ball.attr('cx', dx + (Number(ball.attr('cx')))).attr('cy', dy + Number(ball.attr('cy'))))
        .map(() => Number(ball.attr('cy')) + 2 * Number(ball.attr('r')) >= 600 ||
        Number(ball.attr('cy')) - 2 * Number(ball.attr('r')) <= 0 ?
        dy = -dy : Number(ball.attr('cx')) >= 600 ?
        ball.attr('cx', Number(ball.attr('cx')) - svgRect.width) && scoreboardUpdate(dx, ball, checkScore, firstBall) : Number(ball.attr('cx')) <= 0 ?
        ball.attr('cx', Number(ball.attr('cx')) + svgRect.width) && scoreboardUpdate(dx, ball, checkScore, firstBall) : (dy = dy, dx = dx))
        .map(() => {
        if ((dx > 0 &&
            Number(ball.attr('cx')) + Number(ball.attr('r')) >= Number(paddleTwo.attr('x')) &&
            Number(ball.attr('cy')) + Number(ball.attr('r')) > Number(paddleTwo.attr('y')) &&
            Number(ball.attr('cy')) - Number(ball.attr('r')) < Number(paddleTwo.attr('y')) + Number(paddleTwo.attr('height'))) ||
            (dx < 0 &&
                Number(ball.attr('cx')) - Number(ball.attr('r')) <= Number(paddleOne.attr('x')) + Number(paddleOne.attr('width')) &&
                Number(ball.attr('cy')) + Number(ball.attr('r')) > Number(paddleOne.attr('y')) &&
                Number(ball.attr('cy')) - Number(ball.attr('r')) < Number(paddleOne.attr('y')) + Number(paddleOne.attr('height')))) {
            dx = -dx;
        }
    });
}
function makeElement(svg, x, y, width, height, fill, tag = 'rect') {
    return new Elem(svg, tag)
        .attr('x', x)
        .attr('y', y)
        .attr('width', width)
        .attr('height', height)
        .attr('fill', fill);
}
function pong() {
    const classic = document.getElementById("classic-mode"), crazy = document.getElementById("crazy-mode"), svg = document.getElementById("canvas"), svgRect = svg.getBoundingClientRect(), topBorder = makeElement(svg, 0, 0, svgRect.width, 10, '#fff'), rightBorder = makeElement(svg, 590, 0, 10, svgRect.height, '#fff'), bottomBorder = makeElement(svg, 0, 590, svgRect.width, 10, '#fff'), leftBorder = makeElement(svg, 0, 0, 10, svgRect.height, '#fff'), aiPaddle = makeElement(svg, 20, 260, 10, 80, '#fff'), userPaddle = makeElement(svg, 570, 260, 10, 80, '#fff');
    let ball = new Elem(svg, 'circle')
        .attr('cx', Math.random() * svgRect.width)
        .attr('cy', Math.random() * svgRect.height)
        .attr('r', 10)
        .attr('fill', '#fff'), level = 1, checkScore = 11, start = animateBall(svg, ball, aiPaddle, userPaddle, level, checkScore).subscribe(() => { });
    mouseMove(svg, userPaddle).subscribe(() => { });
    AIMove(svg, ball, aiPaddle).subscribe(() => { });
    Observable.fromEvent(classic, "click")
        .subscribe(() => location.reload());
    Observable.fromEvent(crazy, "click")
        .subscribe(() => crazyMode(svg, userPaddle, level = level + 1, checkScore = checkScore + 10, ball));
    Observable.fromEvent(document, "keypress")
        .filter(e => e.key == "q" || e.key == "Q" || e.key == "81")
        .subscribe(() => {
        start();
        document.getElementById("backdrop").style.display = "block",
            document.getElementById("popup").style.display = "block";
    });
}
if (typeof window != 'undefined')
    window.onload = () => {
        pong();
    };
//# sourceMappingURL=pong.js.map