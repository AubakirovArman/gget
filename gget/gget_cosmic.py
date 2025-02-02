import requests
import pandas as pd
import json as json_package
import io
import logging

# Add and format time stamp in logging messages
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%c",
)
# Mute numexpr threads info
logging.getLogger("numexpr").setLevel(logging.WARNING)

# Custom functions
from .gget_info import info

# Constants
from .constants import COSMIC_GET_URL


def cosmic(
    name,
    limit=100,
    types="mutations",
    save=False,
    verbose=True,
    json=False
):
    """
    COSMIC, the Catalogue Of Somatic Mutations In Cancer, 
    is the world's largest and most comprehensive resource 
    for exploring the impact of somatic mutations in human cancer.
    Start using COSMIC by searching for a gene, cancer type, mutation, etc. below. 
    (https://cancer.sanger.ac.uk/cosmic/).

    Args:
    - name      by searching for a gene, cancer type, mutation, etc. below.
    - limit     Number of rows to return (default: 100).
    - types      'mutations' (default) or 'pubmed', 'genes','studies','samples'.
    - json          If True, returns results in json format instead of data frame. Default: False.
    - save          True/False whether to save the results in the local directory.
    - verbose        True/False whether to print progress information. Default True.

    Returns a data frame with the requested results.
    """

    # Check if 'species' argument is valid
    sps = ["mutations" ,"pubmed", "genes","studies","samples"]
    if types not in sps:
        raise ValueError(
            f"'type' argument specified as {types}. Expected one of: {', '.join(sps)}"
        )

    if verbose:
        logging.info(
            f"Fetching the {limit} most correlated to {name} from COSMIC."
        )

    r = requests.get(url=COSMIC_GET_URL+types+'?q='+name+'&export=json')

    if not r.ok:
        raise RuntimeError(
            f"Gene correlation API request returned with error code: {r.status_code}. "
            "Please double-check the arguments and try again.\n"
        )

    if r.text=='\n':
        raise RuntimeError(
            f"Your search term {name} did not return any results in {types} "
            "Please double-check the arguments and try again.\n"
        )
    data = r.text.split('\n')
    # Check if the request returned an error (e.g. gene not found)
    dicts={}
    if types == "mutations":
        dicts={
            'Gene':[],
            'Syntax':[],
            'Alternate IDs':[],
            'Canonical':[]
        }
        counter=0
        for i in data:
            if len(i)>2:
                parsing_mutations=i.split('\t')
                dicts['Gene'].append(parsing_mutations[0])
                dicts['Syntax'].append(parsing_mutations[1])
                dicts['Alternate IDs'].append(parsing_mutations[2])
                dicts['Canonical'].append(parsing_mutations[3])
                counter=counter+1
                if limit<counter:
                    break
    #pubmed logic  
    elif types == "pubmed":
        dicts={
            'Pubmed':[],
            'Paper title':[],
            'Author':[]
            }
        counter=0
        for i in data:
            if len(i)>2:
                parsing_mutations=i.split('\t')
                dicts['Pubmed'].append(parsing_mutations[0])
                dicts['Paper title'].append(parsing_mutations[1])
                dicts['Author'].append(parsing_mutations[2])
                counter=counter+1
                if limit<=counter:
                    break 
    elif types == "genes":
        dicts={
            'Gene':[],
            'Alternate IDs':[],
            'Tested samples':[],
            'Simple Mutations':[],
            'Fusions':[],
            'Coding':[],
            }
        counter=0
        for i in data:
            if len(i)>2:
                parsing_mutations=i.split('\t')
                dicts['Gene'].append(parsing_mutations[0])
                dicts['Alternate IDs'].append(parsing_mutations[1])
                dicts['Tested samples'].append(parsing_mutations[2])
                dicts['Simple Mutations'].append(parsing_mutations[3])
                dicts['Fusions'].append(parsing_mutations[4])
                dicts['Coding'].append(parsing_mutations[5])
                counter=counter+1
                if limit<counter:
                    break 
    elif types == "samples":
        dicts={
            'Sample Name':[],
            'Sites &amp; Histologies':[],
            'Analysed Genes':[],
            'Mutations':[],
            'Fusions':[],
            'Structual variants':[],
            }
        counter=0
        for i in data:
            if len(i)>2:
                parsing_mutations=i.split('\t')
                dicts['Sample Name'].append(parsing_mutations[0])
                dicts['Sites &amp; Histologies'].append(parsing_mutations[1])
                dicts['Analysed Genes'].append(parsing_mutations[2])
                dicts['Mutations'].append(parsing_mutations[3])
                dicts['Fusions'].append(parsing_mutations[4])
                dicts['Structual variants'].append(parsing_mutations[5])
                counter=counter+1
                if limit<counter:
                    break 
    elif types == "studies":
        dicts={
            'Study Id':[],
            'Project Code':[],
            'Description':[],
            }
        counter=0
        for i in data:
            if len(i)>2:
                parsing_mutations=i.split('\t')
                dicts['Study Id'].append(parsing_mutations[0])
                dicts['Project Code'].append(parsing_mutations[1])
                dicts['Description'].append(parsing_mutations[2])
                counter=counter+1
                if limit<counter:
                    break 

    # Build data frame from returned results
    corr_df = pd.DataFrame(dicts)
    # Drop the first row (since that is the searched gene against itself)
    if json:
        results_dict = json_package.loads(corr_df.to_json(orient="records"))
        if save:
            with open(
                f"gget_cosmic_{types}-name_{name}.json", "w", encoding="utf-8"
            ) as f:
                json_package.dump(results_dict, f, ensure_ascii=False, indent=4)

        return results_dict
    else:
        if save:    
            corr_df.to_csv(f"gget_cosmic_{types}-name_{name}.csv", index=False)
        return corr_df
