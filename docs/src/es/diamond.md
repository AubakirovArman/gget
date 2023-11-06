> Parámetros de Python són iguales a los parámetros largos (`--parámetro`) de Terminal, si no especificado de otra manera. Las banderas son parámetros de verdadero o falso (True/False) en Python. El manuál para cualquier modulo de gget se puede llamar desde la Terminal con la bandera `-h` `--help`.  
## gget diamond 💎
Alinee múltiples proteínas o secuencias de ADN traducidas usando [DIAMOND](https://www.nature.com/articles/nmeth.3176) (DIAMOND es similar a BLAST, pero este es un cálculo local).       
Produce: Resultados en formato JSON (Terminal) o Dataframe/CSV (Python).  

**Parámetro posicional**  
`query`  
Secuencia(s) (str o lista) de aminoácidos, o una ruta a un archivo tipo FASTA.    

**Parámetro requerido**  
`-ref` `--reference`  
Secuencias de aminoácidos de referencia (str o lista), o una ruta a un archivo tipo FASTA.  

**Parámetros optionales**  
`-db` `--diamond_db`  
Ruta para guardar la base de datos DIAMOND creada a partir de `reference` (str).  
Por defecto: None -> El archivo de base de datos DIAMOND temporal se eliminará después de la alineación o se guardará en `out` si se proporciona `out`.  

`-s` `--sensitivity`  
Sensibilidad de la alineación (str). Por defecto: "very-sensitive" (muy sensible).  
Uno de los siguientes: fast, mid-sensitive, sensitive, more-sensitive, very-sensitive, or ultra-sensitive.    

`-t` `--threads`  
Número de hilos de procesamiento utilizados (int). Por defecto: 1.  

`-db` `--diamond_binary`  
Ruta al binario DIAMOND (str). Por defecto: None -> Utiliza el binario DIAMOND instalado automáticamente con `gget`.  

`-o` `--out`   
Ruta al archivo en el que se guardarán los resultados (str), p. ej. "ruta/al/directorio". Por defecto: salida estándar (STDOUT); los archivos temporales se eliminan.    

**Banderas**  
`-u` `--uniprot`  
Use esta bandera cuando `sequence` es un ID de Uniprot en lugar de una secuencia de aminoácidos.      

`-csv` `--csv`  
Solo para Terminal. Produce los resultados en formato CSV.    
Para Python, usa `json=True` para producir los resultados en formato JSON.  

`-q` `--quiet`   
Solo para Terminal. Impide la información de progreso de ser exhibida durante la ejecución del programa.  
Para Python, usa `verbose=False` para impedir la información de progreso de ser exhibida durante la ejecución del programa.  

### Ejemplo
```bash
# !!! Asegúrese de enumerar primero el argumento posicional aquí para que no se agregue como secuencia de referencia
gget diamond GGETISAWESQME ELVISISALIVE LQVEFRANKLIN PACHTERLABRQCKS -ref GGETISAWESQMEELVISISALIVELQVEFRANKLIN PACHTERLABRQCKS
```
```python
# Python
gget.diamond(["GGETISAWESQME", "ELVISISALIVE", "LQVEFRANKLIN", "PACHTERLABRQCKS"], reference=["GGETISAWESQMEELVISISALIVELQVEFRANKLIN", "PACHTERLABRQCKS"])
```
&rarr; Produce los resultados de la alineación en formato JSON (Terminal) o Dataframe/CSV:  


#### [Màs ejemplos](https://github.com/pachterlab/gget_examples)
