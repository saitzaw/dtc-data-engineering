# Copy file 
copy File from windows to wsl [copy from WSL terminal]
```shell
cp /mnt/c/Users/YourUsername/Downloads/file.txt ~/file.txt
```

copy File form wsl to host [copy from WSL terminal]
```shell
cp ~/file.txt /mnt/c/Users/YourUsername/Downloads/file.txt
```

# Login to psql 
psql -h localhost -p 5432 -U user 