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
### Correct Response 使用者成功創建
```
{
	"message": "User created successfully."
}
```
### Error Response 使用者名稱重複
```
{
	"code": 409,
	"message": "A user with that username already exists.",
	"status": "Conflict"
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
### Correst Response 登入成功
```
{
	"access_token": _access_token_ ,
	"refresh_token": _refresh_token_
}
```

### Error Response 登入失敗
```
```
{
	"code": 401,
	"message": "Invalid credentials",
	"status": "Unauthorized"
}
```


