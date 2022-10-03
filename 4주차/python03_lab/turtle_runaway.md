# 오픈소스소프트웨어 4주차 과제

## turtle_runaway.py 및 turtle_runaway.md 작성

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
* 설명  
def start(self, ...): 에서 시작 시간(self.timer_start = time.time())과 제한 시간(self.timer_limit = timer_limit)을 정한 후 이를 통해 남는 시간(self.timer = self.timer_limit - (time.time() - self.timer_start))을 구한다. 만약 남는 시간이 0보다 크다면 화면에 남는 시간을 출력하고, 반대로 0 이하라면 "Timeout"을 출력한다. 
<!--
![image](https://user-images.githubusercontent.com/113341200/193529380-c99e8eab-c22e-4799-bb76-9fa965f38f11.png)
![image](https://user-images.githubusercontent.com/113341200/193529446-421b1a17-10e2-48ff-a856-5957767cbdb7.png)
-->
<img src="https://user-images.githubusercontent.com/113341200/193529380-c99e8eab-c22e-4799-bb76-9fa965f38f11.png" width="450" height="300"/>
<img src="https://user-images.githubusercontent.com/113341200/193529446-421b1a17-10e2-48ff-a856-5957767cbdb7.png" width="450" height="300"/>

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
