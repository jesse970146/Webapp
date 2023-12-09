# API


## API_URL :　https://web-app-backend-r3ac.onrender.com



## POST   /register 創帳號
提供username與password
```json
{
	"username": "jesse1",
	"password": "testing"	
}
```
Correct Response 使用者成功創建
```json
{
	"message": "User created successfully."
}
```
Error Response 使用者名稱重複
```json
{
	"code": 409,
	"message": "A user with that username already exists.",
	"status": "Conflict"
}
```

## POST   /login 登入
提供username與password
```json
{
	"username": "jesse1",
	"password": "testing"	
}
```
Correst Response 

登入成功會取得由**jwt**生成的token，要使用後續的api，大部分都需要在**http header**提供此token，token會帶有用戶id

token的使用方式請參考 https://medium.com/%E4%BC%81%E9%B5%9D%E4%B9%9F%E6%87%82%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88/jwt-json-web-token-%E5%8E%9F%E7%90%86%E4%BB%8B%E7%B4%B9-74abfafad7ba
```json
{
	"access_token": "token" ,
	"refresh_token": "token"
}
```

Error Response 登入失敗

```json
{
	"code": 401,
	"message": "Invalid credentials",
	"status": "Unauthorized"
}
```

## POST   /logout 登出
僅須提供token便可登出，登出後token會被儲存在database，下次使用會被拒絕

Correct Response 成功登出
```json
{
	"message": " Sucessfully logout"
}
```
若用戶已登出，使用相同token，會出現
```json
{
	"descripition": "The token has been revoked",
	"error": "token_revoked"
}
```
告訴用戶token已經被移除

## 方便測試用的API，之後會刪除
## GET   /user
可以得知創建的所有帳號內容

## GET   /user/<user_id>
可以得知創建的特定帳號的內容

## DELETE   /user/<user_id>
可以刪除創建的特定帳號的內容







