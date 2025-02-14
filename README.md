<div align="center">

# [![beast](https://github.com/crut0i/Beast_Bomber/assets/80776324/14fc365c-1e28-4733-b607-bec1f2d9d105)](https://t.me/beast_project_team)

# Beast Bomber 💣

​​​​​​</br> [![Button](https://user-images.githubusercontent.com/80776324/234415221-021db78d-8949-4da8-bf54-f9ae21628d41.png)](https://github.com/crut0i/Beast_Bomber/fork) [![Discord](https://user-images.githubusercontent.com/80776324/234414710-496d8ec0-992f-409e-a0c7-bf70df85d948.png)](https://discord.gg/qkK4NG4ARU)

</div>

# 📌 Menu / Меню

📌 [<kbd>EN</kbd>](#-en)
- [<kbd>Installation</kbd>](#-installation)
- [<kbd>First setup</kbd>](#-first-setup)
- [<kbd>SMS</kbd>](#-sms-info)
- [<kbd>Discord</kbd>](#-discord-info)
- [<kbd>DDoS</kbd>](#-ddos-info)
- [<kbd>Email</kbd>](#-email-info)
- [<kbd>Telegram</kbd>](#-telegram-info)
- [<kbd>Problems and their solutions</kbd>](#-problems-and-their-solutions)
- [<kbd>Donate for coffee</kbd>](#-donate-for-coffee)

📌 [<kbd>RU</kbd>](#-ru)
- [<kbd>Установка</kbd>](#-установка)
- [<kbd>Первая настройка</kbd>](#-первая-настройка)
- [<kbd>СМС</kbd>](#-смс-инфо)
- [<kbd>Discord</kbd>](#-discord-инфо)
- [<kbd>DDoS</kbd>](#-ddos-инфо)
- [<kbd>Email</kbd>](#-email-инфо)
- [<kbd>Telegram</kbd>](#-telegram-инфо)
- [<kbd>Проблемы и их решения</kbd>](#-проблемы-и-их-решения)
- [<kbd>Автору на кофе</kbd>](#-автору-на-кофе)

# 📌 EN

<div align="center">
  
  ## **Use this script for educational purposes only and do not abuse it. Only YOU are responsible for its use**
  ![Screenshot_1](https://github.com/un1cum/Beast_Bomber/assets/80776324/50f44435-3431-4854-9de3-0f5a17803ea7)

</div>

`Possibilities`
* SMS attack
* Email attack
* Discord attack
* Telegram attack
* DDoS attack
* Multilanguage

# 📌 Installation

![tutorial](https://user-images.githubusercontent.com/80776324/230665884-f52bb3d8-b20d-4275-9afc-0f5068eeaf82.gif)

- To run the beast bomber you need to download Python: https://www.python.org


  ```
  git clone https://github.com/un1cum/Beast_Bomber
  ```

- P.S
  - If you don't have git, you need to install it: https://git-scm.com/downloads
  - If you install Beast Bomber manually, without git, be sure to delete the .gitkeep file in the input\telegram_accounts folder
  - To get started, you need to install the necessary Python libraries. Go to the Beast_Bomber folder and enter this command in cmd or terminal:  


    ```
    pip install -r requirements.txt
    ```

- To start the bomber, enter this command:


  ```
  python beast.py
  ```

# 📌 First setup

- For a DDoS attack to work correctly, you need to enter **proxies** into the input\proxies.txt file or automatically parse them using the built-in function
  - Proxies format: `ip:port` or `user:pass@ip:port`
- For the Telegram attack to work, you need to put the Telegram accounts in **tdata** format (each account in a separate folder) in the input\telegram_accounts folder
- To make email spam work, you need to put email accounts in the format **email:password** in the input\email_accounts.txt file
- For discord spam to work, you must place **tokens** from discord accounts in the file input\discord_accounts.txt

# 📌 SMS info

Beast Bomber supports **ONLY Russian and Kazakh** phone numbers.

# 📌 Discord info

To send messages in Discord, you need to specify the **ID of the target**, it can be found in the url of the discord dialog in your browser.


![discord](https://user-images.githubusercontent.com/80776324/230663913-d68dbf58-0738-4501-9539-17daf0d36753.png)

# 📌 DDoS info

**Test results from dstat.**

![screenshot](https://user-images.githubusercontent.com/80776324/214398918-81d488c7-e23a-4dc3-864b-3b82b1c55571.png)

| Threads | Attack time |
|---------|-------------|
|   40    | 60 seconds  |

# 📌 Email info

Beast Bomber supports the following email services (from which spam will be sent): **mail.ru, yahoo, rambler**

# 📌 Telegram info

How the script sends messages:


Beast Bomber logs into the accounts that you put in your input\telegram_accounts folder and sends the message you write from them.


You can buy tdata telegram accounts here: [click](https://darkstore.biz/?search_triggered=true&category_id=43&group_id=&sort=-purchase_counter&feature=) **(not advertising)**

# 📌 Problems and their solutions

``If you see something like this:``

![error](https://github.com/un1cum/Beast_Bomber/assets/80776324/f6a72474-dc25-42bd-ba93-638270f4c77f)

This means that you don't have the library that is specified in the error, in this case: "_ctypes". You need to enter in the terminal or cmd:

* pip install <the name of the required library> 

``Example:``

```
pip install _ctypes
```

``If you install Beast Bomber on the termux:``

You may have a problem installing the **opentele** library, to fix it enter the following command: 

```
pkg install pyqt5 python-pyqtwebengine
```

then reinstall the **opentele** library.

# 📌 Donate for coffee

* ![BNB](https://user-images.githubusercontent.com/80776324/230691108-ecd10132-af58-4064-8c44-ad10f6f55dd1.png) **BNB: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1**


* ![BTC](https://user-images.githubusercontent.com/80776324/230691099-1422c66c-099e-49f2-adee-b48fa9533c0c.png) **BTC: bc1qxfvstf99kyuc5x5uugxtsh3m6w3a73ruzfav7e**


* ![ETH](https://user-images.githubusercontent.com/80776324/230691090-32c937b9-61bc-4eeb-b058-c46c8fc250ac.png) **ETH: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1**


* ![LTC](https://user-images.githubusercontent.com/80776324/230691072-c3bc7a2b-7e4e-4a4b-ab56-e82ee5ffb717.png) **LTC: ltc1qudx4ge8zvncqpdtl5mshfqjxzyvg43f27ysqjt**


* ![USDT](https://user-images.githubusercontent.com/80776324/230691044-44802059-c433-4de5-a221-0f69c0b7c660.png) **USDT (TRC-20): TKVs4Bt63mVGSYth7HSvNQBk8Xp1UKMH9Y**


<div align="center">
  
# ❤️ Thank you all for your contributions to the project

</div>


# 📌 RU

<div align="center">
  
  ## **Используйте данный скрипт только в образовательных целях и не злоупотребляйте этим. Вся ответственность за его использование ложится НА ВАС**
  ![Screenshot_1](https://github.com/un1cum/Beast_Bomber/assets/80776324/50f44435-3431-4854-9de3-0f5a17803ea7)

</div>

`Возможности`
* SMS атака
* Email атака
* Discord атака
* Telegram атака
* DDoS атака
* Поддержка двух языков

# 📌 Установка

![tutorial](https://user-images.githubusercontent.com/80776324/230665884-f52bb3d8-b20d-4275-9afc-0f5068eeaf82.gif)

- Для работы beast bomber вам нужно установить Python: https://www.python.org


  ```
  git clone https://github.com/un1cum/Beast_Bomber
  ```

- P.S
  - Если у вас нет git, вам нужно установить его: https://git-scm.com/downloads
  - Если будете устанавливать Beast Bomber вручную, без git, то обязательно удаляйте файл .gitkeep в папке input\telegram_accounts
  - Чтобы начать работу, вам нужно установить необходимые библиотеки Python. Зайдите в папку Beast_Bomber и введите в cmd или terminal эту команду: 


    ```
    pip install -r requirements.txt
    ```
    
    
- Чтобы запустить бомбер, введите это:


  ```
  python beast.py
  ```

# 📌 Первая настройка

- Для корректной работы DDoS атаки необходимо поместить прокси в файл input\proxies.txt или автоматически спарсить их с помощью встроенной функции
  - Формат прокси: `ip:port` или `user:pass@ip:port`
- Чтобы атака Telegram работала, необходимо поместить аккаунты Telegram в формате **tdata** (каждый аккаунт в отдельной папке) в папку input\telegram_accounts
- Чтобы спам по электронной почте работал, вам нужно поместить учетные записи электронной почты в формате **email:пароль** в файл input\email_accounts.txt
- Для того, чтобы работал спам в Discord, вы должны поместить **токены** от аккаунтов Discord в файл input\discord_accounts.txt

# 📌 СМС инфо

Beast Bomber поддерживает **ТОЛЬКО русские и казахские** номера телефонов.

# 📌 Discord инфо

Чтобы отправлять сообщения в Discord, вам нужно указать **ID цели**, его можно найти в url диалога discord в вашем браузере.


![discord](https://user-images.githubusercontent.com/80776324/230664016-2cb6d111-15fb-422e-ae3d-d38ead9bcbb2.png)

# 📌 DDoS инфо

**Результаты теста с dstat.**

![screenshot](https://user-images.githubusercontent.com/80776324/214398918-81d488c7-e23a-4dc3-864b-3b82b1c55571.png)

| Потоки  | Время атаки |
|---------|-------------|
|   40    |  60 секунд  |

# 📌 Email инфо

Beast Bomber поддерживает следующие почтовые сервисы: **mail.ru, yahoo, rambler**

# 📌 Telegram инфо

Как скрипт отправляет сообщения:


Beast Bomber входит в аккаунты, которые Вы поместили в папку input\telegram_accounts и отправляет от них сообщение, которое Вы указали.


Купить telegram аккаунты в формате tdata можно тут: [тык](https://darkstore.biz/?search_triggered=true&category_id=43&group_id=&sort=-purchase_counter&feature=) **(не реклама)**

# 📌 Проблемы и их решения

``Если у вас похожая ошибка:``

![error](https://github.com/un1cum/Beast_Bomber/assets/80776324/f6a72474-dc25-42bd-ba93-638270f4c77f)

Это означает, что у вас отсутствует нужная библиотека pip, в этом случае: "_ctypes". Откройте терминал, cmd или что там у вас и пишите:

* pip install <имя отсутствующей библиотеки>

``Пример:``

```
pip install _ctypes
```

``Если вы устанавливаете Beast Bomber на termux:``

У вас может возникнуть пробоема с установкой библиотеки **opentele**, чтобы исправить её, введите следующую команду: 

```
pkg install pyqt5 python-pyqtwebengine
```

затем повторите установку **opentele**.

# 📌 Автору на кофе

* ![BNB](https://user-images.githubusercontent.com/80776324/230691108-ecd10132-af58-4064-8c44-ad10f6f55dd1.png) **BNB: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1**


* ![BTC](https://user-images.githubusercontent.com/80776324/230691099-1422c66c-099e-49f2-adee-b48fa9533c0c.png) **BTC: bc1qxfvstf99kyuc5x5uugxtsh3m6w3a73ruzfav7e**


* ![ETH](https://user-images.githubusercontent.com/80776324/230691090-32c937b9-61bc-4eeb-b058-c46c8fc250ac.png) **ETH: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1**


* ![LTC](https://user-images.githubusercontent.com/80776324/230691072-c3bc7a2b-7e4e-4a4b-ab56-e82ee5ffb717.png) **LTC: ltc1qudx4ge8zvncqpdtl5mshfqjxzyvg43f27ysqjt**


* ![USDT](https://user-images.githubusercontent.com/80776324/230691044-44802059-c433-4de5-a221-0f69c0b7c660.png) **USDT (TRC-20): TKVs4Bt63mVGSYth7HSvNQBk8Xp1UKMH9Y**


<div align="center">
  
# ❤️ Спасибо всем за ваши вклады в проект

</div>

