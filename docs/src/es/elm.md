> Parámetros de Python són iguales a los parámetros largos (`--parámetro`) de Terminal, si no especificado de otra manera. Banderas son parámetros de verdadero o falso (True/False) en Python. El manuál para cualquier modulo de gget se puede llamar desde la Terminal con la bandera `-h` `--help`.  
## gget elm 🎭
Prediga localmente motivos lineales eucarióticos (ELMs) a partir de una secuencia de aminoácidos o UniProt ID utilizando datos de la [base de datos ELM](http://elm.eu.org/).  
Produce: Resultados en formato JSON (Terminal) o Dataframe/CSV (Python). Este módulo devuelve dos tipos de resultados (ver ejemplos).   

Antes de usar `gget elm` por primera vez, ejecute `gget setup elm` / `gget.setup("elm")` una vez (consulte también [`gget setup`](setup.md)).   

**Parámetro posicional**  
`sequence`  
Secuencia de aminoácidos o ID de Uniprot (str).  
Al proporcionar una ID de Uniprot, use la bandera `--uniprot` (Python: `uniprot==True`).  

**Parámetros optionales**  
`-s` `sensitivity`  
Sensibilidad de la alineación DIAMOND (str). Por defecto: "very-sensitive" (muy sensible).  
Uno de los siguientes: fast, mid-sensitive, sensitive, more-sensitive, very-sensitive, or ultra-sensitive.  

`-t` `threads`  
Número de hilos de procesamiento utilizados en la alineación de secuencias con DIAMOND (int). Por defecto: 1.  

`-bin` `diamond_binary`  
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
Encuentre ELM en una secuencia de aminoácidos:  
```bash
gget setup elm          # Descarga/actualiza la base de datos ELM local
gget elm -o gget_elm_results LIAQSIGQASFV
```
```python
# Python
gget.setup(“elm”)      # Descarga/actualiza la base de datos ELM local
ortholog_df, regex_df = gget.elm("LIAQSIGQASFV")
```
  
Encuentre ELM que proporcionen un ID de UniProt como entrada: 
```bash
gget setup elm          # Descarga/actualiza la base de datos ELM local
gget elm -o gget_elm_results --uniprot Q02410
```
```python
# Python
gget.setup(“elm”)      # Descarga/actualiza la base de datos ELM local
ortholog_df, regex_df = gget.elm("Q02410", uniprot=True)
```
&rarr; Produce dos resultados con información extensa sobre ELMs asociados con proteínas ortólogas y motivos encontrados en la secuencia de entrada directamente en función de sus expresiones regex:  

Ortholog data frame:  
|Ortholog_UniProt_ID|ProteinName|class_accession|ELMIdentifier  |FunctionalSiteName                   |Description                                                                                                                              |Regex                        |Probability      |Methods                                                                                                             |Organism    |query_seq_length|subject_seq_length|alignment_length|identity_percentage|motif_in_query|query_start|query_end|subject_start|subject_end|motif_start_in_subject|motif_end_in_subject|References      |InstanceLogic|PDB |#Instances|#Instances_in_PDB|
|-------------------|-----------|---------------|---------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------|------------|----------------|------------------|----------------|-------------------|--------------|-----------|---------|-------------|-----------|----------------------|--------------------|----------------|-------------|----|----------|-----------------|
|Q02410             |APBA1_HUMAN|ELME000357     |LIG_CaMK_CASK_1|CASK CaMK domain binding ligand motif|Motif that mediates binding to the calmodulin-dependent protein kinase (CaMK) domain of the peripheral plasma membrane protein CASK/Lin2.|[STED].{0,2}[IV]W[IVLM].[RHK]|1.11776693962e-05|comigration in gel electrophoresis; far western blotting; glutathione s tranferase tag; mutation analysis; pull down|Homo sapiens|                |                  |                |                   |              |           |         |             |           |376                   |382                 |9952408 21763699|true positive|    |7         |3                |
|Q02410             |APBA1_HUMAN|ELME000091     |LIG_PDZ_Class_2|PDZ domain ligands                   |The C-terminal class 2 PDZ-binding motif is classically represented by a pattern such as (VYF)X(VIL)*                                    |...[VLIFY].[ACVILF]$         |7.88851572129e-05|mutation analysis; nuclear magnetic resonance; two hybrid                                                           |Homo sapiens|                |                  |                |                   |              |           |         |             |           |832                   |837                 |16007100        |true positive|1U38|13        |8                |


Regex data frame:  
|Instance_accession|ELMIdentifier      |FunctionalSiteName                         |ELMType|Description                                                                                                                                                                                                 |Regex                      |Instances (Matched Sequence)|motif_start_in_query|motif_end_in_query|ProteinName     |Organism                                                           |References                         |InstanceLogic |#Instances|#Instances_in_PDB|
|------------------|-------------------|-------------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------|--------------------|------------------|----------------|-------------------------------------------------------------------|-----------------------------------|--------------|----------|-----------------|
|ELME000321        |CLV_C14_Caspase3-7 |Caspase cleavage motif                     |CLV    |Caspase-3 and Caspase-7 cleavage site.                                                                                                                                                                      |[DSTE][^P][^DEWHFYC]D[GSAN]|EIGDA                       |199                 |204               |A0A0H3NIK3_SALTS|Salmonella enterica subsp. enterica serovar Typhimurium str. SL1344|20947770                           |true positive |41        |0                |
|ELME000321        |CLV_C14_Caspase3-7 |Caspase cleavage motif                     |CLV    |Caspase-3 and Caspase-7 cleavage site.                                                                                                                                                                      |[DSTE][^P][^DEWHFYC]D[GSAN]|DLIDG                       |453                 |458               |STK4_HUMAN      |Homo sapiens                                                       |11278283 11278782                  |true positive |41        |0                |
|ELME000321        |CLV_C14_Caspase3-7 |Caspase cleavage motif                     |CLV    |Caspase-3 and Caspase-7 cleavage site.                                                                                                                                                                      |[DSTE][^P][^DEWHFYC]D[GSAN]|DLIDG                       |453                 |458               |VDR_HUMAN       |Homo sapiens                                                       |18832097                           |true positive |41        |0                |
|ELME000102        |CLV_NRD_NRD_1      |NRD cleavage site                          |CLV    |N-Arg dibasic convertase (NRD/Nardilysin) cleavage site (X-&#124;-R-K or R-&#124;-R-X).                                                                                                                               |(.RK)&#124;(RR[^KR])            |RRA                         |142                 |145               |PDYN_RAT        |Rattus norvegicus                                                  |8294457                            |true positive |2         |0                |
|ELME000102        |CLV_NRD_NRD_1      |NRD cleavage site                          |CLV    |N-Arg dibasic convertase (NRD/Nardilysin) cleavage site (X-&#124;-R-K or R-&#124;-R-X).                                                                                                                               |(.RK)&#124;(RR[^KR])            |RRA                         |142                 |145               |SMS_RAT         |Rattus norvegicus                                                  |8294457                            |true positive |2         |0                |
|ELME000108        |CLV_PCSK_KEX2_1    |PCSK cleavage site                         |CLV    |Yeast kexin 2 cleavage site (K-R-&#124;-X or R-R-&#124;-X).                                                                                                                                                           |[KR]R.                     |KRQ                         |581                 |584               |CIS3_YEAST      |Saccharomyces cerevisiae S288c                                     |10438739                           |true positive |1         |0                |
|ELME000146        |CLV_PCSK_SKI1_1    |PCSK cleavage site                         |CLV    |Subtilisin/kexin isozyme-1 (SKI1) cleavage site ([RK]-X-[hydrophobic]-[LTKF]-&#124;-X).                                                                                                                          |[RK].[AILMFV][LTKF].       |RLLTA                       |825                 |830               |ATF6A_HUMAN     |Homo sapiens                                                       |11163209                           |true positive |2         |0                |
|ELME000146        |CLV_PCSK_SKI1_1    |PCSK cleavage site                         |CLV    |Subtilisin/kexin isozyme-1 (SKI1) cleavage site ([RK]-X-[hydrophobic]-[LTKF]-&#124;-X).                                                                                                                          |[RK].[AILMFV][LTKF].       |RLLTA                       |825                 |830               |SRBP2_HUMAN     |Homo sapiens                                                       |9139737                            |true positive |2         |0                |
|ELME000231        |DEG_APCC_DBOX_1    |APCC-binding Destruction motifs            |DEG    |An RxxL-based motif that binds to the Cdh1 and Cdc20 components of APC/C thereby targeting the protein for destruction in a cell cycle dependent manner                                                     |.R..L..[LIVM].             |SRVKLNIVR                   |732                 |741               |ACM1_YEAST      |Saccharomyces cerevisiae S288c                                     |23707760 18596038 18498748 18519589|true positive |18        |3                |
|ELME000231        |DEG_APCC_DBOX_1    |APCC-binding Destruction motifs            |DEG    |An RxxL-based motif that binds to the Cdh1 and Cdc20 components of APC/C thereby targeting the protein for destruction in a cell cycle dependent manner                                                     |.R..L..[LIVM].             |SRVKLNIVR                   |732                 |741               |AURKB_HUMAN     |Homo sapiens                                                       |16204042 15923616                  |false positive|18        |3                |
|ELME000231        |DEG_APCC_DBOX_1    |APCC-binding Destruction motifs            |DEG    |An RxxL-based motif that binds to the Cdh1 and Cdc20 components of APC/C thereby targeting the protein for destruction in a cell cycle dependent manner                                                     |.R..L..[LIVM].             |SRVKLNIVR                   |732                 |741               |STK6A_XENLA     |Xenopus laevis                                                     |12208850 11707286                  |false positive|18        |3                |
|ELME000231        |DEG_APCC_DBOX_1    |APCC-binding Destruction motifs            |DEG    |An RxxL-based motif that binds to the Cdh1 and Cdc20 components of APC/C thereby targeting the protein for destruction in a cell cycle dependent manner                                                     |.R..L..[LIVM].             |SRVKLNIVR                   |732                 |741               |STK6_HUMAN      |Homo sapiens                                                       |15536123                           |false positive|18        |3                |
|ELME000353        |DEG_Nend_UBRbox_3  |N-degron                                   |       |N-terminal motif that initiates protein degradation by binding to the UBR-box of N-recognins. This N-degron variant comprises N-terminal Asn or Gln as destabilizing residue.                               |^M{0,1}([NQ]).             |MNH                         |0                   |3                 |                |                                                                   |                                   |              |0         |0                |
|ELME000322        |DEG_SCF_SKP2-CKS1_1|SCF ubiquitin ligase binding Phosphodegrons|DEG    |Degradation motif recognised by a pre-assembled complex consisting of Skp2 (an F box protein of the SCF E3 ubiquitin ligase) and Cks1, which leads to ubiquitylation and subsequent proteosomal degradation.|..[DE].(T)P.K              |LSDKTPSK                    |471                 |479               |CDN1B_HUMAN     |Homo sapiens                                                       |16209941                           |true positive |3         |1                |
|ELME000322        |DEG_SCF_SKP2-CKS1_1|SCF ubiquitin ligase binding Phosphodegrons|DEG    |Degradation motif recognised by a pre-assembled complex consisting of Skp2 (an F box protein of the SCF E3 ubiquitin ligase) and Cks1, which leads to ubiquitylation and subsequent proteosomal degradation.|..[DE].(T)P.K              |LSDKTPSK                    |471                 |479               |CDN1C_HUMAN     |Homo sapiens                                                       |12925736                           |true positive |3         |1                |
|ELME000388        |DEG_SPOP_SBC_1     |SPOP SBC docking motif                     |DEG    |The S/T rich motif known as the SPOP-binding consensus (SBC) of the MATH-BTB protein, SPOP, is present in substrates that undergo SPOP/Cul3-dependant ubiquitination.                                       |[AVP].[ST][ST][ST]         |AESSS                       |411                 |416               |Q9VHV8_DROME    |Drosophila melanogaster                                            |19818708                           |true positive |8         |6                |
|ELME000485        |DOC_CDC14_PxL_1    |Yeast Cdc14 phosphatase docking site       |DOC    |The PxL substrate docking motif enhances the Cdc14 phosphatase‚Äìsubstrate interaction and promotes subsequent dephosphorylation.                                                                           |[FYLIM]..[YVILA]P.L..      |IGDAPELDA                   |200                 |209               |ACE2_YEAST      |Saccharomyces cerevisiae S288c                                     |27826861                           |unknown       |10        |2                |
|…                 |…                  |…                                          |…      |…                                                                                                                                                                                                           |…                          |…                           |…                   |…                 |…               |…                                                                  |…                                  |…             |…         |…                |

(Los motivos que aparecen en muchas especies diferentes pueden parecer repetidos, pero todas las filas deben ser únicas.)

#### [Màs ejemplos](https://github.com/pachterlab/gget_examples)  
