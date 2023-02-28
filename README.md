# http-security-header-checker
You can run it as follows.

To see how to use the tool, you can run it as follows.

python3 http-header-checker.py -h

![ss1](https://user-images.githubusercontent.com/33905344/221777946-e97b3e89-f42d-4487-b3a8-e2434d5c6a16.png)

If you are going to give a single target you can use the -t parameter.

python3 http-header-checker.py -t https://target.com

![ss2](https://user-images.githubusercontent.com/33905344/221778110-edcf07b5-b177-41ee-8a2d-b9a5b0d76113.png)

If you are going to give more than one target, you can use the -l parameter.

python3 http-header-checker.py -l target-list.txt

![ss3](https://user-images.githubusercontent.com/33905344/221778217-e1e8b57e-72b4-4db8-9e85-e2b805e4b6da.png)

If you want to get the output after the tool is running, you can use the -o parameter.

python3 http-header-checker.py -t https://target.com -o output.txt

python3 http-header-checker.py -l target-list.txt -o output.txt
