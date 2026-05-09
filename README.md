# README

# Database project. 
## Commands 
Copy command: \copy llm_energy FROM 'llmenergy.csv' DELIMITER ',' CSV

## Written responses 
### Question One 
When creating the database, it was challenging to choose what datatypes to use. In the data we use, some LLMs do not disclose or specify certain parameters. However, when I was cleaning the data, I felt like it would be misrepresenting my data to just delete all of the LLMs who do not include all of the information. I made the choice to include all of the numerical information as the varchar type. From my brief research on the postgresql documentation, it seemed like the best datatype to store both strings, integers, and decimals. It is also possible to convert the numbers back to an integer type in the future. I selected on table because I feel like all of the data centers around the model names and it is not too large of a dataset. I removed two columns because we have not used them in any of the previous assignments. The primary key is the model_name. 

### Question Two 
My user stories centered around being able to retrieve data in various ways. My first user story was collecting a column, which for our dataset meant learning all of the various information about a specific LLM. My first queries takes in an LLM name and returns its row, which matches the user story completely. My other query returns a specified column, which is my other user story. If a user inputs one of the keys for the database, they are able to view all of the information in that column. 

# Individual Flask project.

## get_column 
To view any column, enter http://127.0.0.1:PORT/0/column_name/"
### Valid columns: 
- Model name
- model_parameters_billion
- training_tokens_billion
- gpu_type
- num_gpus
- training_hours
- data_center_region
- PUE
- hardware_power_draw_watts_per_gpu
- carbon_intensity_gco2_per_kwh
- total_energy_kwh
- total_carbon_footprint_kgco2e

## get_row 
To view any row, enter http://127.0.0.1:PORT/row_name/"
### Valid rows: 
- GPT-3
- GPT-4 
- PaLM
- BLOOM
- DeepSeek-V3 
- Llama_3.1
- Claude_3_Opus 
- Claude_3_Sonnet
- Claude_3_Haiku
- Gemini_1.0_Ultra
- Gemini_1.5_Pro
- T5
- GShard
- Switch
- XLM
- Chinchilla
- GLaM
- Falcon_180B
- Mistral_7B
- Mixtral_8x7B
- Qwen_72B
- Yi-34B
- Grok 3
- Gopher
- OPT-175B 
- Gemma_7B 
- Vicuna_7B