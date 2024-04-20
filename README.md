
<h1 align="center">
    🔱 ParamSpider
  <br>
</h1>

<h4 align="center">  Mining URLs from Dark Corners of Web Archives for Bug Hunting / Fuzzing / Further Probing </h4>

<p align="center">•
  <a href="#-about"> 📖 About </a> •
  <a href="#-installation"> 🏗️ Installation </a> •
  <a href="#-usage"> 🛠 Usage </a> •
  <a href="#-examples"> 🚀 Examples </a> •
  <a href="#-contributing"> 🤝 Contributing </a> •
  <a href="#-upgraded-by-"> 🥷🏻 Social </a> •
  <a href="#-just-4-fun"> 💀 Fun </a> •
</p>

![paramspider](https://github.com/PushkraJ99/ParamSpider/blob/master/static/paramspider.png?raw=true)
<br><br>

ParamSpider Allows you to Fetch URLs Related to any Domain or a List of Domains from Wayback Achives. It Filters Out "boring" URLs, Allowing you to Focus on the Ones that Matter the Most.

---

### 📖 About

- Finds Parameters From Web Archives of the Entered Domain.
- Finds Parameters from Subdomains as Well.
- Gives Support to Exclude URLs with Specific Extensions.
- Saves the Output Result in a Nice and Clean Manner.
- It Mines the Parameters from Web Archives ( Without Interacting with the Target Host )
- New Features Added 
- Scanning for Subdomains of Target Domain OR Target Domain List
- Saving Combined Output of Domain List with Separate Domain Wise URLs and Combined URLs

---

## 📥 Installation
To Install `paramspider`, Follow These Steps:

```sh
git clone https://github.com/PushkraJ99/ParamSpider
cd ParamSpider
pip install .
paramspider -h
```
OR
```sh
git clone https://github.com/PushkraJ99/ParamSpider ; cd ParamSpider ; pip install . ; paramspider -h
```

If You Are Using Kali Linux and Getting Error `paramspider not found` try This Command
```sh
sudo cp ~/.local/bin/paramspider /usr/local/bin/
```

---

## 💀 Usage
<b> To Use `paramspider`, Follow These Steps </b>

```sh
paramspider -d domain.com
```

---

## 🚀 Examples
Here are a Few Examples of How to Use `paramspider`

- Discover URLs for a Single Domain
```sh
   paramspider -d domain.com
```
- Discover URLs for a Single Domain with Subdomains
```sh
   paramspider -d domain.com --subs
```
![paramspider](https://github.com/PushkraJ99/ParamSpider/blob/master/static/domainscan.png?raw=true)

- Save URLs Output for a Single Domain
```sh
  paramspider -d domain.com --subs -o fuzz.txt
```
![paramspider](https://github.com/PushkraJ99/ParamSpider/blob/master/static/output.png?raw=true)

- Discover URLs for Multiple Domains from a File
```sh
  paramspider -l list.txt
```

- Discover URLs for Multiple Domains with Subdomains from a File 
```sh
  paramspider -l list.txt --subs
```
![paramspider](https://github.com/PushkraJ99/ParamSpider/blob/master/static/listscan.png?raw=true)

- Stream URLs on Terminal
```sh 
  paramspider -d domain.com -s
```

- Set up Web Request Proxy
```sh
  paramspider -d domain.com --proxy '127.0.0.1:7890'
```

- Adding a Placeholder for URL Parameter Values (default: "FUZZ")
```sh
  paramspider -d domain.com -p '"><h1>reflection</h1>'
```

---

## 🤝 Contributing
Contributions are Welcome! If you'd like to Contribute to `paramspider` Please Follow These Steps

1. Fork the Repository.
2. Create a New Branch.
3. Make Your Changes and Commit them.
4. Submit a Pull Request.

---

### 🫣 Author 
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/devanshbatham)

---

### 🥷🏻 UPGRADED BY :) 
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PushkraJ99)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name=PushkraJ99) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pushkaraj-dhuri/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/you_are_not_goodlooking_but_he)

---
### 🤗 JUST 4 FUN
### ✨ Stargazers
[![Stargazers repo roster for @PushkraJ99/NucleiFuzzer](https://reporoster.com/stars/dark/notext/PushkraJ99/ParamSpider)](https://github.com/PushkraJ99/ParamSpider/stargazers)

### ☢️ Forkers 
[![Forkers repo roster for @PushkraJ99/ParamSpider](https://reporoster.com/forks/dark/notext/PushkraJ99/ParamSpider)](https://github.com/PushkraJ99/ParamSpider/network/members)

## 🐍 [Snake4Readme](https://github.com/PushkraJ99/Snake4Readme)

<p align="center">
<img src="https://github.com/PushkraJ99/Snake4Readme/blob/main/Snake4Readme/grid-snake.svg">
</p><br>

[![](https://visitcount.itsvg.in/api?id=PushkraJ99&icon=8&color=12)](https://visitcount.itsvg.in)

<p align="center"> 
  <b> Visitor Count </b><br>
  <img src="https://profile-counter.glitch.me/PushkraJ99/count.svg" />
</p><br>

