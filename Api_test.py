import requests

API_URL="https://random.dog/woof.json"

bigger_count=0
lower_count=0


for i in range(10):


    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Hata varsa raise ediyoruz
        
        r_dict=response.json()

        # Boyut kontrolü
        if r_dict["fileSizeBytes"]>1050000:
            bigger_count += 1
            print(r_dict["fileSizeBytes"])

            
        else:
            lower_count+=1
            print(r_dict["fileSizeBytes"])
            
    except requests.RequestException as e:
        print(f"Error on request {i + 1}: {e}")



print(f"105000 byte ve üzeri olan dosya sayısı :  {bigger_count}")
print(f"105000 byte ve aşağısı olan dosya sayısı :  {lower_count}")
