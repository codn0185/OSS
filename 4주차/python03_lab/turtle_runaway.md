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
