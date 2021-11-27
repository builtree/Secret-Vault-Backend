# Secret-Vault-Backend

![image](https://user-images.githubusercontent.com/60029463/131047936-61b6ba45-4c97-4623-8143-5490d398c3bc.png)

# Self hosted API Key / Secrets manager

## Sign up (Limited to cURL and CLI)
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
 
 ## Login (Limited to cURL and CLI)
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


 ## Add a bucket (Limited to cURL and CLI)
### `/login`
```bash
curl --request POST \
--url 'https://secret-vault.herokuapp.com/add_bucket' \
--header 'Content-Type: application/json' \
--header 'token: {your_token}' \
--data \
  '{
      "bucket_name" : "your_bucket_name",
      "username" : "your_username"
  }'
 ```
 

 ## Get list of buckets (Limited to cURL and CLI)
### `/get_buckets/{username}`
```bash
curl --request GET \
  --url 'https://secret-vault.herokuapp.com/get_buckets/{your_username}' \
  --header 'token: {your_token}'
 ```



 ## Add an Item to Bucket (Limited to cURL and CLI)
### `/add_item`
```bash
curl --request POST \
--url 'https://secret-vault.herokuapp.com/add_item' \
--header 'Content-Type: application/json' \
--header 'token: {your_token}' \
--data '{
	"username" : "your_username",
	"bucket_name" : "your_bucket_name",
	"name" : "item_name",
	"value" : "item_value"
}'
 ```


 ## Get list of Items in a bucket (Limited to cURL and CLI)
### `/get_items/{username}/{bucket_name}`
```bash
curl --request GET \
  --url 'https://secret-vault.herokuapp.com/get_items/{username}/{bucket_name}' \
  --header 'token: {your_token}'
 ```

 # System Design 
 ![image](https://github.com/AvikantSrivastava/Secret-Vault-Backend/blob/main/system_design.png)
