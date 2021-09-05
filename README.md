# Secret-Vault-Backend

![image](https://user-images.githubusercontent.com/60029463/131047936-61b6ba45-4c97-4623-8143-5490d398c3bc.png)

## Sign up (Limited to cURL)
### `/signup`
```bash
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "username" : "your_username",
  "password" : "your_password"
}' \
 'https://secret-vault.herokuapp.com/signup'
 ```
 
 ## Login (Limited to cURL)
### `/login`
```bash
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "username" : "your_username",
  "password" : "your_password"
}' \
 'https://secret-vault.herokuapp.com/login'
 ```
 
 # System Design 
 ![image](https://github.com/AvikantSrivastava/Secret-Vault-Backend/blob/main/system_design.png)
