# 오픈소스소프트웨어 4주차 과제

## turtle_runaway.py 및 turtle_runaway.md 작성

- - -
### 타이머 구현
```cpp
def display_timer(self):
        self.drawer_timer.undo()
        self.drawer_timer.penup()
        self.drawer_timer.setpos(0, 300)
        self.timer = self.timer_limit - (time.time() - self.timer_start)
        if self.timer > 0:
            self.drawer_timer.write(f'{self.timer:.3f} sec', align="center", font=("Consolas", 32, "bold"))
        else:
            self.drawer_timer.write('Time out!', align="center", font=("Consolas", 32, "bold"))
```
* **설명**  
def start(self, ...): 에서 시작 시간(self.timer_start = time.time())과 제한 시간(self.timer_limit = timer_limit)을 정한 후 이를 통해 남는 시간(self.timer = self.timer_limit - (time.time() - self.timer_start))을 구한다. 만약 남는 시간이 0보다 크다면 화면에 남는 시간을 출력하고, 반대로 0 이하라면 "Timeout"을 출력한다. 
<!--
![image](https://user-images.githubusercontent.com/113341200/193529380-c99e8eab-c22e-4799-bb76-9fa965f38f11.png)
![image](https://user-images.githubusercontent.com/113341200/193531986-ab8fee60-9b81-48f0-9b0a-15383404e447.png)
-->
<img src="https://user-images.githubusercontent.com/113341200/193529380-c99e8eab-c22e-4799-bb76-9fa965f38f11.png" width="450" height="300"/>
<img src="https://user-images.githubusercontent.com/113341200/193531986-ab8fee60-9b81-48f0-9b0a-15383404e447.png" width="450" height="300"/>


- - -
### 점수 구현
```cpp
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
```
* **설명**  
self.is_catched()가 True를 반환할 때마다 self.count가 1씩 증가하며 self.count_goal에 도달하면 점수(self.score)를 1추가하고 다시 self.count를 0으로 초기화를 반복한다. 즉 self.count_goal x self.ai_timer_msec (5 x 100ms = 500ms) 동안 연속해서 chaser가 runner를 잡은 상태일 때마다 점수가 1씩 추가된다. 또한 남은 시간(self.timer)이 0 초과일 때만 작동하므로 남는 시간이 0 이하면 점수는 고정된다.
<!--
![image](https://user-images.githubusercontent.com/113341200/193535181-4fbb8eb9-f365-4d59-a15f-38d49fd35d71.png)
![image](https://user-images.githubusercontent.com/113341200/193535281-a144c0e6-9f3a-4224-9a53-41e92a455336.png)
-->
<img src="https://user-images.githubusercontent.com/113341200/193535181-4fbb8eb9-f365-4d59-a15f-38d49fd35d71.png" width="450" height="300"/>
<img src="https://user-images.githubusercontent.com/113341200/193535281-a144c0e6-9f3a-4224-9a53-41e92a455336.png" width="450" height="300"/>


- - -
### 발전된 runner AI 구현
```cpp
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
```
* 설명  
기존에 받던 상대측의 위치와 방향 대신 자신(runner)과 상대(chaser)의 객체를 받는다. runner.distance(chaser_pos)를 통해 상대와 자신과의 거리가 250 이상이면 기존과 같은 방식의 완전 랜덤으로 움직이는 대신 상대가 어느정도 가까워지면(거리 250이하) self.setheading(-random.randint(int(runner.towards(chaser_pos)) - 20, int(runner.towards(chaser_pos)) + 20))를 통해 상대가 있는 반대 방향의 -20도에서 +20도 범위 내를 바라보고 self.step_move만큼 이동한다. 즉, 기존 방식보다 더 효과적으로 도망칠 수 있다.
<!--
![image](https://user-images.githubusercontent.com/113341200/193535937-63e86cbd-36f3-484f-bbd1-692495e6832c.png)
![image](https://user-images.githubusercontent.com/113341200/193535981-9239ef3a-cc96-4dfe-8aef-4d4c8a73969c.png)
-->
거리가 250보다 멀어 오히려 chaser 쪽으로 오는 runner  
<img src="https://user-images.githubusercontent.com/113341200/193535937-63e86cbd-36f3-484f-bbd1-692495e6832c.png" width="450" height="300"/>  
거리가 250보다 가까워 chaser 로부터 도망가는 runner  
<img src="https://user-images.githubusercontent.com/113341200/193535981-9239ef3a-cc96-4dfe-8aef-4d4c8a73969c.png" width="450" height="300"/>
