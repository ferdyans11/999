B
    ]A  �               @   s   d dl Z ee �d�� dS )�    Ns�  �            	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZm	Z	m
Z
 d dlmZ d dlmZ ejdd� ejdd�Zejd	d
d dd� e�� Zedd��Ze�� ZW dQ R X e�e�Zee
jej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j  d e
j ej d e
j ej d e
j ej! d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j  d e
j ej d  e
j  d! e
j ej d" e
j  d# � e
jej Z"e
j Z#e
jej Z$e
jej Z%e
jej Z&e
jej! Z'e �(� Z)d$Z*d%d&d'd(d)d*d+�Z+e,e-ed, �d- �Z.d.d/� Z/d0d1� Z0d2d3� Z1e)j2e*e+d4d5ed6 d7 ed6 d8 d9d:�d;�Z3e�e3j4�Z5y4ee"d< e$ d e# e6e-e5d= d> �d- � � W n   ed?� e�7�  Y nX e-e5d= d> �d- e-d@�k�rTee"dA � e�7�  e1e,e-edB �d- �e,e-edC �d- �� dS )D�    N)�Fore�Back�Style)�randint)�datetimeT)Z	autoresetz&Script Untuk Menuyul Website CowDollar)Zdescriptionz-cz--betsetz%Enter Your Betset Number (default: 0))�default�helpzconfig.json�rz�      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/z)
=======================================
zAuthor By  z: zKadal15
zChannel Yt �:z Jejaka Tutorialz
999 Dice Botz | zLose Streak �|z Win Streak
z:support by botakberambut(hijrah) And All Termux Id Member
zDonate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z         LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z         Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

z$https://www.999doge.com/api/web.aspxzfile://z�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36z!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-WithzBase Beti ��c             C   st   t dt| � d �}|dkrRt |�d�d �}dt|� }tt|�d|  �ada|dkrpd	at|�d�d	 �ad S )
Ni?B �d   ZHi�.�   �   �
   �Lowr   )�str�float�split�len�int�low�high)ZpersenZtaruhan�c�nZpangkat� r   � �konvert4   s    r   c             C   s�   t | �dk r4tdt | � �}|d t| � } d|  }t | �dkrjtdt | � �}|d t| � } d|  }n0t | �}| dd � }| d |d � }|d | }|S )N�   �0z0.i����r   )r   r   r   )ZnumZpanjang_nol�resultZlen_num�endZfirstr   r   r   �revB   s    
r"   c          	   C   s|  t jdkrFd}d}x<|d7 }ytd | d }W q   P Y qX qW n
tt j�}ttd | d �d }ttd | d �d }ttd | d	 td | d
 � t}dtd |ttt	dd�ddd�}�y�t
jtt|d�}	t�|	j�}
|
d t|
d � t|� }t|
d �t|� }t|
d t|
d � t|� | �d }ttd tttt|
d �t|� �d � � tdtd | d  � d}d}t�� �d�}t|�ttd � }�x�t jdk�rVt�� �d�}t|�t|d �k�r`t|�ttd � }|d7 }||k�rd}tdtd | d  � ttd | d �d }ttd | d �d }n
tt j�}td | d d dk�r>tt�ttd | d d �ttd | d d ��d�}tt|��}|d k�r�tj�d!t|� d" � |d#k�rtj�d!t|� d$ � |d%k�r&tj�d!t|� d& � t|td | d
 � n"ttd | d	 td | d
 � t �!t|�� t|�}|d7 }dtd |ttt	dd�ddd�}|ttd' �k�rttd( t d) t t|� � t"�#d*t|� � t �!d� t"�#d+ttt|
d �t|� �d � � t�$�  t
jtt|d�}	t�|	j�}
t|
d t|
d � t|� | �d }t|
d �t|� }|
d | k�r@tt%d, t t|
d- � t% d. t& tt|�d � tttt|
d �t|� �d � t&d/ tt|� � ttd0 � t"�#d1� t �!d� t"�#d+ttt|
d �t|� �d � � t�$�  |
d |k �rtt%d, t t|
d- � t% d2 t' d3 tt|�d � tttt|
d �t|� �d � t'd4 tt|� � tt(j)t*j+ d5 � t"�#d6� t �!d� t"�#d+ttt|
d �t|� �d � � t�$�  |
d dk	�r�t|
d �t|� }|dk�r�tt%d, t t|
d- � t% d. t& tt,t|��� ttt,t|��� t&d/ tt|� � nZtt%d, t t|
d- � t% d. t& tt,t|��� ttt,t|��� t'd4 tt|� � n�d}d7}t|
d �t|� }|dk�r�tt%d, t t|
d- � t% d2 t' d3 tt,t|��� ttt,t|��� t&d/ tt|� � n^tt%d, t t|
d- � t% d2 t' d3 tt,t|��� ttt,t|��� t'd4 tt|� � |d7k�r |d7 }t|�ttd | d8 � }||k�rPd}d}n0||k�r4d}t}nt|�ttd | d9 � }�q�W W n   t"�#d:� t�$�  Y nX d S );NZAutor   r   ZConfigzBet SetZIntervali�  zReset If WinZChanceZBetZPlaceBetZSessionCookiei?B Zdoge�2)�a�sZPayInr   ZHighZ
ClientSeedZCurrencyZProtocolVersion)�headers�dataZStartingBalanceZPayOuti ��z


Starting BalancezAnda Menggunakan BetSet Ke Fz%MzWaktu nya Ganti Betset zRandom ChanceZToggleZONZMinZMax�   �   �z   �   z  �   � zTarget Profitz$Yay.! 
Profit Mencapai Target.....!
zProfit ztermux-toast You win ztermux-toast Total Balance �[ZSecretz] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z&termux-toast Target Win Sudah Tercapai�]�-zLose zLose Target....!ztermux-toast Lose Target TzIf LosezIf Winztermux-toast Betting Stop)-�my_namespaceZbetset�objr   r   �payin�jsr   r   r   r   Zpost�url�ua�json�loads�textr   �print�hijau�resr   r   ZnowZstrftime�round�randomZuniformr   �sys�stdout�write�timeZsleep�os�system�exit�ungu�hijau2�red2r   �BRIGHTr   �REDr"   )ZwsZlsZurutZjumlahulangZpesanZslpZlimit_aZamountr'   Zr1ZjsnZjumblZjumZprofr   ZburstZmenitZwaktuZhasil_chanceZcokZbal�ir   r   r   �diceS   s�    

"(.

:


" 
*(j

*n

*
\\
`^


&
rL   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccount�Username�Passwordr   )r$   ZKeyrM   rN   ZTotp)r&   r'   zBalance ZDogeZBalancez%Check Your Username And Your Passwordg     @@z|

Maaf Versi Ini Cuma Support Untuk Balance Dibawah 500 Doge
Silahkan Hubungi Author Untuk Full Version
Hub : +6285336117892z
Target WinzLose Target)8Zrequestsr7   rB   r?   r>   rC   ZargparseZcoloramar   r   r   r   r   ZinitZArgumentParserZparserZadd_argumentZ
parse_argsr1   �openZmyfile�readr'   r8   r2   r:   ZNORMALZMAGENTAZGREENrI   ZDIMZWHITEZ	RESET_ALLrJ   r;   r<   Zabu2rF   rG   rH   Zsessionr   r5   r6   r   r   r3   r   r"   rL   �getr	   r9   r4   r   rE   r   r   r   r   �<module>   s\   8
� G ,4)�marshal�exec�loads� r   r   �out.py�<module>   s   