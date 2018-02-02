## raspberry pi skywriter

_currently customized file 현재 사용할 파일_

examples
|
|____ test.py


_raspberry linux command 라즈베리 리눅스 커맨드_

```bash
$ python3 test.py
```

_주의사항_

In test.py, you should change the variable *broker_address* depend on where you're running your mosca broker. 

test.py에 있는 broker_address 변수: 모스카 브로커를 돌리고 있는 ip address 값으로 변경해야 한다.


_mosca broker 모스카 브로커_

```bash
$ mosca -v | pino
//간단한 log 만 나옴
$ mosca --very-verbose | pino -t -l
//자세한 log 나옴

//일렉트론 앱이랑 같이 띄우려고 하면 ::1883 EADDIRINUSE 에러가 날 때가 있음. (nodejs 포트 에러인것 같음)
//다 kill 하고, 일렉트론 앱 실행하고, mosca 띄우기
$ killall -9 node   //로 kill
$ ps ax  //로 체크


//보통 이걸로 linux에서 listening port kill 한다는데, 잘안됐음.
$ kill $(lsof -t -i:1883)
$ lsof -i:1883


//참고로 1883은 mosca 기본 port
```

_프로세스 순서 (커맨드 터미널은 다 다른 location)_

```bash
$ killall -9 node

/demo/second/ $ npm run dev

$ mosca --very-verbose | pino -t -l

$ python3 test.py
```


