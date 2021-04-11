### Windows Driver Download

```
# Uri는 Chrome 버전에 따라 수정 필요
Invoke-WebRequest -OutFile chromedriver_win32.zip -Uri https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
Expand-Archive -Force .\chromedriver_win32.zip
```