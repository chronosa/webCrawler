# 11번가 티켓 모니터링 스크립트
특정 URL의 잔여 좌석을 모니터링하기 위한 스크립트. 좌석이 1 이상일 경우 Slack Webhook을 통해 Noti를 보내도록 구성

## 실행방법
1. requirements.txt의 package 설치
2. config.py 파일 생성 및 설정
[예시]
```
CONFIG = {
    TargetUrl: "",
    "WebhookUrl" : "",
    "ExceptDays" : []
}
3. Crontab 등록 후 실행
```

## 사전 필요사항
### Windows Driver Download
Windows는 아래 명령어를 수행하여 Chrome Driver 설치  
```
# Uri는 Chrome 버전에 따라 수정 필요
Invoke-WebRequest -OutFile chromedriver_win32.zip -Uri https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
Expand-Archive -Force .\chromedriver_win32.zip
```

### Linux Chrome 및 Chrome Driver Install
Execute install_chrome.sh (※Ubuntu 18.04)  

### Crontab
crontab에 등록 (예시)
```
(* * * * * sh -c "PATH=$PATH:/usr/local/bin; python3 /home/user/workspace/webCrawler/app.py >> /tmp/temp.log 2>&1") | crontab -
```
