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
Correst Response 登入成功會取得由**jwt**生成的token，要使用後續的api，大部分都需要在**http header**提供此token，token會帶有用戶id
token的使用方式請參考 https://medium.com/%E4%BC%81%E9%B5%9D%E4%B9%9F%E6%87%82%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88/jwt-json-web-token-%E5%8E%9F%E7%90%86%E4%BB%8B%E7%B4%B9-74abfafad7ba
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
僅須提供token






