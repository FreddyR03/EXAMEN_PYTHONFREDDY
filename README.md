#  Simulador de Propina (Consola - Python)

## 📌 Descripción

**Simulador de Propina** es una aplicación de consola sencilla desarrollada en **Python**, que permite calcular la propina a dejar en un restaurante en función del monto total de la cuenta y el porcentaje seleccionado por el usuario.  

Además, ofrece la opción de **dividir el total (incluyendo propina) entre varias personas**, mostrando claramente cuánto debe pagar cada una.  

Este proyecto busca facilitar el cálculo de propinas y totales a pagar en situaciones cotidianas, como salidas a restaurantes.

---

##  Problema que resuelve

En muchos restaurantes, la propina no está incluida automáticamente en la cuenta, por lo que el cliente debe calcularla manualmente.  
Dependiendo del servicio, la propina puede variar (10 %, 15 %, 20 % o personalizada).  
Este programa permite:

- Calcular fácilmente el valor de la propina.
- Obtener el total a pagar con la propina incluida.
- Dividir el pago entre varias personas de forma justa.

---

##  Flujo de uso 

1. El usuario ingresa el monto de la cuenta (por ejemplo, **$50**).
2. Elige el porcentaje de propina (por ejemplo, **15 %**).
3. El programa calcula la propina (**$7.50**) y el total a pagar (**$57.50**).
4. Si el usuario desea dividir entre varias personas (por ejemplo, **4 personas**), el programa calcula que cada una debe pagar **$14.38**.

---

##  Funcionalidades principales

- **Ingreso del monto total de la cuenta**  
- **Selección del porcentaje de propina** (10 %, 15 %, 20 % o personalizado)  
- **Cálculo de propina** y **total a pagar**  
- **División del total entre varias personas** (opcional)  
- **Validaciones** para evitar montos o porcentajes en cero  
- **Menú interactivo de consola** para elegir opciones fácilmente

---

##  Funciones específicas

| Función | Descripción |
|---------|-------------|
| `porcentaje_de_propina()` | Calcula la propina y el total cuando paga **una sola persona**. |
| `porcentaje_de_propina_varias_personas()` | Calcula la propina y divide el total entre **varias personas**. |
| `menu_principal()` | Muestra el menú principal para elegir entre pagar individualmente, dividir entre varias personas o salir. |

---

##  Ejemplo de salida

```
------RESTAURANTE DON FREDDY------

1. Va a pagar el total con la propina 1 sola persona
2. Va a pagar el total con la propina varias personas
3. Salir

Ingrese la opción que desea: 1

------- Menú del cliente -------
Ingrese el porcentaje de propina que quieres agregar

1. 10%
2. 15%
3. 20%
4. Ingresar porcentaje personalizado
5. Salir

Ingresa la opción que desea usar: 2
Ingrese el monto total de la cuenta: 50
El total del monto $50.0 más la propina $7.5 es de $57.5
```

###  División entre varias personas

```
Ingresa la opción que desea usar: 2
Ingrese el monto total de la cuenta: 50
Ingrese cuántas personas van a pagar la propina: 4
El total del monto $50.0 más la propina $7.5 que tienen que pagar las 4 personas es de $14.38 cada una.
```

---

##  Requisitos

- **Python 3.7 o superior**
- Consola de comandos o terminal

---

## 🚀 Ejecución

1. Clona este repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/tu-usuario/simulador-propina.git
   cd simulador-propina
   ```

2. Ejecuta el programa:
   ```bash
   python menu_principal.py
   ```

---

## 📂 Estructura del proyecto

```
simulador-propina/
│
├── calculos.py             # Contiene las funciones de cálculo de propina
├── main.py                 # Contiene el menú principal y la ejecución del programa
├── README.md               # Documentación del proyecto
```

---

##  Posibles mejoras futuras

* Interfaz gráfica con Tkinter o PyQt.
* Validaciones adicionales de entrada (manejo de excepciones).
* Opción de múltiples monedas.
* Registro histórico de cálculos.

---

##  Autor

**Freddy Ramón**  
Proyecto desarrollado como ejercicio práctico de programación básica en Python.  


---

## 📸 Salida esperada

**Visualización en consola** mostrando la propina calculada, el total con propina y la división por persona (si aplica).

```
Total: $50.00
Propina (15%): $7.50
Total a pagar: $57.50
Cada persona (4): $14.38
```

---
