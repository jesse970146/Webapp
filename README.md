# API

```
API_URL :　https://web-app-backend-r3ac.onrender.com
```


## POST   /register 創帳號
### 提供username與password

```
{
	"username": "jesse1",
	"password": "testing"	
}
```
### Response
```
{
	"message": "User created successfully."
}
```

## POST   /login 登入
### 提供username與password
```
{
	"username": "jesse1",
	"password": "testing"	
}
```
### Response
```
{
	"access_token": "_access_token_" ,
	"refresh_token": "_refresh_token_"
}
```








