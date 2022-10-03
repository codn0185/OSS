# 오픈소스소프트웨어 4주차 과제

## turtle_runaway.py 및 turtle_runaway.md 작성

### 타이머
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
* 설명  
def start(self, ...): 에서 시작 시간과 제한 시간을 정해서 현재 시간에서 시작 시간을 뺸 것을 제한 시간에서 빼서 남는 시간을 구하고, 제한 시간이 

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
