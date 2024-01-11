# **DICCIONARIO DE DATOS** - [Link](https://github.com/feedzai/bank-account-fraud/blob/main/documents/datasheet.pdf)

### Tamaño del dataset: 

+ **Filas:** 1 millón.
+ **Columnas:** 32.

### Cantidad de variables por tipo:

- <font color='orange'>**Numéricas**</font>: 20 variables.
- <font color='lightgreen'>**Categóricas**</font>: 5 variables.
- <font color='yellow'>**Binarias**</font>: 7 variables.

### Resumen de las variables:

1. **income** (<font color='orange'>numérica</font>): Renta anual del solicitante (en forma de decil). Rangos entre
[0.1, 0.9].

2. **name_email_similarity** (<font color='orange'>numérica</font>): Métrica de similitud entre el correo electrónico y el nombre del
del candidato. Los valores más altos representan una mayor similitud. Oscila entre [0, 1].

3. **prev_address_months_count** (<font color='orange'>numérica</font>): Número de meses en la dirección registrada
del solicitante, es decir, la residencia anterior del solicitante, si procede. Rangos
entre [-1, 380] meses (-1 es un valor que falta).

4. **current_address_months_count** (<font color='orange'>numérica</font>): Meses en la dirección actualmente registrada del
del solicitante. Oscila entre [-1, 429] meses (-1 es un valor ausente).

5. **customer_age** (<font color='orange'>numérica</font>): Edad del solicitante en años, redondeada a la década. Rangos
entre [10, 90] años.

6. **days_since_request** (<font color='orange'>numérica</font>): Número de días transcurridos desde que se realizó la solicitud.
Oscila entre [0, 79] días.

7. **intended_balcon_amount** (<font color='orange'>numérica</font>): Importe inicial transferido para la solicitud.
Oscila entre [-16, 114] (los valores negativos son valores omitidos).

8. **payment_type** (<font color='lightgreen'>categórica</font>): Tipo de plan de pago del crédito. 5 posibles valores (anonimizados).

9. **zip_count_4w** (<font color='orange'>numérica</font>): Número de solicitudes dentro del mismo código postal en las últimas 4 semanas.
Rangos entre [1, 6830].

10. **velocity_6h** (<font color='orange'>numérica</font>): Velocidad del total de solicitudes realizadas en las últimas 6 horas, es decir, número medio de solicitudes por hora en las últimas 6 horas.
de solicitudes por hora en las últimas 6 horas. Oscila entre [-175, 16818].

11. **velocity_24h** (<font color='orange'>numérica</font>): Velocidad del total de solicitudes realizadas en las últimas 24 horas, es decir, número medio de solicitudes por hora en las últimas 6 horas.
de solicitudes por hora en las últimas 24 horas.

12. **velocity_4w** (<font color='orange'>numérica</font>): Velocidad del total de solicitudes realizadas en las últimas 4 semanas, es decir, media
de solicitudes por hora en las últimas 4 semanas. Rangos entre [2825, 7020].

13. **bank_branch_count_8w** (<font color='orange'>numérica</font>): Número de solicitudes totales en la sucursal bancaria
bancaria seleccionada en las últimas 8 semanas. Rangos entre [0, 2404].

14. **date_of_birth_distinct_emails_4w** (<font color='orange'>numérica</font>): Número de correos electrónicos de solicitantes con
misma fecha de nacimiento en las últimas 4 semanas. Rangos entre [0, 39].

15. **employment_status** (<font color='lightgreen'>categórica</font>): Situación laboral del solicitante. 7 posibles
(anónimos) posibles.

16. **credit_risk_score** (<font color='orange'>numérica</font>): Puntuación interna del riesgo de la solicitud. Oscila entre
[-191, 389].

17. **email_is_free** (<font color='yellow'>binaria</font>): Dominio del correo electrónico de la solicitud (gratuito o de pago).

18. **housing_status** (<font color='lightgreen'>categórica</font>): Estado residencial actual del solicitante. 7 posibles
(anónimos) posibles.

19. **phone_home_valid** (<font color='yellow'>binaria</font>): Validez del teléfono particular facilitado.

20. **phone_mobile_valid** (<font color='yellow'>binaria</font>): Validez del teléfono móvil facilitado.

21. **bank_months_count** (<font color='orange'>numérica</font>): Antigüedad de la cuenta anterior (si se tiene) en meses.
Oscila entre [-1, 32] meses (-1 es un valor omitido).

22. **has_other_cards** (<font color='yellow'>binaria</font>): Si el solicitante tiene otras tarjetas de la misma empresa bancaria.
bancaria.

23. **proposed_credit_limit** (<font color='orange'>numérica</font>): Límite de crédito propuesto por el solicitante. Oscila entre
[200, 2000].

24. **foreign_request** (<font color='yellow'>binaria</font>): Si el país de origen de la solicitud es distinto del país del banco.

25. **source** (<font color='lightgreen'>categórica</font>): Fuente en línea de la solicitud. Navegador (INTERNET) o
aplicación (TELEAPP).

26. **session_length_in_minutes** (<font color='orange'>numérica</font>): Duración de la sesión del usuario en el sitio web bancario en
minutos. Oscila entre [-1, 107] minutos (-1 es un valor omitido).

27. **device_os** (<font color='lightgreen'>categórica</font>): Sistema operativo del dispositivo que realizó la solicitud. Los valores posibles
son: Windows, macOS, Linux, X11 u otro.

28. **keep_alive_session** (<font color='yellow'>binaria</font>): Opción del usuario en el cierre de sesión.

29. **device_distinct_emails_8w** (<font color='orange'>numérica</font>): Número de correos electrónicos distintos en el sitio web bancario desde
el dispositivo utilizado en las últimas 8 semanas. Oscila entre [-1, 2] correos electrónicos (-1 es un valor omitido).

30. **device_fraud_count** (<font color='orange'>numérica</font>): Número de solicitudes fraudulentas con el dispositivo utilizado.
Rangos entre [0, 1].

31. **month** (<font color='orange'>numérica</font>): Mes en el que se realizó la solicitud. Rangos entre [0, 7].

32. **fraud_bool** (<font color='yellow'>binaria</font>): Si la solicitud es fraudulenta o no.  

