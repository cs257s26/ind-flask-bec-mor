DROP TABLE IF EXISTS llm_energy;
CREATE TABLE llm_energy (
  model_name varchar(50),
  model_params varchar(20),
  gpu_type varchar(20),
  num_gpus varchar(20),
  training_hours varchar(20), 
  data_center_region varchar(50), 
  hardware_watts varchar(20), 
  carbon_emissions varchar(20), 
  energy_kwh varchar(20), 
  carbon_footprint varchar(20)
);
