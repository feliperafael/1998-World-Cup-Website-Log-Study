# 1998WorldCupWebsiteLogStudy
This repositoy contains a study of access logs from the 1998 World Cup Web site (www.france98.com).  
The log files are available for download at: http://ita.ee.lbl.gov/html/contrib/WorldCup.html

<span>How to run the script:</span><br>

In terminal: $python main.py wc_day13_1.gz<br>
Where the wc_day13_1.gz file should be inside the folder
ita_public_tools/input/<br>
<b>If log files are not provided a default test log will be used</b><br><br>

<hr>
In this study, the clientID was used to identify the user<br>

<b>clientID</b> - a unique integer identifier for the client that issued the
request (this may be a proxy); due to privacy concerns these mappings
cannot be released; note that each clientID maps to exactly one IP
address, and the mappings are preserved across the entire data set -
that is if IP address 0.0.0.0 mapped to clientID X on day Y then any
request in any of the data sets containing clientID X also came from
IP address 0.0.0.0



**A brief review**
d) Is it possible to model the behavior of users throughout a game?

Não é possivel modelar o comportamento do usuario ao longo de um jogo pois não existe a informação de quando um jogo começa e termina. Existe apenas a informação das requisições ao longo do dia.
Porém é possivel inferir quando o jogo esta acontecendo com base nas tendencias de alta de requisições de cada log. Por exemplo a maioria dos logs tem altas no numero de requisições durante invervalos de cerca de 3 horas. O pico desse intervalo deve conhecidir em algum lugar da duração do jogo, e a queda do numero de requisições deve acontecer com o termino do jogo.
