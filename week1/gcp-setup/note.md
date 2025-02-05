## GCP account 
- create a GCP account 
- create a json for meta data
- create a VM 
- create a ssh connection to VM 
- Local setup with ssh 
- connect to vm and install 
    - anaconda 
        conda config --set auto_activate_base false
    - git 
    - wget 
    - docker 

## generate SSH key in wsl 
ssh-keygen -t rsa -b 4096 -C "alextun" -f ~/.ssh/gcp

## wsl [Linux config]
```shell
Host dtc-course
    HostName xx.xx.xx.xx
    User alextun
    IdentityFile /home/saithihazaw/.ssh/gcp
```


### Copy from Windows to Linux 
cp ~/.ssh/gcp.pub /mnt/c/Users/my_name/.ssh/gcp.pub
cp ~/.ssh/gcp /mnt/c/Users/my_name/.ssh/gcp



### using Powershell to the configure the config 
```powershell 
Host dtc-course
    HostName xx.xx.xx.xx
    User alextun
    IdentityFile C:/Users/saith/.ssh/gcp
```

## Run docker without permission [wsl, VM]
sudo groupadd docker 
sudo gpasswd -a $USER docker
sudo service docker restart

### Get the docker compose  
mkdir ~/bin
cd ~/bin 
wget link -O docker-compose
chmod +x docker-compose 

### Add the docker compose to path 
export PATH="${HOME}/bin:${PATH}
