
Sublime Text2 Mlog(Micro-LOG)
=
> ST2-Mlog是一款基于Sublime Text2全能文本编辑器的个人工作记录日志实践，它提供了丰富的语义化的日志格式，试图使您工作生活时间的统筹更加有效和便捷。

前记
=

在日常生活工作中，我们总是被乱七八糟的事情围绕。于是我们发现，自己的脑子完全不够用，于是避免不了要记录各种琐事。学生时代，我们把这些内容记录在笔记册中。职场社会中，我们或以小贴条的方式存在冰箱外壳，或是电脑显示器四周。天啊，还是乱七八糟的对不对。上周写的贴条，本周任务在哪，怎么找不到了，是不是周末被清洁的大姐清走了。更喜欢桌面简洁的朋友，可能更喜欢更绿色环保的方式，通过手机下载一个TODO类的APP，把内容记录在APP里。可是工作的时候，还老要翻手机看吗？当然，有很多APP支持上传到Cloud端。等等，我只是想要记下一些事情，不想事情太复杂，记下的内容让我比较容易看到，如果我一看就知道是什么事情，紧急不紧急那就太棒了。

以上，便是ST2-Mlog的初衷。

开发过程
=
您长得太丑，不能查看此内容。



后记
=
ST2-Mlog最初的几个`snippet`是`TODO`、`NEXT`、`WORK`、`DONE`、`Fixed`、`Refused`、`Delay`,前四个是个人工作事务相关的，例如TODO是标识该条事项应该着手去完成，NEXT则是接下来立马去做的。后三个则是BUG修复领域相关，如Fixed标识该条BUG已被修复，Refused表示BUG记录已被拒绝。`snippet`除了通过文本内容标识外，还通过突出的色彩高亮标识，使事项条目更易识别。

应用ST2-Mlog前，我参与的项目正处在开发未段，各种测试不断攻来，随之而来的是满天飞的BUG记录。上线时间点就在眼前，事情变得有压力起来，有的时候脑子真的很混乱。于是花了一个下午熟悉了Sublime Text2的开发指南，开始开发ST2-Mlog，于是才有以上的`snippet`。也正是以上这几个`snippet`在后面的这段富有压力的开发工作中，真的发挥了难以预见的作用，使得我在后面的软件开发生涯，莫名的产生了对ST2-Mlog的依赖。正是由于自己在这上面得到了很大的益处，才想要分享给大家，如果它同样使大家更高效的工作和生活，那便真的太棒了。

安装（Install）
=
中文
-
1. 下载本软件
2. 进入Sublime Text2的包安装目录
3. 将下载的压缩文件解压到包安装目录
4. 新建文件并以.mlog结尾
5. 改主题色调到`Mlog`
6. 完成


English
-
1. Download from Github
2. Go to `Browse Packages` folder of Sublime Text2
3. Unzip #1 download file to `Browse Packages` folder
4. Create a new file with stuff `.mlog`
5. Change color scheme to `Mlog`
6. Done


使用指引(Usage)
=
中文
-
### 个人事务领域 ###

| Snippet | 应用场景                   | 快速录入  | 快捷键 | 默认内容                        |
|---------|----------------------------|-----------|--------|---------------------------------|
| TODO    | 标识事项需要被完成         | td,TODO   |        | ** TODO,what do to ?            |
| NEXT    | 标识事项需要接下来立即完成 | nt,NEXT   |        | ** NEXT,what to do next ?       |
| WORK    | 标识事项正在被处理         | wk,WORK   |        | ** WORK,what to do in work?     |
| DONE    | 标识事项已完成             | done,DONE |        | ** DONE,what time ?,what done?. |



### 软件开发领域 ###

| Snippet | 应用场景                    | 快速录入   | 快捷键 | 默认内容                                   |
|---------|-----------------------------|------------|--------|--------------------------------------------|
| Delay   | 标识BUG被阻塞，应当延迟处理 | dl,Delay   |        | /* bug number */,Delay /* your commit */   |
| Fixed   | 标识BUG已被开发人员修复     | fx,Fixed   |        | /* bug number */,Fixed /* your commit */   |
| Refused | 标识BUG已被开发人员拒绝     | rf,Refused |        | /* bug number */,Refused /* your commit */ |

### 紧要级别 ###

| Snippet    | 应用场景                                 | 快速录入      | 快捷键 | 默认内容        |
|------------|------------------------------------------|---------------|--------|-----------------|
| #DEFAULT   | 标识事项为默认级别                       | df,Defalt     |        | #DEFAULT this   |
| #SUCCESS   | 标识事项为成功级别                       | sc,Success    |        | #SUCCESS this   |
| #WARNING   | 标识事项为注意级别                       | wn,Warning    |        | #WARNING this   |
| #IMPORTANT | 标识事项为重要级别                       | ipt,Important |        | #IMPORTANT this |
| #INFO      | 标识事项为通知级别                       | if,Info       |        | #INFO this      |
| #ERROR     | 标识事项为错误级别                       | er,Error      |        | #ERROR this     |
| #INVERSE   | 标识事项为反转级别(可以自定义为特定级别) | iv,Inverse    |        | #INVERSE this   |
| #1         | 标识事项为一级紧要级别                   | l1            |        | #1              |
| #2         | 标识事项为二级紧要级别                   | l2            |        | #2              |
| #3         | 标识事项为三级紧要级别                   | l3            |        | #3              |
| #4         | 标识事项为四级紧要级别                   | l4            |        | #4              |
| #5         | 标识事项为五级紧要级别                   | l5            |        | #5              |
| #6         | 标识事项为六级紧要级别                   | l1            |        | #6              |
| #7         | 标识事项为七级紧要级别                   | l2            |        | #7              |
| #8         | 标识事项为八级紧要级别                   | l3            |        | #8              |
| #9         | 标识事项为九级紧要级别                   | l4            |        | #9              |
| #10        | 标识事项为十级紧要级别                   | l10           |        | #10             |


### 快捷键 ###


| 快捷键       | 说明                                            |
|--------------|-------------------------------------------------|
| ctrl+shift+d | 快速录入完整日期时间戳到mlog(%Y-%m-%d %H:%M:%S) |
| ctrl+d       | 快速录入日期时间戳到mlog(%Y-%m-%d %H:%M)        |
| ctrl+shift+t | 快速录入时间戳到mlog(%H:%M:%S)                  |
| alt+1        | 将事项转为todo状态                              |
| alt+2        | 将事项转为next状态                              |
| alt+3        | 将事项转为work状态                              |
| alt+4        | 将事项转为done状态                              |
| alt+5        | 将事项转为reopen状态，BUG修复后被打开时使用     |

### 其他 ###

 Snippet | 应用场景                                                                                                             | 快速录入 | 快捷键 | 默认内容                                                                                                                                                                                                                                                                                 |
|---------|----------------------------------------------------------------------------------------------------------------------|----------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INIT    | MLOG记录创建时，作为记录注释使用，提供文档说明、类别、作者、链接、版本号等语义化条目。方便后期人为或机器维护和存档。 | init     |        | /**   *----------------------------------------//   * mlog description   *----------------------------------------//   *@category,mlogcategory[Study,Work,School,Family...]   *@author,mlog author,who write this log   *@link,contact   *@version,mlog version   *@stamp,what time? **/ |




English
-

### Personal Bussiness domain ###

| Snippet | Aim                                              | Hot word  | Hot key | Default content                 |
|---------|--------------------------------------------------|-----------|---------|---------------------------------|
| TODO    | mark this item should to do as soon as possiable | td,TODO   |         | ** TODO,what do to ?            |
| NEXT    | mark this item must to do next                   | nt,NEXT   |         | ** NEXT,what to do next ?       |
| WORK    | mark this item is processing                     | wk,WORK   |         | ** WORK,what to do in work?     |
| DONE    | mark this item has finished                      | done,DONE |         | ** DONE,what time ?,what done?. |


### Software development domain ###

| Snippet | Aim                                      | Hot word   | Hot key | Default content                            |
|---------|------------------------------------------|------------|---------|--------------------------------------------|
| Delay   | mark this BUG is blocked,should be delay | dl,Delay   |         | /* bug number */,Delay /* your commit */   |
| Fixed   | mark this BUG has fixed                  | fx,Fixed   |         | /* bug number */,Fixed /* your commit */   |
| Refused | mark this BUG has refused by developer   | rf,Refused |         | /* bug number */,Refused /* your commit */ |

### Warning level domain ###

| Snippet    | Aim                                          | Hot word      | Hot key | Default content |
|------------|----------------------------------------------|---------------|---------|-----------------|
| #DEFAULT   | Mark this item as default warning level item | df,Defalt     |         | #DEFAULT this   |
| #SUCCESS   | Mark this item as success level item         | sc,Success    |         | #SUCCESS this   |
| #WARNING   | Mark this item as warning level item         | wn,Warning    |         | #WARNING this   |
| #IMPORTANT | Mark this item as important level item       | ipt,Important |         | #IMPORTANT this |
| #INFO      | Mark this item as info level item            | if,Info       |         | #INFO this      |
| #ERROR     | Mark this item as error level item           | er,Error      |         | #ERROR this     |
| #INVERSE   | Mark this item as inverse level item         | iv,Inverse    |         | #INVERSE this   |
| #1         | Mark this item as level one warning item     | l1            |         | #1              |
| #2         | Mark this item as level two warning item     | l2            |         | #2              |
| #3         | Mark this item as level three warning item   | l3            |         | #3              |
| #4         | Mark this item as level four warning item    | l4            |         | #4              |
| #5         | Mark this item as level five warning item    | l5            |         | #5              |
| #6         | Mark this item as level six warning item     | l6            |         | #6              |
| #7         | Mark this item as level seven warning item   | l7            |         | #7              |
| #8         | Mark this item as level eight warning item   | l8            |         | #8              |
| #9         | Mark this item as level night warning item   | l9            |         | #9              |
| #10        | Mark this item as level ten warning item     | l10           |         | #10             |


### Hot Keys ###

| Keys         | Aim                                           |
|--------------|-----------------------------------------------|
| ctrl+shift+d | add datetime stamp to mlog(%Y-%m-%d %H:%M:%S) |
| ctrl+d       | add date stamp to mlog(%Y-%m-%d %H:%M)        |
| ctrl+shift+t | add time stamp to mlog(%H:%M:%S)              |
| alt+1        | translate this item state to todo             |
| alt+2        | translate this item state to next             |
| alt+3        | translate this item state to work             |
| alt+4        | translate this item state to done             |
| alt+5        | translate this item state to reopen           |


### Other ###

| Snippet | Aim                                                                                                                                                                                                                | Hot word | Hot key | Default content                                                                                                                                                                                                                                                                          |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INIT    | After mlog file created, this snippet should generate as file description. this snippet supported semantic description、category、author、link、version and so on，for human or matchine to maintenance easy late. | init     |         | /**   *----------------------------------------//   * mlog description   *----------------------------------------//   *@category,mlogcategory[Study,Work,School,Family...]   *@author,mlog author,who write this log   *@link,contact   *@version,mlog version   *@stamp,what time? **/ |
