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
Correct Response 使用者成功創建
```
{
	"message": "User created successfully."
}
```
Error Response 使用者名稱重複
```
{
	"code": 409,
	"message": "A user with that username already exists.",
	"status": "Conflict"
}
```

## POST   /login 登入
提供username與password
```
{
	"username": "jesse1",
	"password": "testing"	
}
```
Correst Response 登入成功會取得由__jwt__生成的token，要使用後續的api，大部分都需要在http header提供此token
```
{
	"access_token": "token" ,
	"refresh_token": "token"
}
```

Error Response 登入失敗

```
{
	"code": 401,
	"message": "Invalid credentials",
	"status": "Unauthorized"
}
```

## POST   /logout 登入
### 提供於login取得的access token 放在Http Header中

Header內的內容是 Authorization: Bearer *access_token*




