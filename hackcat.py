#!/bin/bash

# Title: HACKCAT Toolkit v2.0
# Developer: qwexsa

# Welcome Banner
python -c "from cfonts import render; qawe = render('HACKCAT', colors=['red', 'green', 'white'], align='center', font='block'); print(qawe)"
echo -e "\e[1m\e[32mDeveloper:\e[0m \e[1m\e[36mqwexsa\e[0m"
echo -e "\e[33mDiscord: qawexsa\e[0m"
echo -e "\e[33m ➛ Welcome to my own hacking toolkit <3\e[0m"
echo -e "\e[36m ➛ Kendi hack araç kit'ime hoşgeldin <3\e[0m"
echo ""

# Menu function
main_menu() {
  echo -e "\033[1;37m [1] > Information Gathering Tools < \e[0m"
  echo -e "\033[1;37m [2] > SQL Injection Tools < \e[0m"
  echo -e "\033[1;37m [3] > Wireless Attack Tools < \e[0m"
  echo -e "\033[1;37m [4] > Phishing Attack Tools < \e[0m"
  echo -e "\033[1;37m [5] > Web Attack Tools < \e[0m"
  echo -e "\033[1;37m [6] > Forensic Tools < \e[0m"
  echo -e "\033[1;37m [7] > DDOS Attack Tools < \e[0m"
  echo -e "\033[1;37m [8] > Wordlist Generator < \e[0m"
  echo -e "\033[1;37m [9] > Sniffing & Spoofing Tools < \e[0m"
  echo -e "\033[1;37m [10] > Password Attack Tools < \e[0m"
  echo -e "\033[1;37m [11] > Social Engineering Tools < \e[0m"
  echo -e "\033[1;37m [12] > XSS Attack Tools < \e[0m"
  echo -e "\033[1;37m [13] > Network Pentesting Tools < \e[0m"
  echo -e "\033[1;37m [14] > Other Tools < \e[0m"
  echo -e "\033[1;37m [99] > Exit < \e[0m"
  echo ""

  read -p "Please make a selection > " secim

  case $secim in
    1) info_gathering ;;
    2) sql_injection ;;
    3) wireless_attack ;;
    4) phishing_attack ;;
    5) web_attack ;;
    6) forensic_tools ;;
    7) ddos_attack ;;
    8) wordlist_gen ;;
    9) sniffing_spoofing ;;
    10) password_attacks ;;
    11) social_eng ;;
    12) xss_attack ;;
    13) network_pentest ;;
    14) other_tools ;;
    99) exit_message ;;
    *) 
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      main_menu
      ;;
  esac
}

# Category 1: Information Gathering Tools
info_gathering() {
  echo -e "\033[1;32m You selected Information Gathering Tools! \e[0m"
  echo -e "\033[1;33m [1] > theHarvester < \e[0m"
  echo -e "\033[1;33m [2] > Dmitry < \e[0m"
  echo -e "\033[1;33m [3] > Nmap < \e[0m"
  echo -e "\033[1;33m [4] > Maltego < \e[0m"
  echo -e "\033[1;33m [5] > Recon-ng < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose an Information Gathering Tool > " infoselect
  case $infoselect in
    1)
      git clone https://github.com/laramies/theHarvester
      ;;
    2)
      git clone https://github.com/jaygreig86/dmitry
      ;;
    3)
      sudo apt install nmap
      ;;
    4)
      echo -e "\033[1;32m Please download Maltego manually from https://www.maltego.com/downloads/ \e[0m"
      ;;
    5)
      git clone https://github.com/lanmaster53/recon-ng
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      info_gathering
      ;;
  esac
}

# Category 2: SQL Injection Tools
sql_injection() {
  echo -e "\033[1;32m You selected SQL Injection Tools! \e[0m"
  echo -e "\033[1;33m [1] > sqlmap < \e[0m"
  echo -e "\033[1;33m [2] > jSQL Injection < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose an SQL Injection Tool > " sqlselect
  case $sqlselect in
    1)
      git clone https://github.com/sqlmapproject/sqlmap
      ;;
    2)
      git clone https://github.com/ron190/jsql-injection
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      sql_injection
      ;;
  esac
}

# Category 3: Wireless Attack Tools
wireless_attack() {
  echo -e "\033[1;32m You selected Wireless Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > Aircrack-ng < \e[0m"
  echo -e "\033[1;33m [2] > Reaver < \e[0m"
  echo -e "\033[1;33m [3] > Wifite < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Wireless Attack Tool > " wireselect
  case $wireselect in
    1)
      sudo apt install aircrack-ng
      ;;
    2)
      sudo apt install reaver
      ;;
    3)
      git clone https://github.com/derv82/wifite
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      wireless_attack
      ;;
  esac
}

# Category 4: Phishing Attack Tools
phishing_attack() {
  echo -e "\033[1;32m You selected Phishing Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > HiddenEye < \e[0m"
  echo -e "\033[1;33m [2] > SocialFish < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Phishing Attack Tool > " phishselect
  case $phishselect in
    1)
      git clone https://github.com/DarkSecDevelopers/HiddenEye
      ;;
    2)
      git clone https://github.com/An0nUD4Y/SocialFish
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      phishing_attack
      ;;
  esac
}

# Category 5: Web Attack Tools
web_attack() {
  echo -e "\033[1;32m You selected Web Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > XAttacker < \e[0m"
  echo -e "\033[1;33m [2] > Websploit < \e[0m"
  echo -e "\033[1;33m [3] > Commix < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Web Attack Tool > " webselect
  case $webselect in
    1)
      git clone https://github.com/Moham3dRiahi/XAttacker
      ;;
    2)
      git clone https://github.com/websploit/websploit
      ;;
    3)
      git clone https://github.com/commixproject/commix
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      web_attack
      ;;
  esac
}

# Category 6: Forensic Tools
forensic_tools() {
  echo -e "\033[1;32m You selected Forensic Tools! \e[0m"
  echo -e "\033[1;33m [1] > Autopsy < \e[0m"
  echo -e "\033[1;33m [2] > Volatility < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Forensic Tool > " forenselect
  case $forenselect in
    1)
      sudo apt install autopsy
      ;;
    2)
      git clone https://github.com/volatilityfoundation/volatility
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      forensic_tools
      ;;
  esac
}

# Category 7: DDOS Attack Tools
ddos_attack() {
  echo -e "\033[1;32m You selected DDOS Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > Slowloris < \e[0m"
  echo -e "\033[1;33m [2] > LOIC < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a DDOS Attack Tool > " ddosselect
  case $ddosselect in
    1)
      git clone https://github.com/gkbrk/slowloris
      ;;
    2)
      git clone https://github.com/NewEraCracker/LOIC
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      ddos_attack
      ;;
  esac
}

# Category 8: Wordlist Generator
wordlist_gen() {
  echo -e "\033[1;32m You selected Wordlist Generator! \e[0m"
  echo -e "\033[1;33m [1] > Crunch < \e[0m"
  echo -e "\033[1;33m [2] > Cewl < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Wordlist Generator > " wordlistselect
  case $wordlistselect in
    1)
      sudo apt install crunch
      ;;
    2)
      sudo apt install cewl
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      wordlist_gen
      ;;
  esac
}

# Category 9: Sniffing & Spoofing Tools
sniffing_spoofing() {
  echo -e "\033[1;32m You selected Sniffing & Spoofing Tools! \e[0m"
  echo -e "\033[1;33m [1] > Wireshark < \e[0m"
  echo -e "\033[1;33m [2] > Ettercap < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Sniffing & Spoofing Tool > " sniffselect
  case $sniffselect in
    1)
      sudo apt install wireshark
      ;;
    2)
      sudo apt install ettercap-graphical
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      sniffing_spoofing
      ;;
  esac
}

# Category 10: Password Attack Tools
password_attacks() {
  echo -e "\033[1;32m You selected Password Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > John the Ripper < \e[0m"
  echo -e "\033[1;33m [2] > Hydra < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Password Attack Tool > " passselect
  case $passselect in
    1)
      sudo apt install john
      ;;
    2)
      sudo apt install hydra
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      password_attacks
      ;;
  esac
}

# Category 11: Social Engineering Tools
social_eng() {
  echo -e "\033[1;32m You selected Social Engineering Tools! \e[0m"
  echo -e "\033[1;33m [1] > Social-Engineer Toolkit (SET) < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Social Engineering Tool > " socselect
  case $socselect in
    1)
      git clone https://github.com/trustedsec/social-engineer-toolkit
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      social_eng
      ;;
  esac
}

# Category 12: XSS Attack Tools
xss_attack() {
  echo -e "\033[1;32m You selected XSS Attack Tools! \e[0m"
  echo -e "\033[1;33m [1] > XSSer < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose an XSS Attack Tool > " xssselect
  case $xssselect in
    1)
      git clone https://github.com/epsylon/xsser
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      xss_attack
      ;;
  esac
}

# Category 13: Network Pentesting Tools
network_pentest() {
  echo -e "\033[1;32m You selected Network Pentesting Tools! \e[0m"
  echo -e "\033[1;33m [1] > Metasploit Framework < \e[0m"
  echo -e "\033[1;33m [2] > Nikto < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose a Network Pentesting Tool > " netselect
  case $netselect in
    1)
      curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfinstall | sh
      ;;
    2)
      sudo apt install nikto
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      network_pentest
      ;;
  esac
}

# Category 14: Other Tools
other_tools() {
  echo -e "\033[1;32m You selected Other Tools! \e[0m"
  echo -e "\033[1;33m [1] > Hashcat < \e[0m"
  echo -e "\033[1;33m [2] > Dirb < \e[0m"
  echo -e "\033[1;33m [99] > Back to Main Menu < \e[0m"

  read -p "Choose an Other Tool > " otherselect
  case $otherselect in
    1)
      sudo apt install hashcat
      ;;
    2)
      sudo apt install dirb
      ;;
    99)
      main_menu
      ;;
    *)
      echo -e "\033[1;31m Invalid selection! Please try again.\e[0m"
      other_tools
      ;;
  esac
}

# Exit message
exit_message() {
  echo -e "\033[1;32m Thank you for using the HACKCAT Toolkit! Stay safe and ethical! \e[0m"
  exit 0
}

# Start the script by calling the main menu
main_menu
