echo "Installing apt-get..."
apt-get update
apt-get upgrade -y

echo "Installing all dependencies..."
sudo apt-get update && sudo apt-get install -y \
 build-essential \
 curl \
 libcurl3-dev \
 git \
 libfreetype6-dev \
 libpng12-dev \
 libzmq3-dev \
 pkg-config \
 python-dev \
 python-numpy \
 python-pip \
 software-properties-common \
 swig \
 zip \
 zlib1g-dev

sudo apt-get install -y libstdc++6

sudo add-apt-repository ppa:ubuntu-toolchain-r/test 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo pip install -y grpcio

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

sudo pip install tensorflow

echo "Installing git..."
apt-get install -y git

echo "installing curl..."
apt install -y curl

sudo pip install tensorflow-serving-api
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install -y tensorflow-model-server

