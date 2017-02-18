#!/bin/bash

sudo add-apt-repository ppa:graphics-drivers/ppa   
sudo apt-get update   
sudo apt-get upgrade 

sudo apt-get install nvidia-370

sudo apt-get install python3.5 vim git

sudo apt-get install dconf-cli
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git
cd gnome-terminal-colors-solarized
./install.sh

mkdir -p ~/.vim/autoload ~/.vim/bundle && \
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
echo "execute pathogen#infect()" > ~/.vimrc
cd ~/.vim/bundle
git clone https://github.com/tpope/vim-surround
git clone https://github.com/kien/ctrlp.vim
git clone https://github.com/altercation/vim-colors-solarized
git clone https://github.com/bling/vim-airline
