### 为什么会有这个项目:
在使用parsec远程桌面的时候，我的鼠标图标消失了，并且很长时间没有解决。<br>
后来我调了windows的设置使得我按ctrl的时候我的鼠标位置会被高亮。<br>
我在使用远程电脑时不停的按着ctrl，直到我都感到厌烦并且不愿意再打开远程桌面。<br>
但是今天突然想到了用一个图片跟随鼠标位置的方法。 <br>
### 原理:
实际上是新建一个透明无边框窗口里面贴图跟随鼠标。fps=60，用pyautogui获取鼠标位置。<br>
### 注意:
因为远程桌面的原因，我的鼠标位置和实际位置有错位，我加上了x=450,y=450的偏移量。请根据实际情况调整。<br>
注意不要将鼠标活动区正好落在窗口上，否则会被窗口捕获，变得无法和其他窗口交互。<br>

======<br>
你可以换上任何你喜欢的图片.
