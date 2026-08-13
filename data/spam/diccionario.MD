<div style="text-align: justify; line-height: 1.5; font-size: 18px;"> 

<div align="center">

# **Descripción General de los Datos**

</div>

La base de datos corresponde a un conjunto de correos electrónicos utilizado para el análisis y detección automática de spam mediante técnicas de Machine Learning.

Cada observación representa un correo electrónico y las variables describen características textuales y tipográficas extraídas de su contenido.

Las variables incluyen principalmente:

- frecuencias de palabras específicas asociadas a correos spam,
- frecuencias de caracteres especiales,
- patrones de uso de mayúsculas,
- y términos relacionados con promociones, negocios o tecnología.

Muchas variables representan el porcentaje de aparición de ciertas palabras dentro del correo electrónico, por ejemplo:

- `free`
- `money`
- `credit`
- `business`
- `remove`

las cuales suelen ser frecuentes en mensajes spam.

Además, el conjunto de datos contiene variables relacionadas con:

- signos de puntuación (`!`, `$`, `#`),
- cadenas numéricas frecuentes,
- y estadísticas sobre letras mayúsculas.

La variable objetivo es:

<div align="center">

| Variable | Descripción |
|---|---|
| `type` | 1 = Spam, 0 = No Spam |


</div>

El objetivo principal es construir modelos de clasificación capaces de identificar automáticamente correos spam a partir de patrones lingüísticos y estadísticos presentes en los mensajes.

---
---

<div align="center">

| **Variable** | **Descripción** |
|---|---|
| make | Frecuencia de la palabra "make" |
| address | Frecuencia de la palabra "address" |
| all | Frecuencia de la palabra "all" |
| num3d | Frecuencia de la cadena "3d" |
| our | Frecuencia de la palabra "our" |
| over | Frecuencia de la palabra "over" |
| remove | Frecuencia de la palabra "remove" |
| internet | Frecuencia de la palabra "internet" |
| order | Frecuencia de la palabra "order" |
| mail | Frecuencia de la palabra "mail" |
| receive | Frecuencia de la palabra "receive" |
| will | Frecuencia de la palabra "will" |
| people | Frecuencia de la palabra "people" |
| report | Frecuencia de la palabra "report" |
| addresses | Frecuencia de la palabra "addresses" |
| free | Frecuencia de la palabra "free" |
| business | Frecuencia de la palabra "business" |
| email | Frecuencia de la palabra "email" |
| you | Frecuencia de la palabra "you" |
| credit | Frecuencia de la palabra "credit" |
| your | Frecuencia de la palabra "your" |
| font | Frecuencia de la palabra "font" |
| num000 | Frecuencia de la cadena "000" |
| money | Frecuencia de la palabra "money" |
| hp | Frecuencia de la palabra "hp" |
| hpl | Frecuencia de la palabra "hpl" |
| george | Frecuencia de la palabra "george" |
| num650 | Frecuencia de la cadena "650" |
| lab | Frecuencia de la palabra "lab" |
| labs | Frecuencia de la palabra "labs" |
| telnet | Frecuencia de la palabra "telnet" |
| num857 | Frecuencia de la cadena "857" |
| data | Frecuencia de la palabra "data" |
| num415 | Frecuencia de la cadena "415" |
| num85 | Frecuencia de la cadena "85" |
| technology | Frecuencia de la palabra "technology" |
| num1999 | Frecuencia de la cadena "1999" |
| parts | Frecuencia de la palabra "parts" |
| pm | Frecuencia de la palabra "pm" |
| direct | Frecuencia de la palabra "direct" |
| cs | Frecuencia de la palabra "cs" |
| meeting | Frecuencia de la palabra "meeting" |
| original | Frecuencia de la palabra "original" |
| project | Frecuencia de la palabra "project" |
| re | Frecuencia de la palabra "re" |
| edu | Frecuencia de la palabra "edu" |
| table | Frecuencia de la palabra "table" |
| conference | Frecuencia de la palabra "conference" |
| charSemicolon | Frecuencia del carácter ";" |
| charRoundbracket | Frecuencia del carácter "(" |
| charSquarebracket | Frecuencia del carácter "[" |
| charExclamation | Frecuencia del carácter "!" |
| charDollar | Frecuencia del carácter "$" |
| charHash | Frecuencia del carácter "#" |
| capitalAve | Promedio de longitud de secuencias en mayúsculas |
| capitalLong | Longitud máxima de secuencias en mayúsculas |
| capitalTotal | Número total de letras mayúsculas |
| type | Variable objetivo: 1 = Spam, 0 = No Spam |

---
---

</div>


</div>