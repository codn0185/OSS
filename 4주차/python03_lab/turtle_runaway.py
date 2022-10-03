# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.

# TODO: Add a timer (5 points): You can freely choose an up/down timer for your purpose.
# TODO: Add your -intelligent- Turtle (8 points): You can assign a role, runner or chaser or both
# TODO: Add your concept of score (7 points): You can define the score by yourself
import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        canvas.title("Turtle Runaway Game")
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('turquoise')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer_is_catched = turtle.RawTurtle(canvas)
        self.drawer_is_catched.hideturtle()
        self.drawer_is_catched.penup()

        self.drawer_timer = turtle.RawTurtle(canvas)
        self.drawer_timer.hideturtle()
        self.drawer_timer.penup()

        self.drawer_score = turtle.RawTurtle(canvas)
        self.drawer_score.hideturtle()
        self.drawer_score.penup()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100, timer_limit=30):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

        self.timer_limit = timer_limit
        self.timer_start = time.time()

        self.score = 0
        self.count = 0
        self.count_goal = 5


    def step(self):
        self.runner.run_ai(self.runner, self.chaser)
        self.chaser.run_ai(self.runner, self.chaser)

        self.display_is_catched()
        self.display_timer()
        self.display_score()

        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def display_is_catched(self):
        is_catched = self.is_catched()
        self.drawer_is_catched.undo()
        self.drawer_is_catched.penup()
        self.drawer_is_catched.setpos(-300, 300)
        self.drawer_is_catched.write(f'Is catched? {is_catched}')

    def display_timer(self):
        self.drawer_timer.undo()
        self.drawer_timer.penup()
        self.drawer_timer.setpos(0, 300)
        self.timer = self.timer_limit - (time.time() - self.timer_start)
        if self.timer > 0:
            self.drawer_timer.write(f'{self.timer:.3f} sec', align="center", font=("Consolas", 32, "bold"))
        else:
            self.drawer_timer.write('Time out!', align="center", font=("Consolas", 32, "bold"))

    def display_score(self):
        if self.timer > 0:
            if self.is_catched():
                self.count += 1
                if self.count >= self.count_goal:
                    self.score += 1
                    self.count = 0
            else:
                self.count = 0
        score = self.score
        self.drawer_score.undo()
        self.drawer_score.penup()
        self.drawer_score.setpos(300, 300)
        self.drawer_score.write(f'Score: {score}', align="center", font=("Consolas", 22, "bold"))


class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def chase_ai(self, runner, chaser): # TODO: A키로 자동 모드 온/오프
        pass

    def run_ai(self, runner, chaser):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def chase_ai(self, runner, chaser):
        pass

    def run_ai(self, runner, chaser): # TODO: 더 똑똑한 인공지능 만들기
        runner_pos = runner.pos()
        runner_heading = runner.heading()
        chaser_pos = chaser.pos()
        chaser_heading = chaser.heading()

        if runner.distance(chaser_pos) > 250.0:
            mode = random.randint(0, 2)
            if mode == 0:
                self.forward(self.step_move)
            elif mode == 1:
                self.left(self.step_turn)
            elif mode == 2:
                self.right(self.step_turn)
        else:
            self.setheading(-random.randint(int(runner.towards(chaser_pos)) - 20, int(runner.towards(chaser_pos)) + 20)) # chaser의 반대 각도의 -20도 ~ +20도의 범위로 회전
            self.forward(self.step_move)


if __name__ == '__main__':
    canvas = turtle.Screen()
    canvas.setup(width=1200, height=800)
    # AI를 쫓아가기
    runner = RandomMover(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, chaser)
    game.start()
    canvas.mainloop()
