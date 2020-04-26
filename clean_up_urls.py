lines = open("urls.txt", "r").readlines()
actual_urls = open("urls_new.txt", "w")
urls = []
for line in lines:
    if line.split(" ")[0].strip().isdigit():
        continue
    else:
        print(line.split(" ")[-1].strip())
        actual_urls.write(line.split(" ")[-1].strip())
        actual_urls.write("\n")

actual_urls.close()
        
